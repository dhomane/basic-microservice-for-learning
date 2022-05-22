#!/usr/bin/env python

from flask import Flask, request, jsonify, Response
from prometheus_client import Summary, generate_latest
import random

# Prometheus Metrics
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds','Time spent processing request')
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

app = Flask(__name__)

@app.route('/random')
@REQUEST_TIME.time()
def random_number():
    number = random.randint(1,100)
    return jsonify(number)

@app.route('/metrics')
def metrics():
  return Response(generate_latest(registry=REQUEST_TIME), mimetype=CONTENT_TYPE_LATEST)

if __name__=="__main__":
  app.run(host="0.0.0.0", port=7500, debug=True)