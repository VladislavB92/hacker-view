# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /hacker-view

COPY requirements/base.txt base.txt
COPY requirements/test.txt test.txt

RUN pip3 install -r base.txt -r test.txt

COPY . .

CMD [ "python3", "-m" , "application", "run", "--host=0.0.0.0"]