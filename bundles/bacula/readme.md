# Bacula Bundle for ADCM

## Description

**Bacula** is a cross-platform enterprise‑grade backup and recovery system. This bundle for **ADCM (Arenadata Cluster Manager)** automates the deployment of a distributed Bacula cluster, including all key components:

- **PostgreSQL** – catalog (metadata database);
- **Director** – central management component;
- **Storage** – storage daemon (volume management);
- **Client** – File Daemon (agent installed on hosts to be backed up).

With this bundle you can:

- Deploy a full Bacula cluster in just a few clicks;
- Dynamically add and remove clients and storage hosts;
- Create, run, disable, enable, cancel, and delete backup jobs;
- View job status, list clients, storage, and backup history;
- Configure each component via the ADCM web interface.

---

## Requirements

- **ADCM** version **>= 2.12.0**.
- **Target host OS**: **Ubuntu 22.04** (other distributions may work, but only Ubuntu 22.04 is officially supported).
- **Network**: open ports between components:
  - Director: 9101 (for bconsole and API).
  - Storage: 9103.
  - Client: 9102.
  - PostgreSQL: 5432 (if remote connection is used).

---

## Installation

1. **Upload the bundle** to ADCM via the UI or API.
2. **Create a cluster** of type `Bacula`.
3. **Add hosts** to the cluster (at least 4 hosts for a full distributed setup, but fewer can be used if components are co‑located).
4. **Configure host‑component mapping**:
   - Assign the `postgresql` component to the host for the database.
   - Assign the `director` component to the host for the Director.
   - Assign the `storage` component to the host(s) for Storage (multiple hosts allowed).
   - Assign the `client` component to the hosts that will be backed up.
5. **Run the `Install` action** on the cluster. During installation you will be prompted for parameters: backup job name, level, Storage host, schedule, and message profile. After completion, the Director automatically registers all added clients and storage hosts, and creates a backup job for each client linked to the selected Storage.

---

## Configuration

Configuration is split across services. Each service has its own parameters, configurable via ADCM.

### Service `postgresql`

| Parameter | Description | Type | Required |
|-----------|-------------|------|----------|
| `Username` | Database username for the catalog | string | Yes |
| `Password` | Database user password | password | Yes |
| `Database name` | Catalog database name | string | Yes |

### Service `director`

| Parameter | Description | Type | Required |
|-----------|-------------|------|----------|
| `Port number` | Director port (default 9101) | integer | Yes |
| `Working Directory` | Director working directory | string | Yes |
| `Pid Directory` | PID file directory | string | Yes |
| `Maximum Concurrent Jobs` | Maximum number of concurrent backup jobs | integer | Yes |
| `Director password` | Director authentication password | password | Yes |

### Service `Storage`

| Parameter | Description | Type | Required |
|-----------|-------------|------|----------|
| `Volumes directory` | Device map: key – device name, value – filesystem path for backup volumes (supports group customisation) | map | Yes |


### Service `Client`

| Parameter | Description | Type | Required |
|-----------|-------------|------|----------|
| `Paths` | List of directories to back up (supports group customisation) | list | Yes |


**Group customisation**: The `devices` (Storage) and `Paths` (Client) parameters support group‑level customisation, allowing different values per host within the same service.

---

## Actions

### Cluster‑level Actions

| Action | Description |
|--------|-------------|
| **Install** | Sequential installation: PostgreSQL → Client → Storage → Director. Director registers all existing clients and storage. During installation you specify parameters for the first backup job (name, level, Storage host, schedule, message profile). A separate job is created for each client. |
| **Job Status** | Display detailed job information by ID: status, files, bytes, volumes, errors. |
| **Run Job** | Manually run a backup job (by job name). |
| **Disable Job** | Disable a job – it remains in config but won't run on schedule (can still be started manually via bconsole). |
| **Enable Job** | Re‑enable a previously disabled job – it will resume scheduled runs. |
| **Restore Job** | Restore files from a backup job to a specified client and path. |
| **Cancel job** | Cancel a currently running backup job. |
| **Delete job** | Permanently delete job records from the catalog (irreversible). |
| **List Jobs** | Show all job categories: running, scheduled, terminated, disabled, full history. Optional filter by job name. |
| **List Storage** | Display storage daemons with their volumes and disk usage. |
| **List Clients** | Display clients with their backup paths. |
| **Add client** | Install File Daemon on selected hosts and register them in Director. |
| **Remove client** | Uninstall File Daemon and remove all related configurations, jobs, and schedules from Director. |
| **Add Storage** | Install Storage Daemon on selected hosts and register it in Director. |
| **Remove Storage** | Uninstall Storage Daemon and remove all related configurations, jobs, and schedules from Director. |
| **Create Backup Job** | Create a new backup job with schedule, linking a client fileset to a storage destination. |

### Service‑level Actions

#### Service `Storage`
| Action | Description |
|--------|-------------|
| **Reconfig** | Synchronise storage device configurations to Director, creating or updating Storage and Device blocks for all hosts in the service. Use after changing the `devices` parameter in Storage configuration. |

#### Service `Client`
| Action | Description |
|--------|-------------|
| **Reconfig** | Synchronise fileset configurations to Director, creating or updating FileSet blocks with backup paths for all hosts in the service. Use after changing the `Paths` parameter in Client configuration. |

#### Service `Director`
| Action | Description |
|--------|-------------|
| **Status** | Display the current status of the Director daemon, including running jobs, scheduled jobs, terminated jobs, and device status. |


---

## License

Bacula Community Edition is licensed under the **GNU Affero General Public License, version 3.0 (AGPLv3)**.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.