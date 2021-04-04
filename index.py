#!/usr/bin/env python3

from collections import OrderedDict
import flask
from flask import Flask, request, Response, jsonify, render_template 
import urllib.parse
import requests
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config['DEBUG'] = False
port = 83

CORS(app, resources=r'/api/*')
@app.route('/', methods=['get'])
def index():

    # -----------------------------------------------
    # Welcome
    # -----------------------------------------------
    return jsonify({"mensagem": "Acesso via /api/geoip?ip=177.79.48.86"})

@app.route('/api/geoip', methods=['GET'])
def autocomplete():

    # -----------------------------------------------
    # Example request GET
    # /geoip?ip=177.79.48.86
    # -----------------------------------------------

    ip = urllib.parse.quote(request.args['ip']) #""
    url = "https://ipinfo.io/"+ip+"/json"
    response = requests.get(url)

    return Response(response)  

app.run(host="0.0.0.0", port=port)