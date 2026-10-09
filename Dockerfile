FROM python:3.12-slim AS python-base
LABEL maintainer="TACC-ACI-WMA <wma_prtl@tacc.utexas.edu>"
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y git gcc build-essential libmagic-dev ldap-utils libldap2-dev libsasl2-dev
EXPOSE 8000

COPY --from=ghcr.io/astral-sh/uv:0.12.15 /uv /uvx /bin/
ENV PYSETUP_PATH="/opt/pysetup"
ENV PATH="$PYSETUP_PATH/.venv/bin:$PATH"

WORKDIR $PYSETUP_PATH
COPY pyproject.toml uv.lock ./
# install runtime deps
RUN --mount=type=cache,id=uv-cms-prod,target=/uv/sync-prod uv sync --locked --no-dev



# POETRY DEPENDENCIES
FROM python-base AS development
COPY . /code/
WORKDIR /code


FROM ghcr.io/pnpm/pnpm:12 AS node_build
RUN pnpm runtime set node 24 -g
COPY package.json pnpm-lock.yaml /code/
WORKDIR /code
RUN --mount=type=cache,id=pnpm-core-cms,target=/pnpm/store \
    pnpm install --frozen-lockfile

# Build assets
COPY . /code/
ARG BUILD_ID
RUN echo ${BUILD_ID}
RUN pnpm run build


# FINAL LAYER
FROM python-base AS production

# Support CMS logs
RUN mkdir -p /var/log/cms

# Populate with code from Node layer
# - (new) /node_modules
# - (unchanged) /package.json and /package-lock.json
# - (populated) /css/build and /taccsite_ui/dist
COPY --from=node_build /code/ /code
WORKDIR /code
