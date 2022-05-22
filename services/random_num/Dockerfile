FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 7500

CMD [ "python", "/app/random_num.py"]