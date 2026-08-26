# Руководство по участию в проекте

Спасибо за интерес к ADCM Bundle Community! Мы приветствуем вклад от всех участников сообщества.

## 🚀 Как начать

### 1. Изучите документацию

Перед началом разработки ознакомьтесь с:
- [Bundle DSL спецификацией](https://docs.arenadata.io/ru/ADCM/current/references/bundle-dsl.html)
- [Руководством по разработке прототипов](https://docs.arenadata.io/ru/ADCM/current/dev-tools/bundle-guide.html)
- [Существующими бандлами](https://adcm-bundle.duckdns.org/#bundles) в репозитории

### 2. Настройте окружение

```bash
# Форкните репозиторий на GitHub
# Клонируйте ваш форк
git clone https://github.com/YOUR_USERNAME/adcm-bundle-community.git
cd adcm-bundle-community

# Добавьте upstream remote
git remote add upstream https://github.com/d-yacenko/adcm-bundle-community.git

# Создайте новую ветку для вашей разработки
git checkout -b feature/my-new-bundle
```

## 📦 Разработка бандла

### Структура бандла

Минимальная структура бандла:

```
bundles/my-service/
├── config.yaml           # Обязательно: описание прототипов
├── ansible/              # Обязательно: Ansible playbooks
│   ├── install.yaml
│   ├── configure.yaml
│   └── start.yaml
├── monitoring/           # Рекомендуется: метрики
│   └── metrics.json
├── README.md             # Обязательно: документация
└── LICENSE               # Обязательно: лицензия
```

### Требования к бандлу

#### 1. config.yaml

- ✅ Корректный YAML синтаксис
- ✅ Соответствие [Bundle DSL спецификации](https://docs.arenadata.io/ru/ADCM/current/references/bundle-dsl.html)
- ✅ Указание `adcm_min_version`
- ✅ Осмысленные `display_name` и `description`
- ✅ Валидные constraints для компонентов

Пример:

```yaml
---
- type: cluster
  name: myservice
  version: 1.0.0
  display_name: "My Service"
  description: "Detailed description of the service"
  adcm_min_version: 2024.01.01.00
  
  config:
    - name: port
      type: integer
      default: 8080
      required: yes
      
  actions:
    install:
      display_name: "Install Service"
      type: job
      script_type: ansible
      script: ansible/install.yaml
      states:
        available: [created]
        on_success: installed
```

#### 2. Ansible Playbooks

- ✅ Идемпотентность (можно запускать многократно)
- ✅ Корректная обработка ошибок
- ✅ Использование переменных из ADCM inventory
- ✅ Логирование важных операций
- ✅ Поддержка разных ОС (если применимо)

Пример:

```yaml
---
- name: Install My Service
  hosts: all
  become: yes
  
  tasks:
    - name: Install package
      package:
        name: myservice
        state: present
      
    - name: Configure service
      template:
        src: config.j2
        dest: /etc/myservice/config.conf
      notify: restart service
      
  handlers:
    - name: restart service
      service:
        name: myservice
        state: restarted
```

#### 3. Документация (README.md)

Обязательные разделы:

```markdown
# My Service Bundle

## Описание
Краткое описание сервиса и возможностей бандла.

## Требования
- ADCM версия: >= 2024.01.01.00
- ОС: CentOS 7/8, Ubuntu 20.04/22.04
- Зависимости: список необходимых сервисов

## Установка
1. Загрузите бандл в ADCM
2. Создайте кластер
3. Добавьте хосты
4. Настройте host-component mapping
5. Запустите действие "Install"

## Конфигурация
Описание основных параметров конфигурации.

## Действия (Actions)
- **Install** - установка сервиса
- **Configure** - применение конфигурации
- **Start** - запуск сервиса
- **Stop** - остановка сервиса

## Известные проблемы
Список известных ограничений и проблем.

## Лицензия
Apache 2.0
```

#### 4. Лицензия

Каждый бандл должен содержать файл LICENSE с открытой лицензией:
- Apache License 2.0 (рекомендуется)
- MIT License
- GPL v3

### Тестирование

Перед созданием Pull Request протестируйте бандл:

0. **Автоматическая локальная проверка**
   ```bash
   python3 -m pip install -r requirements-dev.txt
   yamllint -c .yamllint.yml bundles examples
   python3 scripts/validate-bundles.py
   bash scripts/build-bundles.sh
   ```

1. **Загрузка в ADCM**
   ```bash
   # Соберите релизный архив локально
   bash scripts/build-bundles.sh

   # Через Web UI или API загрузите нужный архив из dist/
   curl -X POST -F file=@dist/adcm-my-service-1.0.0.tgz http://adcm-host:8000/api/v1/stack/upload/
   ```

2. **Создание кластера**
   - Создайте тестовый кластер
   - Добавьте хосты
   - Настройте host-component mapping

3. **Проверка действий**
   - Запустите все actions
   - Проверьте корректность установки
   - Проверьте работоспособность сервиса

4. **Проверка upgrade** (если применимо)
   - Обновите бандл до новой версии
   - Проверьте миграцию конфигурации

## 🔄 Процесс Pull Request

### 1. Подготовка

```bash
# Обновите вашу ветку из upstream
git fetch upstream
git rebase upstream/main

# Убедитесь, что все изменения закоммичены
git status
```

### 2. Коммиты

Следуйте [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add PostgreSQL bundle
fix: correct Kafka configuration template
docs: update Hadoop bundle README
test: add integration tests for HDFS
```

### 3. Создание PR

1. Push вашей ветки в форк:
   ```bash
   git push origin feature/my-new-bundle
   ```

2. Создайте Pull Request на GitHub

3. Заполните шаблон PR:
   ```markdown
   ## Описание
   Краткое описание изменений.
   
   ## Тип изменений
   - [ ] Новый бандл
   - [ ] Исправление существующего бандла
   - [ ] Обновление документации
   - [ ] Другое (опишите)
   
   ## Тестирование
   - [ ] Бандл загружается в ADCM
   - [ ] Actions выполняются успешно
   - [ ] Сервис работает корректно
   - [ ] CI `Validate bundles` завершился успешно
   - [ ] Документация актуальна
   
   ## Чеклист
   - [ ] Код следует Bundle DSL спецификации
   - [ ] Добавлена документация
   - [ ] Добавлена лицензия
   - [ ] Протестировано на ADCM
   ```

## 📋 Чеклист перед отправкой

- [ ] Код соответствует Bundle DSL спецификации
- [ ] Все Ansible playbooks идемпотентны
- [ ] Добавлена полная документация (README.md)
- [ ] Указана лицензия (LICENSE)
- [ ] Бандл протестирован на ADCM
- [ ] Конфигурация содержит осмысленные defaults
- [ ] Actions имеют корректные states
- [ ] Нет hardcoded значений (используются переменные)
- [ ] Код не содержит секретов и паролей
- [ ] Секретные Ansible tasks используют `no_log: true`
- [ ] Внешние загрузки используют HTTPS, фиксированную версию и проверку целостности
- [ ] Нет символических ссылок и путей, выходящих за каталог бандла
- [ ] Пользовательские значения не подставляются в shell-команды без безопасного quoting

Каждый бандл содержит исполняемые Ansible-сценарии и поэтому проходит ручной security review владельцем репозитория. Успешный CI подтверждает структуру и воспроизводимость сборки, но не заменяет анализ поведения playbooks.

## 🚀 Релизный процесс

- Исходники бандлов хранятся в `bundles/*`
- Готовые архивы публикуются в GitHub Releases
- Workflow релизов: `.github/workflows/release.yml`

Как выпустить релиз:

```bash
# 1) Обновите changelog и убедитесь, что сборка проходит
bash scripts/build-bundles.sh

# 2) Создайте и отправьте тег
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

После `push` тега `v*` GitHub Actions автоматически создаст Release и прикрепит `dist/*.tgz` + `SHA256SUMS`.

## 🐛 Отчеты об ошибках

При обнаружении ошибки откройте Pull Request с исправлением или сообщите о проблеме в [Telegram](https://t.me/adcm_bundle_community). Для PR укажите:

- Название и версия бандла
- Версия ADCM
- Описание проблемы
- Шаги для воспроизведения
- Ожидаемое поведение
- Логи (если применимо)

## 💡 Предложения по улучшению

Предложения оформляйте Pull Request’ом или направляйте в [Telegram](https://t.me/adcm_bundle_community).

## 📞 Связь с сообществом

- 💬 Telegram: [@adcm_bundle_community](https://t.me/adcm_bundle_community)
- 💬 Slack: [adcm-community.slack.com](https://adcm-community.slack.com)
- 📧 Email: community@adcm-bundle.org

## 🙏 Благодарности

Спасибо всем участникам сообщества за вклад в развитие проекта!

---

**Вопросы?** Напишите в [Telegram](https://t.me/adcm_bundle_community) или откройте Pull Request.
