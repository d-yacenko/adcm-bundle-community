# JupyterHub bundle

ADCM bundle for deploying a multi-user JupyterHub and JupyterLab environment on Ubuntu 22.04.

## Features

- PAM authentication and systemd service management;
- JupyterLab with a Python environment;
- optional language kernels managed through ADCM actions;
- package, extension, start, stop, restart, check, and uninstall actions.

## Requirements

- ADCM 2.6.0 or newer;
- Ubuntu 22.04 target host;
- outbound package repository access.

## Installation

1. Upload `adcm-jupyterhub-1.86p3.tgz` to ADCM.
2. Create a cluster and add the JupyterHub service.
3. Assign its component to a target host.
4. Review the service configuration and run `Install`.

Additional kernels can be installed with the corresponding service actions after the base installation succeeds.

## License

See `LICENSE` and the notices included with the bundle. Third-party runtimes and kernels retain their upstream licenses.
