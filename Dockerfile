FROM python:3.12-slim

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE ${SERVICE_PORT}
