docker create --name tm-db -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=db -p 5432:5432 postgres:alpine
manage.py makemigrations
manage.py migrate
manage.py runserver