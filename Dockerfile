FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

EXPOSE 80

ENV NAME World

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
