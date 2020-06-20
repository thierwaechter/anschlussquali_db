FROM python:latest

RUN apt-get update -y

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["/usr/local/bin/python", "/workspace/MyFlask/app.py"]
