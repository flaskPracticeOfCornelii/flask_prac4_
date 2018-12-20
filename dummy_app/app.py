from flask import Flask, send_file, render_template
import random
import requests as rq
from bs4 import BeautifulSoup as bs
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/cornel")
def cornel():
    return "My Korean name is JiMyeong Son"

# /hi/john => "hello john"
# /hi/ashley => "hello ashley"
@app.route("/hi/<name>")
def hi(name):
    return "Hello "+name
    
# /cube/2 ==> 8
# /cube/3 ==> 27
@app.route("/cube/<int:num>")
def cube(num):
    return "{}".format(num**3)
#*Tip: 문자로 넘겨 받고, 문자로 넘겨줘야 함.

# /reverse/hello => olleh
@app.route("/reverse/<name>")
def reverse(name):
    a=list(name)
    a.reverse()
    result="".join(a)
    return result
    
## lecturer
# @app.route("/reverse/<param>")
# def reverse(param):
#     return param[::-1]
    
# /palindrome/racecar ==> true
# /palindrome/hello   ==> false
@app.route("/palindrome/<param>")
def palindrome(param):
    return str(param==param[::-1])

@app.route("/profile")
def profile():
    return send_file('profile.html')

## 웹으로 로또 번호 추첨해서 보여주기
@app.route("/lotto")
def lotto():
    name="Jimyeong Son"
    num=random.sample(list(range(1,46)),6)
    result=str(sorted(num))
    return render_template("lotto.html",result_lotto=result,name=name)
    
## 코스피 지수 뽑아서 웹으로 넣어주기
url="https://finance.naver.com/sise/"
@app.route("/kospi")
def kospi():
    res=rq.get(url)
    doc=bs(res.text,"html.parser")
    result=doc.select_one("#KOSPI_now")
    name="JiMyeong"
    
    return render_template("kospi.html",kospi=result.text,name=name)

## google에 spiderman new universe 검색하면 나오는 검색 수 긁어서 보내주기
target_url="https://www.google.com/search?q=spiderman+new+universe"
@app.route("/spiderman")
def spiderman():
    res=rq.get(target_url)
    doc=bs(res.text,"html.parser")
    result=doc.select_one("#resultStats").text
    
    return render_template("attempts.html",search_num=result)

###datetime
@app.route("/newyear")
def newyear():
    a=date.today()
    mon=a.month
    day=a.day
    return render_template("newyear.html",mon=mon,day=day)
    