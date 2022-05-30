# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /hacker-view

COPY requirements.txt requirements.txt
COPY requirements/base.txt requirements/base.txt
COPY requirements/test.txt requirements/test.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "application", "run", "--host=0.0.0.0"]