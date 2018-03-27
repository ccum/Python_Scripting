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

pip install --user pipenv
pip install pipenv
mkdir -p code/pgbackup
cd code/pgbackup
pipenv install --two
To activate this project's virtualenv, run the following:
 $ pipenv shell
    
mkdir -p src/pgbackup test docs
touch src/pgbackup/__init__.py docs/.keep test/.keep

curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -o .gitignore