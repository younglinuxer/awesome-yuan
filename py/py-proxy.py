#!/usr/bin/env python
#-- coding:utf8 --
from flask import Flask,request,redirect,Response
import requests
app = Flask(__name__)
BASE_NAME='http://127.0.0.1:81/'
SITE_NAME = 'https://www.json.cn/json/jsononline.html'
@app.route('/')
def index():
    return 'Flask is running!'
@app.route('/<path:path>',methods=['GET','POST',"DELETE"])
def proxy(path):
    global SITE_NAME
    url = SITE_NAME + path
    if request.method=='GET':
        resp = requests.get(url=url)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        print headers
        # response = Response(resp.content.replace('href="https://www.json.cn','href="http://127.0.0.1:82'), resp.status_code, headers)
        response = Response(resp.content, resp.status_code, headers)
        # response = Response(resp.content.replace(SITE_NAME,BASE_NAME), resp.status_code, headers)
        return response
    elif request.method=='POST':
        resp = requests.post(url=url, json=request.get_json())
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=='DELETE':
        resp = requests.delete(url=url).content
        # response = Response(resp.content, resp.status_code, headers)
        response = Response(resp.content, resp.status_code)
        return response

if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0',port=82)