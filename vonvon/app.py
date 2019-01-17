from flask import Flask,render_template, request
import faker
import random
import csv
import json

app=Flask(__name__)
a=faker.Faker()

D={}# name matching
# '/':사용자의 이름을 입력 받습니다.
@app.route("/")
def index():
    return render_template("index_job_rec.html")

# '/job': 사용자에게 랜덤으로 생성된 직업 추천.
@app.route("/job")
def job():
    D={}
    try:
        with open("job_list.json","a",encoding="utf-8") as f:
            data=f.read()
            D=json.JSONDecoder().decode(data)
    except: 
        print("first registeration")
    name=request.args.get("name")
    if name in D:
        pass
    else:
        D[name]=a.job()
    with open("job_list.json","a",encoding="utf-8") as f:
        json_data=json.JSONEncoder().encode(D)
        f.write(json_data)
        
    return render_template("job.html",job=D[name])


@app.route("/dic")
def dic():
    dic=D
    return render_template("dic.html",dic=D)

@app.route("/compati")
def compati():
    return render_template("index.html")

@app.route("/match")
def match():
    # 1. fake 궁합을 알려주고,
    babo=request.args.get("babo")
    victim=request.args.get("victim")
    # 2. 우리만 알 수 있게 저장한다.
    # 3. fish 리스트에 append를 통해 저장한다.
    couple=[babo,victim]
    
    # xx님과 yy의 궁합은 88%입니다.
    if str(couple) in D:
        num=D[str(couple)]
    else:
        num=random.choice(range(10,100))
        D[str(couple)]=num
        with open("fish_list.csv","a",encoding="utf-8") as csvfile:
            writer=csv.writer(csvfile,delimiter=",")
            writer.writerow(couple)
            
    return render_template("match.html",babo=babo,victim=victim,num=num)

@app.route("/admin")
def admin():
    # 낚인 사람들의 명단
    # template에서 반복(for)을 써서, fish에 들어가 있는 데이터를 모두 보여준다.
    with open("fish_list.csv","r",encoding="utf-8") as csvfile:
        reader=csv.reader(csvfile,delimiter=",")
    
        return render_template("admin.html",fish=reader)
    
    