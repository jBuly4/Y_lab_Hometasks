FROM python:3.10
MAINTAINER jBuly4

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y sudo vim && apt-get upgrade -y

COPY ./requierments.txt /requirements.txt
RUN pip install --upgrade pip -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./recepie_book /app

RUN adduser --disabled-password --gecos '' python
RUN adduser python sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER python