#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUNDLES_DIR="${ROOT_DIR}/bundles"
DIST_DIR="${ROOT_DIR}/dist"

if [[ ! -d "${BUNDLES_DIR}" ]]; then
  echo "ERROR: bundles directory not found: ${BUNDLES_DIR}" >&2
  exit 1
fi

rm -rf "${DIST_DIR}"
mkdir -p "${DIST_DIR}"

build_one_bundle() {
  local bundle_dir="$1"
  local bundle_name
  local config_file
  local version
  local output_file

  bundle_name="$(basename "${bundle_dir}")"
  config_file="${bundle_dir}/config.yaml"

  if [[ ! "${bundle_name}" =~ ^[a-z0-9][a-z0-9._-]{0,63}$ ]]; then
    echo "ERROR: unsafe bundle directory name: ${bundle_name}" >&2
    exit 1
  fi

  if [[ ! -f "${config_file}" ]]; then
    echo "ERROR: config.yaml not found for bundle '${bundle_name}'" >&2
    exit 1
  fi

  version="$(
    awk '
      $1 == "-" && $2 == "type:" && $3 == "cluster" { in_cluster = 1; next }
      in_cluster && $1 == "version:" {
        gsub(/"/, "", $NF)
        print $NF
        exit
      }
    ' "${config_file}" || true
  )"

  if [[ -z "${version}" ]]; then
    version="$(
      awk '
        $1 == "version:" {
          gsub(/"/, "", $NF)
          print $NF
          exit
        }
      ' "${config_file}" || true
    )"
  fi

  if [[ -z "${version}" ]]; then
    echo "ERROR: cannot determine version from ${config_file}" >&2
    exit 1
  fi

  if [[ ! "${version}" =~ ^[0-9A-Za-z][0-9A-Za-z._+-]{0,63}$ ]]; then
    echo "ERROR: unsafe bundle version in ${config_file}: ${version}" >&2
    exit 1
  fi

  output_file="adcm-${bundle_name}-${version}.tgz"

  echo "Building ${output_file}"
  tar \
    --sort=name \
    --mtime='UTC 1970-01-01' \
    --owner=0 \
    --group=0 \
    --numeric-owner \
    -czf "${DIST_DIR}/${output_file}" \
    -C "${bundle_dir}" \
    .
}

for dir in "${BUNDLES_DIR}"/*; do
  [[ -d "${dir}" ]] || continue
  build_one_bundle "${dir}"
done

(
  cd "${DIST_DIR}"
  sha256sum ./*.tgz > SHA256SUMS
)

python3 "${ROOT_DIR}/scripts/build-catalog.py" \
  --bundles-dir "${BUNDLES_DIR}" \
  --dist-dir "${DIST_DIR}"

echo
echo "Artifacts:"
ls -lh "${DIST_DIR}"/*.tgz "${DIST_DIR}"/SHA256SUMS "${DIST_DIR}"/catalog.json
