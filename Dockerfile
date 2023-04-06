# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "gunicorn", "app:app" , "-c", "gunicorn.conf.py" ]
