# Electronics Network API
## Описание проекта.
Electronics Network API — это RESTful API для управления сетью по продаже электроники, разработанное с использованием Django и Django REST Framework (DRF). Проект поддерживает иерархическую структуру участников сети (заводы, розничные сети, индивидуальные предприниматели) и связанных с ними продуктов, а также управление пользователями с JWT-аутентификацией.

## Проект разделен на три основных приложения:
users: Управление пользователями (CustomUser) с ролями и аутентификацией через JWT.
product: Управление продуктами (Product), связанными с участниками сети.
network: Управление участниками сети (NetworkNode) с трёхуровневой иерархией.

## Технические требования
Python 3.8+
Django 3+
DRF 3.10+
PostgreSQL 10+
Swagger и Redoc /OpenAPI для документации

## Установка:
Клонируйте репозиторий
https://github.com/MaximOdeg/Electronics.git
# Создайте виртуальное окружение:
python -m venv venv
# Активируйте виртуальное окружение:
venv\Scripts\activate - для Windows
source venv/bin/activate - для macOS/Linux
# Установите зависимости
pip install -r requirements.txt
# Создайте файл .env на основе .env.sample
SECRET_KEY=
DEBUG=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
# Примените миграции:
python manage.py makemigrations
python manage.py migrate
# Создайте суперпользователя:
python manage.py createsuperuser_custom --email youemail --password youpassword
## Запуск проекта
# Запустите сервер
python manage.py runserver
# Тестирование
Используйте Postman для отправки запросов к API.
## Документация
Для Swagger UI - http://127.0.0.1:8000/swagger/
