FROM python:3.9-alpine

WORKDIR /taskmanager

COPY requirements.txt /taskmanager/

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . /taskmanager/

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE taskmanager.settings

EXPOSE 8000