pgbackup
========

CLI for backing up remote PostgesSLQ data bases localy or to AWS S3

Preparing for Development
-------------------------

1. Ensure ``pip``, and ``pipenv`` are installed
2. Clone the repository: ``git clone git@github.com....``
3. Fetch Development dependencies: ``make install``

Usage
-----

Pass in full database URL, the storage drive, and destination

S3 example w/ bucket name:

::
    $ pgbackup postgres://bog@example.com:5432/bn_one --drive s3 backups

Local example w/ local path

::
  $ pgbackup postgres://bog@example.com:5432/bn_one --drive local /var/local/db_one/backups/dump.sql

Running test
------------

Run test locally using ``make`` if virtualenv is active:

:: 
    $ make

if virtualenv innot active the use:

::
    $ pipenv run make

