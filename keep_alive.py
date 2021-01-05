from flask import Flask, render_template
from threading import Thread

app = Flask('__name__')

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()