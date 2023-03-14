from flask import Flask

app = Flask(__name__)

menu = """
<a href="/">Página inicial</a> | <a href="/musica">Música</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def hello_world():
  return menu + "Olá, mundo! Esse é meu site. (Natali Carvalho)"

@app.route("/sobre")
def sobre():
  return menu + "aqui vai o conteúdo da página Sobre"

@app.route("/contato")
def contato():
  <font color="red">Contato</font>
  return menu + "aqui vai o conteúdo da página Contato"


