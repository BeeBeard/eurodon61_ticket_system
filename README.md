# API для тикет системы

Backend-сервис для управления пользовательскими заявками (tickets),
построенный на FastAPI + SQLAlchemy + Alembic.

------------------------------------------------------------------------

## Стек технологий

-   Python 3.11+
-   FastAPI
-   SQLAlchemy
-   Alembic (миграции)
-   SQLite (по умолчанию)
-   Pydantic
-   Jinja2 (HTML report)

------------------------------------------------------------------------

## Возможности

-   Создание заявок
-   Получение списка заявок
-   Фильтрация по `status` и `priority`
-   Получение заявки по ID
-   Обновление статуса заявки
-   Получение статистики
-   HTML-отчёт по заявкам

------------------------------------------------------------------------

## Архитектура проекта

```text
ticket-system/
├── data/                      # SQLite база данных (tickets.db)
├── src/                       # Основной код приложения
│   ├── api/                   # REST API эндпоинты
│   ├── core/                  # Ядро: конфигурация, база данных, зависимости
│   ├── modules/               # Бизнес-модули
│   │   └── tickets/           # Модуль тикетов
│   ├── shared/                # Общие модели, утилиты, схемы
│   ├── templates/             # HTML-шаблоны (если используются)
│   └── app.py                 # Главный файл FastAPI приложения
├── migrations/                # Alembic миграции
│   └── versions/              # Файлы миграций
├── .env.example               # Пример переменных окружения
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── README.md
├── requirements.txt
└── data/.gitkeep              # Чтобы папка data попадала в Git
```
------------------------------------------------------------------------

## Установка

``` bash
git clone <repo_url>
cd ticket_system

python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

------------------------------------------------------------------------

## Переменные окружения

Создайте файл `.env`:

``` env
DATABASE_URL=sqlite:////app/data/tickets.db
```

------------------------------------------------------------------------

## Миграции

Создать миграцию:

``` bash
docker compose run --rm --entrypoint "alembic" ticket-system revision --autogenerate -m "add new feature"
```

Применить миграции:

``` bash
docker compose run --rm --entrypoint "alembic" ticket-system upgrade head
```

------------------------------------------------------------------------

## Запуск

``` bash
git clone <репозиторий>
cd ticket_system

# Первый запуск (сборка образа)
docker compose up --build

# Запуск в фоне
docker compose up -d
```

После запуска:

-   Swagger UI: http://127.0.0.1:8000/docs
-   ReDoc: http://127.0.0.1:8000/redoc

------------------------------------------------------------------------

## API

### Создать заявку

``` http
POST /tickets
```

### Получить список заявок

``` http
GET /tickets
GET /tickets?status=open
GET /tickets?priority=high
GET /tickets?status=open&priority=high
```

### Получить заявку

``` http
GET /tickets/{ticket_id}
```

### Изменить статус

``` http
PATCH /tickets/{ticket_id}/status
```

### Статистика

``` http
GET /stats
```

### HTML-отчёт

``` http
GET /report
```

Отображает:

-   общую статистику;
-   распределение по приоритетам;
-   последние 10 заявок.

------------------------------------------------------------------------

[//]: # (## 🧪 Тестирование)

[//]: # ()
[//]: # (``` bash)

[//]: # (pytest)

[//]: # (```)

[//]: # (------------------------------------------------------------------------)

## Архитектурные решения

-   Модульная структура проекта.
-   SQLAlchemy ORM.
-   Alembic для управления миграциями.
-   Pydantic для валидации данных.
-   FastAPI Depends для внедрения зависимостей.
-   Jinja2 для формирования HTML-отчёта.


