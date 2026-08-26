# Релизы ADCM-бандлов

Репозиторий хранит исходники в `bundles/*`. Готовые архивы публикуются только как GitHub Release assets и не коммитятся в Git.

Каждый release содержит:

- `adcm-<bundle>-<version>.tgz` для каждого каталога в `bundles/`;
- `SHA256SUMS`;
- `catalog.json` с версиями, checksum и прямыми download URL.

## Предварительная проверка

```bash
python3 -m pip install -r requirements-dev.txt
yamllint -c .yamllint.yml bundles examples
python3 scripts/validate-bundles.py
bash scripts/build-bundles.sh
```

## Выпуск

Release workflow запускается тегом `v*`:

```bash
git switch main
git pull --ff-only
git tag -a v2026.08.26 -m "ADCM community bundles 2026.08.26"
git push origin v2026.08.26
```

Workflow повторно валидирует исходники, собирает все архивы и создаёт GitHub Release. После завершения необходимо проверить:

1. workflow `Release Bundles` завершился успешно;
2. Release не является draft или prerelease;
3. все `.tgz`, `SHA256SUMS` и `catalog.json` доступны без авторизации;
4. прямые ссылки с лендинга возвращают HTTP 200.

Версия каталога в теге и версии отдельных бандлов независимы: версия каждого `.tgz` берётся из cluster prototype в его `config.yaml`.
