# ADCM Bundle Community 🚀

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fadcm-bundle.duckdns.org)](https://adcm-bundle.duckdns.org)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Community](https://img.shields.io/badge/community-open-brightgreen.svg)](https://adcm-bundle.duckdns.org)

Открытое сообщество разработчиков бандлов для Arenadata Cluster Manager (ADCM).

🌐 **Сайт:** [adcm-bundle.duckdns.org](https://adcm-bundle.duckdns.org)

## 📖 О проекте

**ADCM Bundle Community** — это открытая платформа для разработки, публикации и обмена бандлами для ADCM. Мы создаем экосистему готовых решений для оркестрации инфраструктуры.

### Что такое ADCM?

**ADCM** (Arenadata Cluster Manager) — это платформа для оркестрации инфраструктуры.

**Бандл** — это пакет для интеграции с ADCM, содержащий:
- Описание сервисов и их конфигураций (YAML DSL)
- Ansible playbooks для автоматизации
- Метрики и настройки мониторинга
- Документацию по развертыванию

## 📦 Доступные бандлы

| Бандл | Версия | Автор | Размер | Описание |
|-------|--------|-------|--------|----------|
| **JupyterHub** | 1.86p1 | D.V. Iatsenko | ~120KB | Многопользовательская среда для Jupyter Notebooks с поддержкой 12+ языков программирования и LaTeX |
| **pgAdmin 4** | 1.0.5 | D.V. Iatsenko | ~24KB | Web-интерфейс для администрирования PostgreSQL |
| **WebSSH** | 1.0.5 | D.V. Iatsenko | ~22KB | Web-терминал для SSH подключений из браузера |

📥 **Скачать:** Все бандлы доступны в директории `dist/`

🌐 **Подробнее:** [adcm-bundle.duckdns.org](https://adcm-bundle.duckdns.org/#bundles)

## 🚀 Быстрый старт

### Использование готовых бандлов

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/d-yacenko/adcm-bundle-community.git
cd adcm-bundle-community

# 2. Готовые бандлы находятся в dist/
ls -lh dist/

# 3. Загрузите бандл в ADCM через Web UI или API
```

### Разработка собственного бандла

См. [examples/simple-bundle](examples/simple-bundle) для примера.

**Документация:**
- [Bundle DSL спецификация](https://docs.arenadata.io/ru/ADCM/current/references/bundle-dsl.html)
- [Руководство по разработке](https://docs.arenadata.io/ru/ADCM/current/dev-tools/bundle-guide.html)

## 🤝 Участие в проекте

Мы приветствуем вклад от сообщества! См. [CONTRIBUTING.md](CONTRIBUTING.md)

### Как добавить бандл:

1. **Fork** репозиторий
2. Создайте директорию в `bundles/your-bundle/`
3. Разработайте и протестируйте бандл
4. Соберите `.tgz` файл: `./scripts/build-bundles.sh`
5. Создайте **Pull Request**

## 📁 Структура репозитория

```
adcm-bundle-community/
├── bundles/              # Исходники бандлов
├── dist/                 # Готовые .tgz файлы
├── examples/             # Примеры и шаблоны
├── scripts/              # Скрипты сборки
├── .github/workflows/    # CI/CD
└── docs/                 # Документация
```

## 📚 Документация

- [ADCM Documentation](https://docs.arenadata.io/ru/ADCM/)
- [Bundle DSL Reference](https://docs.arenadata.io/ru/ADCM/current/references/bundle-dsl.html)
- [ADCM API](https://docs.arenadata.io/ru/ADCM/current/dev-tools/adcm-api.html)
- [Руководство по релизам](RELEASING.md)

## 💬 Сообщество

- 💬 [Telegram](https://t.me/adcm_community)
- 🐛 [Issues](https://github.com/d-yacenko/adcm-bundle-community/issues)
- 💡 [Discussions](https://github.com/d-yacenko/adcm-bundle-community/discussions)

## 🔗 Связанные репозитории

- [landing](https://github.com/d-yacenko/landing) - Веб-сайт сообщества

## 📄 Лицензия

Apache License 2.0 - см. [LICENSE](LICENSE)

---

<div align="center">

**Создано с ❤️ сообществом ADCM**

[Website](https://adcm-bundle.duckdns.org) • [Documentation](https://docs.arenadata.io/ru/ADCM/) • [GitHub](https://github.com/d-yacenko/adcm-bundle-community)

</div>
