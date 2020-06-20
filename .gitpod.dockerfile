FROM python:latest

RUN apt-get update -y

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["python2, "app.py"]
#  python3 manage.py runserver 0.0.0.0:8080
