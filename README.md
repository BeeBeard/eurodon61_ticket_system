# Ticket System API

Backend-сервис для управления пользовательскими заявками (tickets), построенный на FastAPI + SQLAlchemy + Alembic.

---

## 🚀 Стек технологий

- Python 3.11+
- FastAPI
- SQLAlchemy
- Alembic (миграции)
- SQLite
- Pydantic
- Jinja2 (HTML report)

---

## 📦 Возможности

- Создание заявок
- Получение списка заявок
- Фильтрация по status и priority
- Получение заявки по id
- Обновление статуса заявки
- Получение статистики
- HTML-отчёт по заявкам

---

## 📁 Архитектура проекта

```text
src/
├── api/                # REST API
├── core/               # инфраструктура (db, config)
├── modules/            # бизнес-модули (tickets, users)
├── shared/             # общие компоненты
├── templates/          # HTML шаблоны
├── app.py
migrations/
alembic.ini
README.md
main.py


```


## ⚙️ Установка
```bash
git clone <repo_url>
```
cd ticket_system

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt


---

---

---

---

---

---

# Ticket System API

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

``` text
src/
├── api/                # REST API
├── core/               # инфраструктура (db, config)
├── modules/            # бизнес-модули (tickets, users)
├── shared/             # общие компоненты
├── templates/          # HTML шаблоны
├── app.py
migrations/
alembic.ini
README.md
main.py
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


