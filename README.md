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


psql postgres://cecum:password@127.0.0.1:80/sample -c "SELECT count(id) FROM employees;"
pg_dump postgres://cecum:password@127.0.0.1:80/sample
pip install --user pipenv
pip uninstall pipenv
mkdir -p code/pgbackup
cd code/pgbackup
pipenv install --two
To activate this project's virtualenv, run the following:
 $ pipenv shell
    
mkdir -p src/pgbackup test docs
touch src/pgbackup/__init__.py docs/.keep test/.keep

curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -o .gitignore

pipenv install --dev pytest
pipenv install --dev --trusted-host pypi.python.org pytest


problem on MACos
----------------

    export LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8
https://stackoverflow.com/questions/14102416/python-requests-requests-exceptions-sslerror-errno-8-ssl-c504-eof-occurred

export SERVER_IP=127.0.0.1

pipenv install --dev pytest-mock



psql postgres://cecum:password@172.18.0.3:5432/sample -c "SELECT count(id) FROM employees;"
pg_dump postgres://cecum:password@172.18.0.3:5432/sample


pip install --user awscli
~/.local/bin/aws --version
chmod +x ~/.local/bin/aws
export PATH=~/.local/bin:$PATH
aws --version

---OTROS-----
export PATH="$HOME/.local/bin:$PATH"
pipenv shell --fancy
---------------
