from flask import Flask,request
import xml.etree.ElementTree as ET
from flask import  make_response
# from my_sqlite import *
from reply_template import *
from my_mysql import *
app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():
    if request.method == 'GET':
        if request.args.get('echostr'):
            return request.args.get('echostr')
        else:
            return 'ok'

    if request.method == 'POST':
        xml = ET.fromstring(request.data)
        ToUserName = xml.find('ToUserName').text    #开发者微信号
        FromUserName = xml.find('FromUserName').text    #发送方帐号（一个OpenID）
        CreateTime = xml.find('CreateTime').text    #消息创建时间 （整型）
        MsgType = xml.find("MsgType").text  #text
        Content = xml.find("Content").text  #	文本消息内容
        MsgId = xml.find("MsgId").text  #	消息id，64位整型
        # print(ToUserName)
        # print(FromUserName)
        # print('消息创建时间：%s' %CreateTime)
        # print(MsgType)
        # print(Content)
        # print(MsgId)

        if MsgType == 'text':

            content = get_data(Content)
            return reply_text(FromUserName, ToUserName, content)
        else:
            return reply_text(FromUserName, ToUserName, "嗯？我听不太懂")

def handler(environ, start_response):
    return app(environ, start_response)

