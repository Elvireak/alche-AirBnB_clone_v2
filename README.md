# AirBnB Clone - MySQL

## Description

This project is the second version of the AirBnB clone. It builds on the
command interpreter from the first version and adds a MySQL database.
The same code can work with two storage types: file storage (JSON) and
database storage (MySQL with SQLAlchemy).

## Environment variables

| Variable | Meaning |
|----------|---------|
| HBNB_ENV | Running environment: `dev` or `test` |
| HBNB_MYSQL_USER | MySQL username |
| HBNB_MYSQL_PWD | MySQL password |
| HBNB_MYSQL_HOST | MySQL hostname |
| HBNB_MYSQL_DB | MySQL database name |
| HBNB_TYPE_STORAGE | Storage type: `file` or `db` |

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQL 8.0
- SQLAlchemy 1.4.x
- pycodestyle 2.7.*

## How to run

Run the console in interactive mode:

    $ ./console.py
    (hbnb) help

Run the tests:

    $ python3 -m unittest discover tests

Use database storage:

    $ HBNB_ENV=dev HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd \
      HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db \
      HBNB_TYPE_STORAGE=db ./console.py

## Authors

- <Original author 1 from v1, keep this line>
- <Original author 2 from v1, keep this line>
- Elvire Akayezu
- Claire Uwineza
