# Книга рецептов

Сайт со статьями о рецептах и блюдах.
Доступный функционал:
 - работа через админку:
   - добавление рецептов и ингредиентов
   - добавление категорий, статей и тегов
   - загрузка изображений
   - встроенный редактор текста для инструкции из рецепта
 - статьи содержат:
   - категории
   - теги
   - рецепты
 - рецепты содержат:
   - ингредиенты
   - инструкцию
   - фотографию
 - реализовано меню:
   - домашняя страница
   - страница рецептов
   - меню категорий: фильтрация статей по категориям
   

## Использование Docker

### Настройка проекта
Загрузите проект в нужный репозиторий:

```bash
git clone https://github.com/jBuly4/Y_lab_Hometasks/tree/main/task_4
```

Создайте `.env` файл в корне репозитория:

```bash
cp .env .env
```

Внесите при необходимости корректировки в переменные окружения.

### Запуск проекта

При первом запуске в корне репозитория выполните команды:

```bash
docker-compose up -d --build db
```

```bash
docker-compose up -d --build app
```

При первом запуске и в далнейшем для запуска приложения выполните команду:

```bash
docker-compose up --build
```

При первом запуске процессы могут занять несколько минут.


### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

Проект доступен по адресу http://127.0.0.1:8000

### Возможные проблемы

- установка psycopg2:
  - Error: pg_config executable not found.
  - Возможное решение: https://www.compose.com/articles/postgresql-tips-installing-the-postgresql-client/ 
    - install libpq - это починит pg_config
  - Решение: https://stackoverflow.com/questions/26288042/error-installing-psycopg2-library-not-found-for-lssl 
    - env LDFLAGS="-I/opt/homebrew/opt/openssl/include -L/opt/homebrew/opt/openssl/lib" pip --no-cache install psycopg2
- при проблемах с докером:
  - Коннектим postgresql и джанго:
    - https://djangocentral.com/using-postgresql-with-django/
    - не забываем скорректировать settings
- при проблеме запуска Postgres: https://stackoverflow.com/questions/50993655/how-to-run-a-postgres-command-could-not-identify-current-directory
  - запускать стоит из корневой директории, где установлена СУБД