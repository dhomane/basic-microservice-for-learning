FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 7502

CMD [ "python", "/app/database.py"]