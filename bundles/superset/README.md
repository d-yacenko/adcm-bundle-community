# Apache Superset bundle

Community ADCM bundle for deploying Apache Superset 4.1.1 on Ubuntu 22.04.

## What it installs

- Apache Superset from the official upstream tag;
- Docker Engine and Docker Compose;
- PostgreSQL and Redis containers used by Superset;
- a systemd unit for managing the Compose deployment.

## Requirements

- ADCM 2.6.0 or newer;
- Ubuntu 22.04 target host;
- outbound access to GitHub, Docker repositories, and the Superset image registry;
- TCP port 8088 available for the web interface.

## Installation

1. Upload `adcm-superset-1.0.1.tgz` to ADCM.
2. Create a Superset cluster and add the Superset service.
3. Assign the `WEB` component to a host.
4. Set a strong administrator password in the service configuration.
5. Run the `Install` action.

After installation, open `http://<host>:8088` and sign in as `admin` with the configured password.

## Actions

- `Install` — install Docker and deploy Superset;
- `Configure` — update the deployment configuration;
- `Start`, `Stop`, `Restart` — control the systemd service;
- `Check` — verify service availability;
- `Uninstall` — remove the deployment.

## License

The bundle source code is licensed under Apache License 2.0. Apache Superset and its dependencies retain their respective upstream licenses.
