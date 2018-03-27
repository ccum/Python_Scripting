```python
$ pip install --user virtualenv
$ mkdir venvs
$ virtualenv venvs/pg
$ source venvs/pg/bin/activate
(pg) $ pip install psycopg2

```

curl -o db_setup.sh https://raw.githubusercontent.com/ccum/content-python-for-sys-admins/master/helpers/db_setup.sh
chmod u+x db_setup.sh
./db_setup.sh

cliente : https://www.postgresql.org/download/macosx/
brew install postgresql


psql postgres://root:ppppgioassword@34.227.101.103:80/sample -c "SELECT count(id) FROM employees;"