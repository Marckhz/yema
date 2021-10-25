FROM python:3.9.7-bullseye


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /myapp
WORKDIR /myapp
COPY . /myapp/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
