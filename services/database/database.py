#!/usr/bin/env python

from flask import Flask, request, jsonify, g, Response
from prometheus_client import Summary, generate_latest
import sqlite3

DATABASE = 'results.db'

app = Flask(__name__)


def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DATABASE)
    db.execute("CREATE TABLE if not exists entries ( number NUM, result NUM );")
  return db

# Prometheus Metrics
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds','Time spent processing request')
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()

@app.route('/entries', methods=['POST'])
@REQUEST_TIME.time()
def entries():
  content = request.json
  number = content['number']
  result = content['result']
  sql = "INSERT INTO entries (number, result) VALUES('%s','%s')" %(number, result)
  db = get_db()
  db.execute(sql)
  db.commit()
  return "commited"

@app.route('/metrics')
def metrics():
  return Response(generate_latest(registry=REQUEST_TIME), mimetype=CONTENT_TYPE_LATEST)

if __name__=="__main__":
  app.run(host="0.0.0.0", port=7502, debug=True)