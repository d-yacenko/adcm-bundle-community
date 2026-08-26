# Каталог ADCM-бандлов

Исходники находятся в `bundles/*`. Готовые архивы публикуются как assets в [последнем GitHub Release](https://github.com/d-yacenko/adcm-bundle-community/releases/latest).

| Бандл | Версия | ADCM | Архив |
|---|---:|---:|---|
| Bacula | 15.0.3_63 | >= 2.12.0 | [`adcm-bacula-15.0.3_63.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-bacula-15.0.3_63.tgz) |
| JupyterHub | 1.86p3 | >= 2.6.0 | [`adcm-jupyterhub-1.86p3.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-jupyterhub-1.86p3.tgz) |
| Apache Superset | 1.0.1 | >= 2.6.0 | [`adcm-superset-1.0.1.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-superset-1.0.1.tgz) |
| pgAdmin 4 | 1.0.5 | >= 2.6.0 | [`adcm-pgadmin4-web-1.0.5.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-pgadmin4-web-1.0.5.tgz) |
| WebSSH | 1.0.6 | >= 2.6.0 | [`adcm-webssh-1.0.6.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-webssh-1.0.6.tgz) |

## Проверка целостности

```bash
curl -LO https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/SHA256SUMS
sha256sum --check SHA256SUMS
```

## Локальная сборка

```bash
python3 -m pip install -r requirements-dev.txt
bash scripts/build-bundles.sh
ls -lh dist/
```

## Загрузка в ADCM

Откройте `Bundles` в ADCM, нажмите `Upload bundle` и передайте нужный `.tgz`. Исходный код всего репозитория, который GitHub предлагает как `Source code`, не является отдельным ADCM-бандлом.
