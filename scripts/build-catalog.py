#!/usr/bin/env python3
"""Build a machine-readable catalog for the landing page and API consumers."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import yaml


DEFAULT_REPOSITORY = "d-yacenko/adcm-bundle-community"


def cluster_prototype(config_path: Path) -> dict:
    documents = list(yaml.safe_load_all(config_path.read_text(encoding="utf-8")))
    objects = [item for document in documents if document for item in document]
    for item in objects:
        if isinstance(item, dict) and item.get("type") == "cluster":
            return item
    raise ValueError(f"cluster prototype not found in {config_path}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundles-dir", type=Path, required=True)
    parser.add_argument("--dist-dir", type=Path, required=True)
    args = parser.parse_args()

    repository = os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPOSITORY)
    catalog = []

    for bundle_dir in sorted(path for path in args.bundles_dir.iterdir() if path.is_dir()):
        prototype = cluster_prototype(bundle_dir / "config.yaml")
        version = str(prototype["version"])
        asset = f"adcm-{bundle_dir.name}-{version}.tgz"
        asset_path = args.dist_dir / asset
        if not asset_path.is_file():
            raise FileNotFoundError(f"release asset was not built: {asset_path}")

        catalog.append(
            {
                "slug": bundle_dir.name,
                "name": prototype.get("display_name") or prototype.get("name") or bundle_dir.name,
                "version": version,
                "adcm_min_version": str(prototype.get("adcm_min_version", "")),
                "asset": asset,
                "sha256": sha256(asset_path),
                "source_url": f"https://github.com/{repository}/tree/main/bundles/{bundle_dir.name}",
                "download_url": f"https://github.com/{repository}/releases/latest/download/{asset}",
            }
        )

    output = {
        "repository": repository,
        "release_url": f"https://github.com/{repository}/releases/latest",
        "bundles": catalog,
    }
    (args.dist_dir / "catalog.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
