FROM python:3.7

RUN mkdir /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app