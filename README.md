# Приложение Каталог книг

## Cклонировать проект git clone git@github.com:Beka757/books-api.git

### Локальный запуск проекта
- Установить виртуальное окружение pip install -m venv venv
- Запустить виртуальное окружение source venv/bin/activate
- Установить зависимости pip install -r requirements.txt
- Подключить базу данных (sqlite3, postgres)
- Провести миграции python3 manage.py migrate
- Загрузить фикстуры python3 manage.py loaddata fixtures.json
- Запустить проект python3 manage.py runserver
- Перейти по адресу localhost:8000

### Запуск проекта на докере
- Запустить проект(в фоновом режиме) docker-compose up -d
- Перейти по адресу 0.0.0.0:8000 или localhost:8000


### Swagger документация по адресу /schema/swagger/

### Супер юзер email admin@admin.com password admin