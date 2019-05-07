FROM python:3.7-alpine3.8
# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories
# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver
# install selenium
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./webplayground /code/
#RUN python manage.py makemigrations
#RUN python manage.py migrate
CMD gunicorn webplayground.wsgi -b 0.0.0.0:8000
