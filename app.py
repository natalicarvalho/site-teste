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
  return menu + "aqui vai o conteúdo da página Contato"

@app.route("/musica")
def música():
  return menu + "faz assim, te dou meu telefone, você me diz seu nome e a gente então se vê"
