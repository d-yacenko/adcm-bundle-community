#!/usr/bin/env python3
"""Validate the minimum repository contract for every community bundle."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterator

import yaml


ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "bundles"


def mappings(value: Any) -> Iterator[dict]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from mappings(child)
    elif isinstance(value, list):
        for child in value:
            yield from mappings(child)


def validate_bundle(bundle_dir: Path) -> list[str]:
    errors: list[str] = []
    config_path = bundle_dir / "config.yaml"
    if not config_path.is_file():
        return [f"{bundle_dir.name}: config.yaml is missing"]

    try:
        documents = list(yaml.safe_load_all(config_path.read_text(encoding="utf-8")))
    except yaml.YAMLError as error:
        return [f"{bundle_dir.name}: invalid config.yaml: {error}"]

    objects = [item for document in documents if document for item in document]
    clusters = [item for item in objects if isinstance(item, dict) and item.get("type") == "cluster"]
    if len(clusters) != 1:
        errors.append(f"{bundle_dir.name}: expected exactly one cluster prototype")
    else:
        for field in ("name", "version", "adcm_min_version"):
            if clusters[0].get(field) in (None, ""):
                errors.append(f"{bundle_dir.name}: cluster field '{field}' is required")

    if not any((bundle_dir / name).is_file() for name in ("README.md", "readme.md")):
        errors.append(f"{bundle_dir.name}: README.md is missing")
    if not (bundle_dir / "LICENSE").is_file():
        errors.append(f"{bundle_dir.name}: LICENSE is missing")

    for item in mappings(objects):
        script = item.get("script")
        if isinstance(script, str) and not (bundle_dir / script).is_file():
            errors.append(f"{bundle_dir.name}: referenced script does not exist: {script}")

    for yaml_path in sorted(bundle_dir.rglob("*.yml")) + sorted(bundle_dir.rglob("*.yaml")):
        try:
            list(yaml.safe_load_all(yaml_path.read_text(encoding="utf-8")))
        except yaml.YAMLError as error:
            errors.append(f"{bundle_dir.name}: invalid YAML in {yaml_path.relative_to(bundle_dir)}: {error}")

    return errors


def main() -> None:
    errors = [error for bundle in sorted(BUNDLES.iterdir()) if bundle.is_dir() for error in validate_bundle(bundle)]
    if errors:
        raise SystemExit("Bundle validation failed:\n- " + "\n- ".join(errors))
    print(f"Validated {sum(path.is_dir() for path in BUNDLES.iterdir())} bundles")


if __name__ == "__main__":
    main()
