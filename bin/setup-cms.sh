#!/bin/bash

# Exit on error
set -e

# Colors for output
POS='\033[0;32m' # positive
NEG='\033[0;31m' # negative
WRN='\033[1;33m' # warning
INF='\033[0;36m' # info
RST='\033[0m'    # reset

# Define root path
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

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
    make stop
fi

# Check for required example files
echo -e "${INF}Checking for required files...${RST}"
for file in settings_custom settings_local secrets; do
    if [ ! -f "taccsite_cms/${file}.example.py" ]; then
        echo -e "${NEG}Error: taccsite_cms/${file}.example.py not found.${RST}"
        exit 1
    fi
done

# Create expected .var files if they don't exist
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

# Copy required settings files if they don't exist
echo -e "${INF}Setting up configuration files...${RST}"
for file in settings_custom settings_local secrets; do
    if [ ! -f "taccsite_cms/${file}.py" ]; then
        cp "taccsite_cms/${file}.example.py" "taccsite_cms/${file}.py"
        echo -e "  ${POS}Created taccsite_cms/${file}.py${RST}"
    else
        echo -e "  ${INF}taccsite_cms/${file}.py already exists${RST}"
    fi
done

# Build and start Docker containers
echo -e "${INF}Building and starting Docker containers...${RST}"
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

# Try interactive superuser creation first
echo -e "${INF}Creating superuser account...${RST}"
if ! docker exec -it core_cms sh -c "python manage.py createsuperuser"; then
    echo -e "${WRN}Interactive superuser creation failed, falling back to non-interactive method...${RST}"
    echo "Please enter the following information for your superuser account:"
    read -p "Username (default: admin): " username
    username=${username:-admin}
    read -p "Email (optional): " email
    read -s -p "Password: " password
    echo
    read -s -p "Password (again): " password2
    echo

    if [ "$password" != "$password2" ]; then
        echo -e "${NEG}Error: Passwords do not match.${RST}"
        exit 1
    fi

    # Create superuser non-interactively
    docker exec -it core_cms sh -c "python manage.py shell -c \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$username', '$email', '$password')\""
fi

# Collect static files
echo -e "${INF}Preparing static files...${RST}"
docker exec -it core_cms sh -c "python manage.py collectstatic --no-input"

echo -e "${POS}
Setup complete! You can now:
1. Open http://localhost:8000/ in your browser.
2. Log in with the credentials you just created.
3. Create your first CMS page (this will be your homepage).

To stop the CMS, run:
  ${INF}make stop${RST}

To start it again, run:
  ${INF}make start${RST}
${RST}"
