# list of instructions on how to build a container
FROM ubuntu:18.04

# who is maintainer of the project
MAINTAINER gauravk1994@gmail.com

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
RUN apt-get install mysql-server -y

COPY requirements.txt /deploymentProject/requirements.txt

# working directory of the application in docker container
WORKDIR /deploymentProject

RUN pip3 install -r requirements.txt

COPY . /deploymentProject

CMD gunicorn -w 4 --bind 0.0.0.0:5000 wsgi:app