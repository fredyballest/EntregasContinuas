FROM python:3.7-alpine3.8
# update apk repo

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./webplayground /code/

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

#RUN python manage.py makemigrations
#RUN python manage.py migrate
CMD gunicorn webplayground.wsgi -b 0.0.0.0:8000
