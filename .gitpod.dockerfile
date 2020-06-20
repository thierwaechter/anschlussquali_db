FROM python:latest

RUN apt-get update -y

WORKDIR /MyFlask

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["/workspace/MyFlask/app.py"]
