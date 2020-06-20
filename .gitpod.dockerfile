FROM python:latest

RUN apt-get update -y
ENV FLASK_APP run.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["flask", "run"]
