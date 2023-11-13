#!/bin/bash

# Annotate a tag from Github
# FAQ: Github releases create annotated (not lightweight) tags
# SEE: https://github.com/orgs/community/discussions/4924

# Whether string is a valid SemVer version
is_valid_semver() {
  local version=$1
  # SemVer regex pattern (simplified for illustration)
  local semver_pattern="^v[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?$"
  [[ $version =~ $semver_pattern ]]
}

# Is argument (string) provided?
if [ $# -ne 1 ]; then
  echo "Usage: $0 <version_string>"
  exit 1
fi

# Capture arguments
version_string=$1

# Is string a valid SemVer version?
if ! is_valid_semver "$version_string"; then
  echo "Error: Invalid SemVer format. Please provide a valid version string like '3.11.6' or 'v3.12.0-beta.3' or 'v3.6.0-8-gd1dbcab'."
  exit 1
fi

# Annotate the tag
git pull
git checkout "$version_string"
git tag -d "$version_string"
git tag -a "$version_string" -m "chore: $version_string"

# Report success
echo "Annotated tag \"$version_string\"."
