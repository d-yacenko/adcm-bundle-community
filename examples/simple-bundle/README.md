# Simple Service Bundle

Пример простого ADCM бандла для демонстрации базовой структуры и возможностей.

## 📖 Описание

Этот бандл является учебным примером и демонстрирует:
- Базовую структуру ADCM бандла
- Описание прототипов в config.yaml
- Использование Ansible playbooks
- Конфигурацию параметров
- Определение действий (actions)
- Работу с компонентами

## 🎯 Назначение

Используйте этот бандл как:
- **Шаблон** для создания собственных бандлов
- **Учебный материал** для изучения ADCM
- **Отправную точку** для разработки

## 📋 Требования

- ADCM версия: >= 2024.01.01.00
- ОС: CentOS 7/8, RHEL 7/8, Ubuntu 20.04/22.04
- Python 3.6+
- Ansible (предустановлен в ADCM)

## 🚀 Быстрый старт

### 1. Подготовка бандла

```bash
# Упакуйте бандл в tar.gz
cd examples/simple-bundle
tar czf simple-service-1.0.0.tar.gz *
```

### 2. Загрузка в ADCM

**Через Web UI:**
1. Откройте ADCM Web UI
2. Перейдите в раздел "Bundles"
3. Нажмите "Upload Bundle"
4. Выберите файл `simple-service-1.0.0.tar.gz`

**Через API:**
```bash
curl -X POST \
  -H "Authorization: Token YOUR_TOKEN" \
  -F "file=@simple-service-1.0.0.tar.gz" \
  http://adcm-host:8000/api/v1/stack/upload/
```

### 3. Создание кластера

1. В ADCM UI перейдите в "Clusters"
2. Нажмите "Create Cluster"
3. Выберите "Simple Service 1.0.0"
4. Укажите имя кластера
5. Настройте конфигурацию (опционально)

### 4. Добавление хостов

1. Создайте или выберите существующий hostprovider
2. Добавьте хосты в hostprovider
3. Импортируйте хосты в кластер

### 5. Host-Component Mapping

1. Перейдите на вкладку "Hosts"
2. Нажмите "Configure host-components"
3. Распределите компоненты по хостам:
   - `SERVER` - основной сервер (минимум на 1 хост)
   - `CLIENT` - клиент (опционально)

### 6. Установка

1. Перейдите на вкладку "Actions"
2. Запустите действие "Install Service"
3. Дождитесь успешного завершения

## ⚙️ Конфигурация

### Параметры сервиса

| Параметр | Тип | По умолчанию | Описание |
|----------|-----|--------------|----------|
| `service_settings.port` | integer | 8080 | Порт для прослушивания |
| `service_settings.bind_address` | string | 0.0.0.0 | IP адрес привязки |
| `service_settings.log_level` | option | info | Уровень логирования |
| `performance.worker_threads` | integer | 4 | Количество рабочих потоков |
| `performance.enable_cache` | boolean | true | Включить кэширование |

### Изменение конфигурации

1. Перейдите на вкладку "Configuration"
2. Измените необходимые параметры
3. Сохраните изменения
4. Запустите действие "Configure Service"

## 🔧 Действия (Actions)

| Действие | Описание | Доступно в состояниях |
|----------|----------|----------------------|
| **Install Service** | Установка и настройка сервиса | created |
| **Configure Service** | Применение конфигурации | installed, configured |
| **Start Service** | Запуск сервиса | installed, configured, stopped |
| **Stop Service** | Остановка сервиса | started |
| **Restart Service** | Перезапуск сервиса | started |
| **Check Status** | Проверка состояния | любое |

## 📁 Структура бандла

```
simple-bundle/
├── config.yaml              # Описание прототипов
├── ansible/                 # Ansible playbooks
│   ├── install.yaml        # Установка
│   ├── configure.yaml      # Конфигурация
│   ├── start.yaml          # Запуск
│   ├── stop.yaml           # Остановка
│   ├── restart.yaml        # Перезапуск
│   ├── check_status.yaml   # Проверка статуса
│   └── templates/          # Jinja2 шаблоны
│       ├── service.conf.j2
│       └── systemd.service.j2
├── README.md                # Документация
└── LICENSE                  # Лицензия
```

## 🎓 Обучающие материалы

### Основные концепции

**1. Прототипы (Prototypes)**

В ADCM есть несколько типов прототипов:
- `cluster` - кластер (контейнер для сервисов)
- `service` - сервис (логическая группа компонентов)
- `component` - компонент (устанавливается на хосты)
- `provider` - хостпровайдер (управление хостами)
- `host` - хост (физический или виртуальный сервер)

**2. Конфигурация**

Параметры конфигурации могут быть:
- `string`, `text` - строки
- `integer`, `float` - числа
- `boolean` - логические значения
- `option` - выбор из списка
- `list`, `map`, `json` - структуры данных
- `group` - группировка параметров
- `password`, `secretfile` - секретные данные

**3. Состояния (States)**

Объекты ADCM имеют состояния:
- `created` - создан, но не установлен
- `installed` - установлен
- `configured` - сконфигурирован
- `started` - запущен
- `stopped` - остановлен

**4. Действия (Actions)**

Actions переводят объекты между состояниями:
```yaml
states:
  available: [created]      # Доступно из состояния
  on_success: installed     # Перейти в состояние при успехе
  on_fail: created          # Перейти в состояние при ошибке
```

**5. Компоненты и constraints**

Constraints определяют сколько экземпляров компонента нужно:
- `[1]` - ровно один
- `[0,1]` - ноль или один
- `[1,+]` - один или более
- `[+]` - на всех хостах
- `[1,odd]` - нечетное количество

### Переменные в Ansible

ADCM предоставляет переменные в inventory:

```yaml
# Конфигурация кластера
{{ cluster.config.service_settings.port }}

# Информация о кластере
{{ cluster.name }}
{{ cluster.id }}

# Конфигурация сервиса
{{ services.SIMPLE_SERVICE.config.parameter }}

# Информация о хосте
{{ hostvars[inventory_hostname].ansible_fqdn }}
```

## 🔍 Отладка

### Просмотр логов

Логи actions доступны в ADCM UI:
1. Перейдите в "Jobs"
2. Выберите нужную задачу
3. Просмотрите логи выполнения

### Проверка inventory

ADCM генерирует Ansible inventory:
```bash
# На сервере ADCM
cat /adcm/data/run/<job_id>/inventory.json
```

### Тестирование playbook

```bash
# Тестовый запуск без изменений
ansible-playbook -i inventory.ini install.yaml --check

# С отладочной информацией
ansible-playbook -i inventory.ini install.yaml -vvv
```

## 📚 Дополнительные ресурсы

- [Bundle DSL Reference](https://docs.arenadata.io/ru/ADCM/current/references/bundle-dsl.html)
- [ADCM API Documentation](https://docs.arenadata.io/ru/ADCM/current/dev-tools/adcm-api.html)
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Community Website](https://adcm-bundle.duckdns.org)

## 🐛 Известные проблемы

Нет известных проблем. Это учебный пример.

## 📄 Лицензия

Apache License 2.0

## 🤝 Участие

Нашли проблему или хотите улучшить пример? 
Создайте [Issue](https://github.com/d-yacenko/adcm-bundle-community/issues) или [Pull Request](https://github.com/d-yacenko/adcm-bundle-community/pulls)!

---

**Создано сообществом ADCM Bundle Community**
