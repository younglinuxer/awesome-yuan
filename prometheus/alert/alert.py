#! /usr/bin/env python2
# encoding:utf-8
import json,sys
import requests
from flask import Flask,render_template,request
reload(sys)
sys.setdefaultencoding( "utf-8" )
app = Flask(__name__)

def send_sms(content):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send"
    querystring = {"key": "d26f364a-b9ec-48cd-9f2d-8a50b708eaab"}
    payload = '{"msgtype": "text","text": {"content": "%s","mentioned_list":["wangqing","@benyang.yuan@seaboxdata.com"]}}' % content
    print(payload)
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "c31e863f-3b41-a98d-6696-a8fe0e19d88b"
    }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)


@app.route('/send', methods=['POST'])#api定义，返回给短信程序
def register():
    data = json.loads(request.data)
    print(data)
    content_text = data["alerts"][0]["annotations"]["summary"]
    # content_text = data["alerts"]
    print(content_text)
    send_sms(content=content_text)
    return "发送成功"

if __name__ == '__main__':app.run(host='0.0.0.0',port=39092)
