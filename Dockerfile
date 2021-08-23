# list of instructions on how to build a container
FROM python:3.7-slim

# who is maintainer of the project
MAINTAINER gauravk1994@gmail.com

# working directory of the application in docker container
WORKDIR /deploymentProject

COPY . /deploymentProject

RUN pip install -r requirements.txt

CMD gunicorn -w 2 --bind 0.0.0.0:5000 wsgi:app