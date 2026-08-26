# Доступные ADCM бандлы

В репозитории исходники бандлов лежат в `bundles/*`.
Готовые архивы `*.tgz` доступны в GitHub Releases:
- `https://github.com/d-yacenko/adcm-bundle-community/releases/latest`

## 1. JupyterHub (v1.86p3)

- Исходники: `bundles/jupyterhub`
- Релизный файл: `adcm-jupyterhub-1.86p3.tgz`
- Описание: многопользовательская среда JupyterHub/JupyterLab с PAM auth
- ADCM: `>= 2.6.0`
- Документация: https://adcm-bundle.duckdns.org/bundles/jupyterhub.html

## 2. Apache Superset (v1.0.1)

- Исходники: `bundles/superset`
- Релизный файл: `adcm-superset-1.0.1.tgz`
- Описание: Apache Superset 4.1.1 через официальные Docker-образы и Docker Compose
- ADCM: `>= 2.6.0`
- Документация: https://adcm-bundle.duckdns.org/bundles/superset.html

## 3. pgAdmin 4 (v1.0.5)

- Исходники: `bundles/pgadmin4-web`
- Релизный файл: `adcm-pgadmin4-web-1.0.5.tgz`
- Описание: web-интерфейс администрирования PostgreSQL через Apache WSGI
- ADCM: `>= 2.6.0`
- Документация: https://adcm-bundle.duckdns.org/bundles/pgadmin4.html

## 4. WebSSH (v1.0.7)

- Исходники: `bundles/webssh`
- Релизный файл: `adcm-webssh-1.0.7.tgz`
- Описание: web-терминал SSH через браузер
- ADCM: `>= 2.6.0`
- Документация: https://adcm-bundle.duckdns.org/bundles/webssh.html

## Локальная сборка архивов

```bash
bash scripts/build-bundles.sh
ls -lh dist/
```

## Загрузка в ADCM

### Через UI

1. В ADCM откройте раздел `Bundles`.
2. Нажмите `Upload Bundle`.
3. Выберите нужный `adcm-*.tgz`.

### Через API

```bash
curl -X POST \
  -H "Authorization: Token YOUR_TOKEN" \
  -F "file=@dist/adcm-jupyterhub-1.86p3.tgz" \
  http://adcm-host:8000/api/v1/stack/upload/
```
