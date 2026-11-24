FROM python:3.12-slim AS python-base
LABEL maintainer="TACC-ACI-WMA <wma_prtl@tacc.utexas.edu>"
ARG DEBIAN_FRONTEND=noninteractive

# Ensure that system pip is not using compromised certifi bundle [https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576]
RUN python -m pip install "pip @ https://files.pythonhosted.org/packages/3f/06/3e4420302363fbb71be3c7f35ce042f54bfca330e3e66b3a2e3c4cca579f/pip-26.2.2-py3-none-any.whl#sha256=fd7f4dfa8190e014013b9f08f3e973f4e4c26ffd179a204895533a7254813a70"

RUN apt-get update && apt-get install -y git gcc build-essential libmagic-dev ldap-utils libldap2-dev libsasl2-dev
EXPOSE 8000

COPY --from=ghcr.io/astral-sh/uv:0.13.5 /uv /uvx /bin/
ENV PYSETUP_PATH="/opt/pysetup"
ENV PATH="$PYSETUP_PATH/.venv/bin:$PATH"

WORKDIR $PYSETUP_PATH
COPY pyproject.toml uv.lock ./
# install runtime deps
RUN --mount=type=cache,id=uv-cms-prod,target=/uv/sync-prod uv sync --locked --no-dev


FROM python-base AS development
COPY . /code/
WORKDIR /code
RUN --mount=type=cache,id=uv-core-cms-dev,target=/uv/sync-dev uv sync --locked --dev


FROM ghcr.io/pnpm/pnpm:12 AS node_build
RUN pnpm runtime set node 24 -g
COPY package.json pnpm-lock.yaml /code/
WORKDIR /code
RUN --mount=type=cache,id=pnpm-core-cms,target=/pnpm/store \
    pnpm install --frozen-lockfile

# Build assets
COPY . /code/
ARG BUILD_ID
RUN pnpm run build


# FINAL LAYER
FROM python-base AS production

# Support CMS logs
RUN mkdir -p /var/log/cms

# Populate with code from Node layer
# - (new) /node_modules
# - (unchanged) /package.json and /pnpm-lock.yaml
# - (populated) /css/build and /taccsite_ui/dist
COPY --from=node_build /code/ /code
WORKDIR /code
