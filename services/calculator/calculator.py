#!/usr/bin/env python
# 
from flask import Flask, request, jsonify, Response
from prometheus_client import Summary, generate_latest
import random, requests, json, os

svc_randomnum_host = str(os.environ['RANDOMNUM_HOST'])
svc_randomnum_port = str(os.environ['RANDOMNUM_PORT'])
svc_database_host = str(os.environ['DATABASE_HOST'])
svc_database_port = str(os.environ['DATABASE_PORT'])

uri = "http://" + svc_randomnum_host + ":" + svc_randomnum_port + "/random"
db_uri = "http://" + svc_database_host + ":" + svc_database_port + "/entries"

def get_number():
  try:
    r = requests.get(uri)
  except:
    r = "Unable to connect to Random number service"
  return r

def commit_to_db(number, result):
  try:
    r = requests.post(db_uri, json={ "number":number, "result":result })
  except:
    r = "Database Connection failed"
  return r

# Prometheus Metrics
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds','Time spent processing request')
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

app = Flask(__name__)

@app.route('/calc')
@REQUEST_TIME.time()
def add():
  data = get_number()
  if data=="Unable to connect to Random number service":
    result=data
    return jsonify(error=result)
  else:
    num = data.json()
    result = num + num
    commit = commit_to_db(num,result)
    commit_msg = ""
    if commit=="Database Connection failed":
      commit_msg="Database Connection failed"
    else:
      commit_msg=commit.status_code
    return jsonify(input=num, output=result, db_response=commit_msg)

@app.route('/metrics')
def metrics():
  return Response(generate_latest(registry=REQUEST_TIME), mimetype=CONTENT_TYPE_LATEST)

if __name__=="__main__":
  app.run(host="0.0.0.0", port=7501, debug=True)