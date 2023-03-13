from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello world():
  return "olá mundo, este é meu site! (Natali Carvalho)" 
