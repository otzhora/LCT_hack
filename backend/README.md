postgres

    sudo apt-get update
    sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

создаем базу данных db_django и пользователя db_admin с паролем admin

sudo -u postgres psql

	CREATE DATABASE db_django;

	CREATE USER db_admin WITH PASSWORD 'admin';

	ALTER ROLE db_admin SET client_encoding TO 'utf8';
	ALTER ROLE db_admin SET default_transaction_isolation TO 'read committed';
	ALTER ROLE db_admin SET timezone TO 'UTC';

	GRANT ALL PRIVILEGES ON DATABASE db_django TO db_admin;

	\q

далее создаем файл в backend/django_project/django_progect private_settings.py
и в ней пишем:

    DB_NAME = 'db_django'
    DB_USER = 'db_admin'
    DB_PASSWORD = 'admin'

далее в консоле находясь в окружении прописываем:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
