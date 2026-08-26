# WebSSH bundle

ADCM bundle for deploying WebSSH as a managed systemd service on Ubuntu 22.04.

## Features

- Python virtual environment installation;
- systemd service configuration;
- configure, start, stop, restart, check, and uninstall actions.

## Requirements

- ADCM 2.6.0 or newer;
- Ubuntu 22.04 target host;
- network access to the managed SSH endpoints.

## Installation

1. Upload `adcm-webssh-1.0.7.tgz` to ADCM.
2. Create a cluster and add the WebSSH service.
3. Assign its component to a target host.
4. Configure the listening address and run `Install`.

## Security

- WebSSH runs as an unprivileged system user with systemd sandboxing.
- The default listen address is `0.0.0.0`; restrict it with firewall rules or a reverse proxy.
- Publish the service through an HTTPS reverse proxy with authentication and network access controls.
- Enter SSH credentials interactively, or use URL-prefill inside a trusted internal network. Never expose such URLs publicly.
- Version `1.0.7` pins the upstream Python package to WebSSH `1.6.3`.

## License

See `LICENSE` and the notices included with the bundle. WebSSH and its dependencies retain their upstream licenses.
