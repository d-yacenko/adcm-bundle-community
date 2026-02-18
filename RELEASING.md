# Релизы ADCM бандлов

Этот репозиторий хранит исходники бандлов в `bundles/*`.
Готовые архивы `*.tgz` публикуются как assets в GitHub Releases.

## Как устроен GitHub Releases

GitHub Release привязан к Git-тегу и содержит:
- заголовок релиза (`v1.0.0`, `v2026.02.16` и т.д.);
- заметки о релизе (release notes);
- бинарные артефакты (в нашем случае `adcm-*.tgz` и `SHA256SUMS`).

В этом репозитории публикация автоматизирована workflow:
- файл: `.github/workflows/release.yml`;
- триггер: push тега `v*`;
- шаги: сборка `scripts/build-bundles.sh` -> загрузка файлов в Release.

## Локальная сборка артефактов

```bash
bash scripts/build-bundles.sh
ls -lh dist/
```

Скрипт создаёт:
- `dist/adcm-jupyterhub-<version>.tgz`
- `dist/adcm-pgadmin4-web-<version>.tgz`
- `dist/adcm-webssh-<version>.tgz`
- `dist/SHA256SUMS`

## Как выпустить релиз

1. Убедитесь, что изменения в `bundles/*` и документации готовы.
2. Обновите `CHANGELOG.md`.
3. Создайте и отправьте тег:

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

4. GitHub Actions автоматически создаст Release и прикрепит артефакты.
5. Проверьте страницу `Releases` и скачивание `*.tgz`.

## Скачивание для пользователей ADCM

Пользователи скачивают готовые архивы со страницы:
- `https://github.com/<owner>/<repo>/releases/latest`

и загружают нужный `*.tgz` в ADCM UI/API.
