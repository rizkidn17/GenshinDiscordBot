from flask import Flask
from threading import Thread
import requests
import json


response = requests.get('https://api.genshin.dev/characters/albedo').text
response_info = json.loads(response)

app = Flask('')

@app.route('/')
def home():
    return response_info
    # return "Hello. I am alive!"
    # people = [{'name': 'Alice', 'birth-year': 1986},
    #       {'name': 'Bob', 'birth-year': 1985}]
    # return jsonify(people) 

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()