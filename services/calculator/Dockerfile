FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 7501

CMD [ "python", "/app/calculator.py"]