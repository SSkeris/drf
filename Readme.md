# lms_project

Платформа для онлайн-обучения - LMS-система, в которой каждый желающий может размещать свои полезные материалы или
курсы.

<!-- ABOUT THE PROJECT -->

## О проекте

*Бэкенд-сервер, который возвращает на запросы эндпоинтов JSON-структуру.*
*Используется СУБД Postgres*

- В проекте представлены приложения *users*, *materials*, *subscription*.
- Реализованы модели (User, Payment, Course, Lesson, Subscription).
- Для реализации CRUD используется Viewsets и Generic-классы.
- Для работы контроллеров описаны сериализаторы (вложенные сериализаторы; описаны вычисляемые данные).
- Настроена фильтрация для эндпоинта вывода списка платежей с возможностями:
    - менять порядок сортировки по дате оплаты,
    - фильтровать по курсу или уроку,
    - фильтровать по способу оплаты.
- В проекте используется JWT-авторизация, каждый эндпоинт закрыт авторизацией.
- Реализована группа 'модератор', описаны права доступа для объектов, реализована проверка прав.
- Настроена валидация для сохранения уроков на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com.
- Реализована пагинация для вывода всех уроков и курсов.
- Написаны тесты для проверки моделей Lesson, Course, Subscription.
- Подключен и настроен вывод документации для проекта. Для работы с документацией проекта использовалась библиотека
  drf-yasg.
- Подключена возможность оплаты курсов через https://stripe.com/docs/api. Реализованы:
    - создание продукта;
    - создание цены;
    - создание сессии для получения ссылки на оплату;
    - проверка статуса платежа.
- Реализованы задачи в Celery:
    - *send_mail_about_updates* - отложенная задача. При обновлении курса отправляется письмо пользователю, подписанному
      на курс.
    - *check_last_login* - периодическая задача, реализована с использованием celery-beat. Статус пользователей, которые
      не заходили в учетную запись больше месяца, меняется на неактивный.

<!-- GETTING STARTED -->

## Подготовка к работе

Чтобы запустить локальную копию, выполните следующие простые шаги:

### Установка

Если вы используете Docker, то просто клонируйте проект используя ссылку
из пункта "1" ниже и в терминале используйте команду:
```sh
docker-compose up -d --build
```
В противном случае следуйте шагам ниже.

1. Клонируйте проект
   ```sh
   git@github.com:SSkeris/drf.git
   ```
2. Убедитесь, что вы получили из удаленного репозитория все ветки и переключились на ветку разработки develop
   ```sh
   git checkout develop
   ```
3. Установите зависимости проекта (в случае, если не установились при клонировании)
   ```sh
   pip install -r requirements.txt
   ```
   или
   ```sh
   python -m pip install -r requirements.txt
   ```
4. Создайте в корне проекта файл .env и заполните переменные среды в соответствии с желаемой конфигурацией, используя
   файл .env_sample
5. Примените миграции
   ```sh
   python manage.py migrate
   ```

### Запуск приложения

1. Для того, чтобы запустить проект, выполните команду
   ```sh
   python3 manage.py runserver
   ```
2. Работу каждого эндпоинта необходимо проверять с помощью Postman.

### Запуск задач в Celery

В проекте реализованы отложенные и периодические задачи.

1. Для запуска **отложенной задачи**, выполните команду
   ```sh
   celery -A config worker -l INFO
   ```
2. Для запуска **периодической задачи**, выполните команды

```sh
   celery -A config worker --loglevel=info
   celery -A config beat -l INFO -S django
   ```

для запуска на **Windows** может потребоваться установка evenlet или gevent

```sh
    celery -A config worker -l info -P "имя библиотеки: eventlet/gevent"
    celery -A config beat -l INFO -S django
   ```

### Тестирование

Для запуска тестов, находясь в виртуальном окружении проекта, выполните команды

```sh
   coverage run --source='.' manage.py test
   ```

и

```sh
   coverage report
   ```

Для генерации HTML-отчета в целях оценки покрытия тестами выполните команду

```sh
   coverage html
   ```