# Киноколлекция случайных фильмов 

С помощью этого приложения можно делать запрос с различными 
параметрами фильтрации к API Кинопоиска и в ответ получать 
список случайных тайлов фильмов, понравившиеся можно 
сохранять в свою коллекцию. Также из коллекции можно удалить не нужные фильмы.

Для отправки запроса на получение случайных фильмов авторизация не обязательна, 
но для сохранения тайла с фильмом необходимо зарегистрироваться и авторизоваться.

На данный момент пользователям доступно изменение следующих параметров запроса: 
жанр и количество. В конфигурации проекта в файле `app/kino/settings.py` можно 
задать дополнительные параметры запроса. Настройки по умолчанию:
```python
ADDITIONAL_REQUEST_PARAM = {
        'rating.kp': '8-10', # диапазон рейтинга на Кинопоиске
        'year': '2000-2023', # временной период
}
```
Дополнительные возможные параметры указаны в 
[документации kinopoisk api](https://api.kinopoisk.dev/documentation#/Фильмы%2C%20сериалы%2C%20и%20т.д./MovieController_getRandomMovieV1_4)


## Запуск приложения.

Для работы приложения необходимо в боте 
[@kinopoiskdev_bot](https://t.me/kinopoiskdev_bot) получить токен. 

Клонировать репозиторий.
```shell
git clone
```

В корне проекта создать файл `.env` заполнить его по следующему шаблону:
```shell
SECRET_KEY=<djangokey>
DEBUG=1
ALLOWED_HOSTS=127.0.0.1 localhost [::1] testserver
CSRF_TRUSTED_ORIGINS=http://127.0.0.1 http://localhost
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=database
POSTGRES_PORT=5432
CELERY_BROKER_URL = 'redis://redis:6379/0'
API_KEY=<kinopoist apikey>
```
Из корня проекта запустить команду в терминале:
```shell
docker compose up -d
```

Приложение будет доступно по адресу http://localhost:8000


### Асинхронность.

Отправка запросов к API Кинопоиска осуществляется асинхронно с использованием библиотек 
asyncio и httpx.

### Фоновые задачи.
Для скачивания и сохранения на локальный диск постеров фильмов 
используется фоновая задача Celery, настроить которую можно через административную
панель Django. Для этого необходимо создать суперпользователя, пройти по адресу 
http://localhost/admin/, в боковом меню выбрать пункт 'Intervals', затем на открывшейся странице 
нажать "Add interval", и заполнить открывшуюся форму: количество периодов и интервал 
периода. Далее в боковом меню необходимо выбрать пункт 'Periodic tasks', затем на открывшейся странице 
нажать "Add periodic task", и заполнить форму: название задачи, из выпадающего меню выбрать саму
задачу (selections.task.download_img), и задать ранее созданный интервал.