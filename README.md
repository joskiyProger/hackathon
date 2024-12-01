# Система мотивации для сотрудников


>Мы предлагаем создать лидерборд менеджеров с отображением их места в рейтинге, ФИО, суммой, на которую они совершили сделки, и в связи с этим заработанной премией.

>Так же у каждого сотрудника должен быть личный кабинет, в котором он сможет смотреть график роста своей премии в течении месяца, количество совершённых сделок и прочую информацию.

# Установка

Для работы с бэкендом мы истользуем фреймворк FasAPI на Python. 

## Установка Python на Linux 

```
sudo apt update
sudo apt install python3
sudo apt install python3 python3-pip
python --version
pip --version #команды для проверки успешности утановки: 
```

## Создание виртуального окружения

Далее везде, где будет использоваться команда python, в случае неудачи выполнения этой команды попробуйте использовать python3.

Для создания виртуального окружения используйте команду python -m venv ИМЯ ОКРУЖЕНИЯ и активируйте его source ИМЯ ОКРУЖЕНИЯ/bin/activate. После этого можно устанавливать фреймворки для Python.
```
git checkout develop
apt install python3.12-venv
python -m venv .venv
source .venv/bin/activate
pip install psycopg2-binary
sudo apt install libpq-dev python3-dev
pip install -r requirements.txt
```

## Подключение к базе данных

В нашем проекте была использована база данных PostgreSQL. Чтобы иметь возможность взаимодействовать с ней через терминал используйте команды:
```
sudo apt install postgresql postgresql-contrib
psql --version проверка успешного выполнения
sudo service postgresql start запуск сервера
sudo -u postgres psql открытие консоли для работы с PostgreSQL
```

## Восстановление БД

Чтобы создать БД, выполни эти команды из корня репозитория (скопируй и вставь в терминал):
```
sudo -u postgres dropdb motivation_storage # Удаляет БД, если она уже была
sudo -u postgres createdb motivation_storage
psql -U postgres -d motivation_storage -f schema.sql # Восстанавливает таблицы
psql -U postgres -d motivation_storage -f data.sql # Восстанавливает данные таблиц
```
>Если будут выводиться надписи `Permission denied` зайдите в файл
`sudo nano /etc/postgresql/[version]/main/pg_hba.conf` #замените в этом файле первые четыре подключения на trust

# Фронтенд

Нужно запустить второй терминал, чтобы он работал одновременно с сервером. Заупуск происходит при помощи следующих команд 

```
cd templates 
sudo apr install npm
npm update
npm install node
npmrun dev #сам запуск фронтенда
```

# Запуск

После успешной установки пропишите в терминал команду uvicorn main:app --reload, после чего перейдите по адресу `http://127.0.0.1:8000/`

Сейчас БДшкой владеет супер-пользователь postgres, по хорошему нужно создать новую роль, и проводить все махинации от имени этой новой роли