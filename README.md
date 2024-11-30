## Восстановление БД

Сейчас БДшкой владеет супер-пользователь postgres, по хорошему нужно создать новую роль, и проводить все махинации от имени этой новой роли

Чтобы создать БД, выполни эти команды из корня репозитория (скопируй и вставь в терминал):

```
sudo -u postgres dropdb motivation_storage # Удаляет БД, если она уже была
sudo -u postgres createdb motivation_storage
psql -U postgres -d motivation_storage -f schema.sql # Восстанавливает таблицы
psql -U postgres -d motivation_storage -f data.sql # Восстанавливает данные таблиц
```
