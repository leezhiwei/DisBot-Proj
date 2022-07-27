from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "Spot the difference key: {} \nMystery Box key: {}".format(ke2,ke) 

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive(k,k2):
    global ke
    global ke2
    ke = k
    ke2 = k2
    t = Thread(target=run) 
    t.start()