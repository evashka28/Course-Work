from django.http import HttpResponse
from django.shortcuts import render
import json

with open("ladozh.json", "r", encoding='utf-8') as file:
 text = file.read()
 file.close()
 data = json.loads(text)

with open("moskovskii.json", "r", encoding='utf-8') as file:
  text = file.read()
  file.close()
  data1 = json.loads(text)

with open("users.json", "r", encoding='utf-8') as file:
 text = file.read()
 file.close()
 data2 = json.loads(text)

with open("nowuser.json", "r", encoding='utf-8') as file:
 text = file.read()
 file.close()
 data3 = json.loads(text)

status = data3["user"]["status"]
log = data3["user"]["login"]


def save_data():
 dataFile = open(r"ladozh.json", "w", encoding="utf8")
 dataFile.write(json.dumps(data, ensure_ascii=False))
 dataFile.close()


def save_data1():
 dataFile = open(r"moskovskii.json", "w", encoding="utf8")
 dataFile.write(json.dumps(data1, ensure_ascii=False))
 dataFile.close()

def save_data2():
 dataFile = open(r"users.json", "w", encoding="utf8")
 dataFile.write(json.dumps(data2, ensure_ascii=False))
 dataFile.close()

def save_data3():
 dataFile = open(r"nowuser.json", "w", encoding="utf8")
 dataFile.write(json.dumps(data3, ensure_ascii=False))
 dataFile.close()



def index(request):
 with open("nowuser.json", "r", encoding="utf8") as file:
  text = json.loads(file.read())
 req = request.GET
 session = {}
 session["user"] = text["user"]
 if req.get("exit") == "Выход":
  data3["user"]["check"] = "false"
  data3["user"]["login"] = None
  data3["user"]["password"] = None
  data3["user"]["name"] = None
  data3["user"]["surname"] = None
  data3["user"]["status"] = None
  save_data3()
 return  render(request, 'home.html', session)




def ladozhRender(request):
 with open("ladozh.json", "r", encoding="utf8") as file:
  text = json.loads(file.read())

 req = request.GET
 for j in data["отправление"]:
    if req.get("номер") == j["номер"]:
        data["отправление"].remove(j)
 for j in data["прибытие"]:
    if req.get("номер") == j["номер"]:
        data["прибытие"].remove(j)
 save_data()

 with open("nowuser.json", "r", encoding="utf8") as file:
  text1 = json.loads(file.read())
 req = request.GET
 session = {}
 session["user"] = text1["user"]
 if req.get("exit") == "Выход":
  data3["user"]["check"] = "false"
  data3["user"]["login"] = None
  data3["user"]["password"] = None
  data3["user"]["name"] = None
  data3["user"]["surname"] = None
  data3["user"]["status"] = None
  save_data3()

 session['otpr'] = []
 for i in range(0, len(text["отправление"])):
       session['otpr'].append(text["отправление"][i])

 session['prib'] = []
 for i in range(0, len(text["прибытие"])):
       session['prib'].append(text["прибытие"][i])
 return render(request, 'ladozh.html', session)






def moskRender(request):
 with open("moskovskii.json", "r", encoding="utf8") as file:
  text = json.loads(file.read())

 req = request.GET
 for j in data1["отправление"]:
    if req.get("номер") == j["номер"]:
        data1["отправление"].remove(j)
 for j in data1["прибытие"]:
    if req.get("номер") == j["номер"]:
        data1["прибытие"].remove(j)
 save_data1()

 with open("nowuser.json", "r", encoding="utf8") as file:
  text1 = json.loads(file.read())
 req = request.GET
 session = {}
 session["user"] = text1["user"]
 if req.get("exit") == "Выход":
  data3["user"]["check"] = "false"
  data3["user"]["login"] = None
  data3["user"]["password"] = None
  data3["user"]["name"] = None
  data3["user"]["surname"] = None
  data3["user"]["status"] = None
  save_data3()

 session['otpr'] = []
 for i in range(0, len(text["отправление"])):
       session['otpr'].append(text["отправление"][i])

 session['prib'] = []
 for i in range(0, len(text["прибытие"])):
       session['prib'].append(text["прибытие"][i])
 return render(request, 'mosk.html', session)






def trainViewRender(request, id):
 with open("ladozh.json", "r", encoding="utf8") as file:
  text = json.loads(file.read())

  req = request.GET
  session = {}
  session["error"] = None
  for j in data["отправление"]:
   if j["id"] == id:
    if (req.get("номер")!=None)and (req.get("номер")!=""):j["номер"] = req.get("номер")
    if (req.get("модель")!=None)and (req.get("модель")!=""):j["модель"] = req.get("модель")
    if (req.get("направление")!=None)and (req.get("направление")!=""):j["направление"] = req.get("направление")
    if (req.get("ВремяО")!=None)and (req.get("ВремяО")!=""):j["времяО"] = req.get("ВремяО")
    if (req.get("оценка")!=None)and (req.get("оценка")!=""):j["оценка"] = req.get("оценка")
    if (req.get("класс")!=None)and (req.get("класс")!=""):j["класс"] = req.get("класс")
    if (req.get("оценка1") != None) and (req.get("оценка1") != "") and (int(req.get("оценка1")) <= 10):
     j["оценка"] = int((int(str(req.get("оценка1"))) + int(j["оценка"])) / 2)
    elif (req.get("оценка1") == None) or (req.get("оценка1") == ""):session["error"] = None
    else:
     session["error"] = "ошибка ввода"

  for j in data["прибытие"]:
   if j["id"] == id:
    if (req.get("номер")!=None)and (req.get("номер")!=""):j["номер"] = req.get("номер")
    if (req.get("модель")!=None)and (req.get("модель")!=""):j["модель"] = req.get("модель")
    if (req.get("направление")!=None)and (req.get("направление")!=""):j["направление"] = req.get("направление")
    if (req.get("ВремяП")!=None)and (req.get("ВремяП")!=""):j["времяП"] = req.get("ВремяП")
    if (req.get("оценка")!=None)and (req.get("оценка")!=""):j["оценка"] = req.get("оценка")
    if (req.get("класс")!=None)and (req.get("класс")!=""):j["класс"] = req.get("класс")
    if (req.get("оценка1") != None) and (req.get("оценка1") != "") and (int(req.get("оценка1")) <= 10): j["оценка"] = (int(str(req.get("оценка1")))+int(j["оценка"]))/2
    else: session["error"]="ошибка ввода"
  save_data()

  with open("nowuser.json", "r", encoding="utf8") as file:
   text1 = json.loads(file.read())
  req = request.GET

  session["user"] = text1["user"]
  if req.get("exit") == "Выход":
   data3["user"]["check"] = "false"
   data3["user"]["login"] = None
   data3["user"]["password"] = None
   data3["user"]["name"] = None
   data3["user"]["surname"] = None
   data3["user"]["status"] = None
   save_data3()

  for i in text["отправление"]:
   if i["id"]==id:
    session["номер"] = i["номер"]
    session["оценка"] = i["оценка"]
    session["модель"] = i["модель"]
    session["класс"] = i["класс"]
    session["направление"] = i["направление"]
    session['маршрут'] = []
    for j in range(0, len(i["маршрут"])):
       session['маршрут'].append(i["маршрут"][j])

  for i in text["прибытие"]:
   if i["id"] == id:
    session["номер"] = i["номер"]
    session["направление"] = i["направление"]
    session["оценка"] = i["оценка"]
    session["модель"] = i["модель"]
    session["класс"] = i["класс"]
    session['маршрут'] = []
    for j in range(0, len(i["маршрут"])):
     session['маршрут'].append(i["маршрут"][j])
 return render(request, 'ladozh-train.html', session)









def train1ViewRender(request, id):
 with open("moskovskii.json", "r", encoding="utf8") as file:
  text = json.loads(file.read())

  req = request.GET
  session = {}
  session["error"] = None
  for j in data1["отправление"]:
   if j["id"] == id:
    if (req.get("номер")!=None)and (req.get("номер")!=""):j["номер"] = req.get("номер")
    if (req.get("модель")!=None)and (req.get("модель")!=""):j["модель"] = req.get("модель")
    if (req.get("направление")!=None)and (req.get("направление")!=""):j["направление"] = req.get("направление")
    if (req.get("ВремяО")!=None)and (req.get("ВремяО")!=""):j["времяО"] = req.get("ВремяО")
    if (req.get("оценка")!=None)and (req.get("оценка")!=""):j["оценка"] = req.get("оценка")
    if (req.get("класс")!=None)and (req.get("класс")!=""):j["класс"] = req.get("класс")
    if (req.get("оценка1") != None) and (req.get("оценка1") != "") and (int(req.get("оценка1")) <= 10):
     j["оценка"] = int((int(str(req.get("оценка1"))) + int(j["оценка"])) / 2)
    elif (req.get("оценка1") == None) or (req.get("оценка1") == ""):session["error"] = None
    else:
     session["error"] = "ошибка ввода"


  for j in data1["прибытие"]:
   if j["id"] == id:
    if (req.get("номер")!=None)and (req.get("номер")!=""):j["номер"] = req.get("номер")
    if (req.get("модель")!=None)and (req.get("модель")!=""):j["модель"] = req.get("модель")
    if (req.get("направление")!=None)and (req.get("направление")!=""):j["направление"] = req.get("направление")
    if (req.get("ВремяП")!=None)and (req.get("ВремяП")!=""):j["времяП"] = req.get("ВремяП")
    if (req.get("оценка")!=None)and (req.get("оценка")!=""):j["оценка"] = req.get("оценка")
    if (req.get("класс")!=None)and (req.get("класс")!=""):j["класс"] = req.get("класс")
    if (req.get("оценка1") != None) and (req.get("оценка1") != "") and (int(str(req.get("оценка1"))) <= 10): j["оценка"] = (int(str(req.get("оценка1")))+int(j["оценка"]))/2
    else: session["error"]="ошибка ввода"
  save_data1()

  with open("nowuser.json", "r", encoding="utf8") as file:
   text1 = json.loads(file.read())
  req = request.GET

  session["user"] = text1["user"]
  if req.get("exit") == "Выход":
   data3["user"]["check"] = "false"
   data3["user"]["login"] = None
   data3["user"]["password"] = None
   data3["user"]["name"] = None
   data3["user"]["surname"] = None
   data3["user"]["status"] = None
   save_data3()

  for i in text["отправление"]:
   if i["id"]==id:
    session["номер"] = i["номер"]
    session["оценка"] = i["оценка"]
    session["модель"] = i["модель"]
    session["класс"] = i["класс"]
    session["направление"] = i["направление"]
    session['маршрут'] = []
    for j in range(0, len(i["маршрут"])):
       session['маршрут'].append(i["маршрут"][j])

  for i in text["прибытие"]:
   if i["id"] == id:
    session["номер"] = i["номер"]
    session["направление"] = i["направление"]
    session["оценка"] = i["оценка"]
    session["модель"] = i["модель"]
    session["класс"] = i["класс"]
    session['маршрут'] = []
    for j in range(0, len(i["маршрут"])):
     session['маршрут'].append(i["маршрут"][j])
 return render(request, 'mosk-train.html', session)


def vhodRender(request):
 req = request.GET
 session = {}
 session["error"] = ""
 session["result"] = data3["user"]["check"]
 for i in data2["users"]:
  if i["login"] == req.get("login"):
   if i["password"] == req.get("password"):
    data3["user"] = i
    session["login"] = i["login"]
    session["password"] = i["password"]
    session["result"] = data3["user"]["check"]
    save_data3()
   elif (req.get("login") != None) and (req.get("login") != "") and (i["login"] != req.get("login"))and (i["password"] != req.get("password")) :
    session["error"] = "Ошибка ввода"



 return render(request, "vhod.html", session)








def polzRender(request):
 with open("users.json", "r", encoding="utf8") as file:
  text = json.loads(file.read())

  req = request.GET
  for j in data2["users"]:
   if j["login"] == req.get("login"):
    if (req.get("status")!=None)and (req.get("status")!=""):j["status"] = req.get("status")
  save_data2()

  with open("nowuser.json", "r", encoding="utf8") as file:
   text1 = json.loads(file.read())
  req = request.GET
  session = {}
  session["user"] = text1["user"]
  if req.get("exit") == "Выход":
   data3["user"]["check"] = "false"
   data3["user"]["login"] = None
   data3["user"]["password"] = None
   data3["user"]["name"] = None
   data3["user"]["surname"] = None
   data3["user"]["status"] = None
   save_data3()

  session['users'] = []
  for j in range(0, len(text["users"])):
       session['users'].append(text["users"][j])


 return render(request, 'admin.html', session)


def Regist(request):
 req = request.GET
 org = {}
 error = {}
 k=data2["users"][0]
 for i in data2["users"]:
  if (req.get("login") == i["login"]) and (req.get("login") != None) and (req.get("login") != ""):
   error["error"] = "Такой логин уже зарегестрирован"
   k=i
 if (req.get("login") != k["login"]) and (req.get("login") != None) and (req.get("login") != ""):
  if (req.get("password") == req.get("password2")) and (req.get("password") != None) and (req.get("password") != ""):
   org["check"] = "true"
   org["login"] = req.get("login")
   org["name"] = req.get("name")
   org["surname"] = req.get("sername")
   org["status"] = "user"
   org["password"] = req.get("password")
   error["error"] = "Регистрация пройдена. Войдите!"
   data2["users"].append(org)
   save_data2()
  elif (req.get("password") != req.get("password2")) and (req.get("password") != None) and (req.get("password") != ""):
    error["error"] = "Пароли не сопрадают! Попробуйте еще раз!"

 with open("nowuser.json", "r", encoding="utf8") as file:
   text1 = json.loads(file.read())

 error["user"] = text1["user"]

 return render(request, "registr.html", error)
