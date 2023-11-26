FROM python:3.12.0

RUN mkdir -p /usr/src/xyz
WORKDIR /usr/src/xyz

ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .