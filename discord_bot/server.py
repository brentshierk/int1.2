from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')

def home():
    return 'bot currently running'

def run():
    app.run(host='0.0.0.0',port=8008)

def hosting():
    t = Thread(target=run)
    t.start()
