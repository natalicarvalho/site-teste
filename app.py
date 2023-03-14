from flask import Flask

app = Flask(__name__)

menu = """
<a href="/">Página inicial</a> | <a href="/sobre">sobre</a> | <a href="/contato">contato</a>
<br>
"""

@app.route("/")
def hello_world():
  return "Olá, mundo! Esse é meu site. (Natali Carvalho)"

@app.route("/sobre")
def sobre():
  return "aqui vai o conteúdo da página sobre"

@app.route("/contato")
def contato():
  return "aqui vai o conteúdo da página contato"
