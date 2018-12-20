from flask import Flask, render_template, request
import requests as rq

app=Flask(__name__)

#Telegram
key="환경변수에서"

my_id="환경변수에서"
send_url="https://api.telegram.org/" # Origin address
hphk_url="https://api.hphk.io/telegram/" ### hphk 우회 주소.
send_url2="bot{}/sendMessage?chat_id={}&text={}"

#
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sendmsg")
def sendmsg():
    msg=request.args.get("msg") #보낸 박스의 이름
    #telegram에 메세지 보내기
    # 1. chatbot의 key값을 받아서 저장한다.
    # 2. key/token 값을 통해서 /getMe (나(봇)에 대한 정보) /getUpdates (봇에 대한 상태 정보)
    # 3. 
    url=hphk_url+send_url2.format(key,my_id,msg)
    rq.get(url)
    return render_template("sendmsg.html",msg=msg)
# 
@app.route("/fakesearch")
def fakesearch():
    return render_template("fakesearch.html")
