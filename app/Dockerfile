FROM python:3.7

EXPOSE 5000

WORKDIR /app

RUN apt-get update && apt-get -y install cron && apt-get -y install nano

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT python app.py && /bin/bash