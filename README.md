# ADCM Bundle Community

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fadcm-bundle.duckdns.org)](https://adcm-bundle.duckdns.org)
[![Validate bundles](https://github.com/d-yacenko/adcm-bundle-community/actions/workflows/ci.yml/badge.svg)](https://github.com/d-yacenko/adcm-bundle-community/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

Открытый каталог бандлов для Arenadata Cluster Manager. Исходники проходят review через обычный GitHub fork/PR flow, а готовые архивы публикуются в GitHub Releases.

- Сайт: [adcm-bundle.duckdns.org](https://adcm-bundle.duckdns.org)
- Готовые архивы: [Latest Release](https://github.com/d-yacenko/adcm-bundle-community/releases/latest)
- Правила участия: [CONTRIBUTING.md](CONTRIBUTING.md)

## Бандлы

| Бандл | Версия | ADCM | Исходники | Скачать |
|---|---:|---:|---|---|
| Bacula | 15.0.3_63 | >= 2.12.0 | [bundles/bacula](bundles/bacula) | [`.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-bacula-15.0.3_63.tgz) |
| JupyterHub | 1.86p3 | >= 2.6.0 | [bundles/jupyterhub](bundles/jupyterhub) | [`.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-jupyterhub-1.86p3.tgz) |
| Apache Superset | 1.0.1 | >= 2.6.0 | [bundles/superset](bundles/superset) | [`.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-superset-1.0.1.tgz) |
| pgAdmin 4 | 1.0.5 | >= 2.6.0 | [bundles/pgadmin4-web](bundles/pgadmin4-web) | [`.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-pgadmin4-web-1.0.5.tgz) |
| WebSSH | 1.0.6 | >= 2.6.0 | [bundles/webssh](bundles/webssh) | [`.tgz`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/adcm-webssh-1.0.6.tgz) |

Проверить целостность загрузки можно по [`SHA256SUMS`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/SHA256SUMS). Машиночитаемый каталог доступен в [`catalog.json`](https://github.com/d-yacenko/adcm-bundle-community/releases/latest/download/catalog.json).

## Использование готового бандла

1. Скачайте нужный `adcm-*.tgz` из таблицы или со страницы Releases.
2. Откройте `Bundles` в ADCM.
3. Нажмите `Upload bundle` и выберите архив.
4. Создайте объект, настройте host-component mapping и запустите actions.

## Локальная сборка

```bash
git clone https://github.com/d-yacenko/adcm-bundle-community.git
cd adcm-bundle-community
python3 -m pip install -r requirements-dev.txt
bash scripts/build-bundles.sh
ls -lh dist/
```

`dist/` генерируется локально и не хранится в Git. Публикуемые `.tgz`, `SHA256SUMS` и `catalog.json` прикрепляются к GitHub Release.

## Как добавить бандл

1. Сделайте fork репозитория.
2. Создайте каталог `bundles/<bundle-name>/`.
3. Добавьте `config.yaml`, Ansible playbooks, `README.md` и `LICENSE`.
4. Выполните локальную проверку и загрузите собранный архив в тестовый ADCM.
5. Откройте Pull Request и заполните чеклист.

Подробности находятся в [CONTRIBUTING.md](CONTRIBUTING.md). Минимальный пример — в [examples/simple-bundle](examples/simple-bundle).

## Автоматизация

- каждый PR проверяется workflow `Validate bundles`;
- сборка всех архивов должна успешно завершиться до merge;
- push тега `v*` создаёт GitHub Release со всеми актуальными бандлами;
- ветка `main` является источником истины для исходников каталога.

## Полезные ссылки

- [Bundle DSL](https://docs.arenadata.io/ru/ADCM/current/references/bundle-dsl.html)
- [Создание простого бандла](https://docs.arenadata.io/ru/ADCM/current/how-to/simple-bundle.html)
- [ADCM](https://github.com/arenadata/adcm)
- [Руководство по релизам](RELEASING.md)

## Лицензия

Код репозитория распространяется по Apache License 2.0. Сторонние продукты и зависимости сохраняют собственные лицензии.
