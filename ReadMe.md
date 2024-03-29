# REST API для сервиса терминологии

## Установка

```console
git clone https://github.com/expmax85/Komtest
cd Komtest/
python3 -m pip install -r requirements.txt
```
Cоздать файл `.env` и заполнить его по шаблону файла `.env.template`, или переименовать `.env.template`.
Установить и создать БД, заполнить все поля файла `.env`.
```console
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```

> [!NOTE]
> При установке в OS Windows использовать `python` вместо `python3`.
### Тестовые данные
Если необходимо, можно заполнить проект тестовыми данными, выполнив следующие команды перед командой `runserver`:
```console
python3 manage.py loaddata fixtures/users.json
python3 manage.py loaddata fixtures/manuals.json
python3 manage.py loaddata fixtures/versions.json
python3 manage.py loaddata fixtures/elements.json

```

## Docker
Чтобы запустить проект через docker-compose, необходимо переименовать файл `.env.template` в `.env`, внести правки при необходимости в нем и в файле `docker-compose.yml`.
В контейнере используются python3.8 и postgres последней версии.
И выполнить поочередно следующие команды:
```console
sudo docker-compose build
sudo docker-compose up
```

## Swagger
```
/swagger/
```

## Админ панель

В административной панели django доступно управление справочниками, версиями и их элементами: создание, удаление и изименение
В случае загрузку тестовых данных, пользователь с правами администратора будет создан автоматически:
```
login: admin
password: 123456
```
Для ручного создания суперпользователя, используйте команду:
```console
python3 manage.py createsuperuser
```

## Получение списка справочников
```
/api/manuals/
```

## Получение списка справочников, актуальных на указанную дату
```
/api/manuals/?from_date=<date>
```
Значение `date` должно быть указано в формате `YYYY-MM-DD`. Например, следующий запрос выведет акутальные справочики на 15.06.2022:
```
/api/manuals/?from_date=2022-06-15
```
Также параметр `from_date` может принимать в качестве значения `today`, если необходимо вывести актуальные справочники на данный момент: 
```
/api/manuals/?from_date=today
```

## Получение элементов заданного справочника текущей версии
```
/api/elems/?manual_id=<manual id>
```
Параметр `manual_id` - идентификатор нужного справочника. 
Например, следующий запрос выведет элементы справочника из тестовых данных с идентификатором `2` текущей версии:
```
/api/elems/?manual_id=2
```
## Валидация элементов заданного справочника текущей версии
```
/api/elems/?manual_id=2&code=<code>&value=<value>
```
Данный метод позволяет проверить, существует ли элемент по введенным параметрам `code` и `value` в справочнике `manual_id` текущей версии. Параметр `manual_id` является обязательным. 
Допускается использование параметров `value` и `code` независимо друг от друга. В случае наличия элемента в справочнике, будет выведен непосредственно данный элемент или элементы, если их несколько. В случае отсутствия - сообщение об отсутсвии элемента или справочника.
Например, следующий запрос выведет элемент с параметрами `code=32135` `value=value_2` из тестовых данных:
```
/api/elems/?manual_id=1&code=32134&value=value_22
```
А данный запрос выведет сообщение об отсутствии элемента, так как элемента с заданным параметром `code` в тестовых данных нет:
```
/api/elems/?manual_id=1&code=32140
```
## Получение элементов заданного справочника указанной версии
```
/api/elems/?manual_id=<manual id>&version=<version>
```
Параметр `manual_id` - идентификатор нужного справочника, а `version` - версия справочника. 
Например, следующий запрос выведет элементы справочника из тестовых данных с идентификатором `1` версии `1.0.1`:
```
/api/elems/?manual_id=1&version=1.0.1
```
## Валидация элементов заданного справочника указанной версии
```
/api/elems/?manual_id=2&version=<version>&code=<code>&value=<value>
```
Данный метод позволяет проверить, существует ли элемент по введенным параметрам `code` и `value` в справочнике `manual_id` версии `version`. Параметр `manual_id` является обязательным. 
Допускается использование параметров `value` и `code` независимо друг от друга. В случае наличия элемента в справочнике, будет выведен непосредственно данный элемент или элементы, если их несколько. В случае отсутствия - сообщение об отсутсвии элемента или справочника.
Например, следующий запрос выведет элемент с параметрами `code=32134` справочника с идентификатором `1` версии `1.0.0` из тестовых данных:
```
/api/elems/?manual_id=1&version=1.0.0&code=32134
```
