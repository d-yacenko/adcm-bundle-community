# Keycloak Bundle for ADCM

## Description

This bundle installs **Keycloak 26.0.8** and, optionally, **PostgreSQL** on ADCM
cluster hosts.

The bundle provides two services:

| Service | Component | Requirement |
|---|---|---|
| `keycloak` | `keycloak_server` | Required, one or more hosts |
| `postgres` | `postgresql` | Optional, zero or one host |

Keycloak can be installed on multiple hosts. All Keycloak instances are
configured to use the same PostgreSQL database.

## Requirements

- ADCM version: **2.11.0 or newer**
- Bundle contract version: **2.1**
- Ansible venv: **2.16**
- Linux with systemd: Debian/Ubuntu or RHEL-compatible distributions
- Java 17: installed automatically as `openjdk-17-jre-headless` or
  `java-17-openjdk-headless`
- PostgreSQL **12 or newer** for the bundled database
- Outbound HTTPS access to GitHub Releases for the Keycloak 26.0.8 distribution,
  or a preconfigured mirror in the playbook; the archive is verified against a
  pinned SHA-256 checksum
- TCP ports open between cluster hosts:
  - `keycloak_http_port` (default `8080`)
  - `database_port` (default `5432`)

The bundle uses `ansible.builtin` modules and the ADCM-provided `adcm_config`
action plugin, so no additional Ansible collections are required.

## Installation

1. Upload the release archive to ADCM:

   ```text
   dist/adcm-keycloak-26.0.8-1.0.0.tgz
   ```

2. Create a cluster from the `keycloak` prototype.
3. Make sure the required `keycloak` service is present in the cluster.
4. Add the `postgres` service if the bundle should install PostgreSQL.
5. Add hosts to the cluster and map the components:
   - `keycloak_server` — one or more hosts;
   - `postgresql` — one host, if the internal database is used.
6. Fill in the required `database_password` in the cluster configuration and
   `keycloak_admin_password` in the `keycloak` service configuration.
7. Run **Install**. The action creates two ADCM jobs:
   - `Install PostgreSQL`;
   - `Install Keycloak`.
8. After a successful installation, the cluster state becomes `installed`.
   Use **Add Keycloak server** to add more Keycloak hosts later.

The Keycloak administrator console is available at:

```text
http://<IP>:<keycloak_http_port>/admin
```

## Configuration

### Cluster configuration

| Parameter | Default | Description |
|---|---|---|
| `database_mode` | `internal` | `internal` or `external` |
| `database_host` | empty | External PostgreSQL host; required for `external` |
| `database_port` | `5432` | PostgreSQL port |
| `database_name` | `keycloak` | Database name |
| `database_user` | `keycloak` | Database user |
| `database_password` | **required** | Database user password |
| `database_ssl_mode` | `prefer` | JDBC `sslmode` |

`internal` mode installs PostgreSQL on the host where `postgresql` is mapped and
creates the database and role automatically. `external` mode uses an existing
PostgreSQL server.

### Keycloak service configuration

| Parameter | Default | Description |
|---|---|---|
| `keycloak_http_port` | `8080` | Keycloak HTTP port |
| `keycloak_management_port` | `9000` | Health and metrics port |
| `keycloak_hostname` | empty | Optional public URL, for example `https://keycloak.example.com` |
| `keycloak_admin_user` | `admin` | Bootstrap administrator username |
| `keycloak_admin_password` | **required** | Bootstrap administrator password |
| `keycloak_java_opts` | `-Xms512m -Xmx1024m` | JVM options |
| `keycloak_log_level` | `INFO` | Keycloak log level |

The Keycloak version is fixed at **26.0.8** for this bundle version and is not
configurable.

`keycloak_admin_password` is mandatory and has no default. It is applied only
when the first Keycloak instance initializes an empty database. Changing the
parameter after installation does not change the password of an existing
administrator; use the Keycloak admin console to change it.

### PostgreSQL service configuration

| Parameter | Default | Description |
|---|---|---|
| `postgres_max_connections` | `200` | PostgreSQL `max_connections` |
| `postgres_shared_buffers` | `256MB` | PostgreSQL `shared_buffers` |
| `postgres_effective_cache_size` | `1GB` | PostgreSQL `effective_cache_size` |

## Actions

### Install

Available in the `created` state. Two ADCM jobs run sequentially:

1. `Install PostgreSQL` — installs and configures PostgreSQL if `postgresql` is
   mapped.
2. `Install Keycloak` — installs Keycloak on every mapped `keycloak_server` host,
   configures the database connection, starts Keycloak with systemd, and checks
   `/health/ready`.

Keycloak installation uses `serial: 1`: the first node creates the database
schema, and the following nodes connect to the initialized database.

### Add Keycloak server

Available in the `installed` state. Installs Keycloak on the selected hosts and
connects the new instances to the same database.

## Known Issues and Limitations

- Keycloak nodes run as standalone instances with `cache=local` and share one
  database. A load balancer with sticky sessions is required in front of
  multiple nodes. Full session replication requires an external Infinispan or a
  custom cache stack.
- TLS is not configured by the bundle. Use a reverse proxy with HTTPS for
  production and set `keycloak_hostname`.
- In `internal` mode, `pg_hba.conf` allows password authentication from any
  address. Restrict access with a firewall or adjust the template for specific
  subnets.
- The bootstrap administrator is created only during the first database
  initialization. Changing `keycloak_admin_password` after installation does not
  update an existing administrator.
- There are no default passwords. Both `keycloak_admin_password` and
  `database_password` must be set before installation.
- The first installation downloads OpenJDK and the Keycloak distribution
  (about 150 MB). Prerequisite packages are installed in parallel on all
  Keycloak hosts, and the APT cache is refreshed only when Java 17 is missing.
  Use a local package mirror for faster and more predictable installations.

## Versioning

- Bundle version: `26.0.8-1.0.0`
- Keycloak version: `26.0.8`
- Display name: `Keycloak`
- Prototype name: `keycloak`

The community build produces `dist/adcm-keycloak-26.0.8-1.0.0.tgz`.

## License

Apache License 2.0. See [LICENSE](LICENSE).
