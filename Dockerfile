FROM python:3.7-slim

WORKDIR /deploymentProject

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn -w 2 --bind 0.0.0.0:5000 wsgi:app