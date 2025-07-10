#!/bin/bash

# Exit on error
set -e

# Formatting
POS='\033[0;32m' # positive
NEG='\033[0;31m' # negative
WRN='\033[1;33m' # warning
INF='\033[0;36m' # info
RST='\033[0m'    # reset
IMP='\033[1m'    # important

# Define paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${SCRIPT_DIR}/../"
SRC_ROOT="${SCRIPT_DIR}/../src"

# Configure fallback for settings
VERSION="main"
BASE_URL="https://cdn.jsdelivr.net/gh/TACC/Core-CMS@${VERSION}"
CREATE_VAR_FILES=false

# Functions
check_for_curl() {
    if ! command -v curl &> /dev/null; then
        echo -e "${NEG}Error: curl is not installed but is required for downloading remote files.${RST}"
        echo "Please install curl and try again."
        exit 1
    fi
}
download_file() {
    local url="$1"
    local output_file="$2"
    local description="$3"

    check_for_curl

    echo -e "  ${INF}Downloading ${description}...${RST}"

    if curl -sL "$url" -o "$output_file"; then
        if [ -s "$output_file" ]; then
            echo -e "  ${POS}Successfully downloaded ${description}${RST}"
            return 0
        else
            echo -e "  ${NEG}Error: Downloaded file is empty for ${description}${RST}"
            rm -f "$output_file"
            return 1
        fi
    else
        echo -e "  ${NEG}Error: Failed to download ${description} from ${url}${RST}"
        return 1
    fi
}

# Prepare for Django operations
cd "$SRC_ROOT"

# Announce start
echo -e "${POS}Setting up TACC Core CMS...${RST}"

# Check if Docker is installed and running
if ! command -v docker &> /dev/null; then
    echo -e "${NEG}Error: Docker is not installed.${RST}"
    echo "Please install Docker and try again."
    exit 1
fi
if ! docker info &> /dev/null; then
    echo -e "${NEG}Error: Docker is not running.${RST}"
    echo "Please start Docker and try again."
    exit 1
fi

# Check if containers are already running
if docker ps | grep -q "core_cms"; then
    echo -e "${WRN}Containers are already running. Stopping them first...${RST}"
    cd "$PROJECT_ROOT"
    make stop
    cd "$SRC_ROOT"
fi

# Check for required settings files (local first, then remote)
echo -e "${INF}Checking for required settings files...${RST}"

for file in settings_custom settings_local secrets; do
    settings_file="taccsite_cms/${file}.py"
    example_file="taccsite_cms/${file}.example.py"
    url="${BASE_URL}/taccsite_cms/${file}.example.py"

    if [ ! -f "$settings_file" ]; then
        if [ -f "$example_file" ]; then
            echo -e "  ${POS}Found local ${example_file}, copying to ${settings_file}${RST}"
            cp "$example_file" "$settings_file"
        else
            echo -e "  ${WRN}Local ${example_file} not found, downloading directly to ${settings_file}...${RST}"
            if ! download_file "$url" "$settings_file" "${file}.py"; then
                echo -e "${NEG}Error: Failed to download ${settings_file}${RST}"
                exit 1
            fi
        fi
    else
        echo -e "  ${INF}${settings_file} already exists${RST}"
    fi
done

# Create expected .var files if they don't exist (if enabled)
if [ "$CREATE_VAR_FILES" = true ]; then
    echo -e "${INF}Setting up .var files...${RST}"
    if [ ! -f "needs_demo.var" ]; then
        echo "false" > needs_demo.var
        echo -e "  ${POS}Created needs_demo.var${RST}"
    else
        echo -e "  ${INF}needs_demo.var already exists${RST}"
    fi
    if [ ! -f "project_name.var" ]; then
        echo "core-cms" > project_name.var
        echo -e "  ${POS}Created project_name.var${RST}"
    else
        echo -e "  ${INF}project_name.var already exists${RST}"
    fi
    if [ ! -f "docker_repo.var" ]; then
        echo "core-cms" > docker_repo.var
        echo -e "  ${POS}Created docker_repo.var${RST}"
    else
        echo -e "  ${INF}docker_repo.var already exists${RST}"
    fi
else
    echo -e "${INF}Skipping .var file creation (disabled)${RST}"
fi

# Build and start Docker containers (from project root)
echo -e "${INF}Building and starting Docker containers...${RST}"
cd "$PROJECT_ROOT"
make build
make start ARGS=--detach

# Wait for containers to be ready
echo -e "${INF}Waiting for containers to be ready...${RST}"
for i in {1..30}; do
    if docker ps | grep -q "core_cms" && docker ps | grep -q "core_cms_postgres" && docker ps | grep -q "core_cms_elasticsearch"; then
        break
    fi
    if [ $i -eq 30 ]; then
        echo -e "  ${NEG}Error: Containers failed to start.${RST}"
        exit 1
    fi
    sleep 1
done

# Wait for PostgreSQL to be ready
echo -e "${INF}Waiting for PostgreSQL to be ready...${RST}"
for i in {1..30}; do
    if docker exec core_cms_postgres pg_isready -U postgresadmin; then
        break
    fi
    if [ $i -eq 30 ]; then
        echo -e "  ${NEG}Error: PostgreSQL failed to start.${RST}"
        exit 1
    fi
    sleep 1
done

# Wait for Elasticsearch to be ready
echo -e "${INF}Waiting for Elasticsearch to be ready...${RST}"
for i in {1..30}; do
    if curl -s http://localhost:9201/_cluster/health | grep -q '"status":"green"\|"status":"yellow"'; then
        break
    fi
    if [ $i -eq 30 ]; then
        echo -e "  ${NEG}Error: Elasticsearch failed to start.${RST}"
        exit 1
    fi
    sleep 1
done

# Run Django setup commands
echo -e "${INF}Setting up Django...${RST}"
docker exec -it core_cms sh -c "python manage.py migrate"

# Check whether to let user create superuser
echo -e "${INF}Checking for existing superuser...${RST}"

# Define how to check for superuser
HAS_SUPERUSER_CMD="python manage.py shell -c \"from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())\""
HAS_SUPERUSER=$(docker exec core_cms sh -c "$HAS_SUPERUSER_CMD")

# Check for / Create a superuser
if [ "$HAS_SUPERUSER" != "True" ]; then
    echo -e "${INF}No superuser found. Letting you create one...${RST}"
    docker exec -it core_cms sh -c "python manage.py createsuperuser"
else
    echo -e "${INF}Superuser already exists. Skipping creation.${RST}"
fi

# Collect static files
echo -e "${INF}Preparing static files...${RST}"
docker exec -it core_cms sh -c "python manage.py collectstatic --no-input"

# Announce end
echo -e "${POS}
${IMP}Setup complete! You can now:${RST}${POS}
1. Open http://localhost:8000/ in your browser.
2. Log in with the credentials you just created.
3. Create your first CMS page (this will be your homepage).

To stop the CMS, run:
  ${INF}make stop${POS}

To start it again, run:
  ${INF}make start${RST}
${RST}"
