## What changed

Describe the bundle, fix, or documentation change.

## Bundle checklist

- [ ] `config.yaml` follows the current Bundle DSL
- [ ] Referenced Ansible playbooks are included
- [ ] `README.md` documents requirements, installation, actions, and limitations
- [ ] `LICENSE` is included
- [ ] `bash scripts/build-bundles.sh` succeeds
- [ ] The generated `.tgz` uploads to ADCM
- [ ] Install and operational actions were tested in a suitable environment
- [ ] No credentials, tokens, private data, or generated secrets are committed or logged
- [ ] External downloads use HTTPS, fixed versions, and integrity verification where possible
- [ ] Shell/Ansible commands do not interpolate untrusted values into command strings
- [ ] Sensitive Ansible tasks use `no_log: true`
- [ ] The bundle contains no symlinks or paths escaping its own directory

## Test environment

ADCM version, target OS, topology, and actions tested:

## Known limitations

List anything maintainers and users should know before merging.
