# Текущие задачи

* [ ] Внимательно прочитать `README.md`. Задать вопросы, сформировать первую итерацию понимания написанного.
* [ ] Установить [docker](https://docs.docker.com/engine/install/ubuntu/)
  , [docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)
  . Ссылки примерные, не факт, что по этим туториалам получится установить и то и другое, возможно придётся самому
  погуглить.
* [ ] Запустить `make core-up`, удостовериться, что все сервисы запущены.
    * Изучить команды
        * `docker-compose up --build -d`
        * `docker-compose down`
        * `docker-compose stop`
* [ ] Запустить `main` из `/run` (см `README.md`). Получить такой вывод в консоль: `Should start server on 0.0.0.0:1980`
* [ ] Написать код исходного сервера.
    * Достать конфигурации из переменных окружения.
    * Запустить примитивный сервер на нужном хосте и порте.
* [ ] Написать ручки для отдачи фронтенда и статики:
    * На `404`-ю ошибку при `GET` запросах
      возвращать `index.html` ([пример нагугленного](https://stackoverflow.com/questions/29516093/how-to-redirect-to-a-external-404-page-python-flask))
      .
    * Возвращать файлы из `/static` на
      урле `/static/*` ([тут второй ответ правильный](https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask))
      .
    * В результате задача будет выполнена если получится увидеть фронтенд, который будет сыпать ошибками из-за того, что
      ручки, которые должны отдавать ему данные, еще не реализованы
* [ ] Написать модель данных для `sqlalchemy`: `User`.
    * Необходимо будет подключиться к базе данных, используя данные из `env` конфигураций.
* [ ] Написать код для работы с сессией пользователя, реализовать хендлеры из `API.md`
    * `API.md` придётся не один раз прочитать и задавать вопросы по каждому хендлеру пока не станет понятно в чём их
      назначение.
