FROM python:latest

RUN apt-get update -y

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["/workspace/MyFlask/app.py"]
