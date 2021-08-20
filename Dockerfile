# list of instructions on how to build a container
FROM python:3.7-slim

# name of the application in the docker container and its working directory
WORKDIR /deploymentProject

RUN cd /deploymentProject

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn -w 2 --bind 0.0.0.0:5000 wsgi:app