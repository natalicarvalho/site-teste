from flask import Flask

app = Flask(__name__)

menu = """
<a href="/">Página inicial</a> | <a href="/textos">Textos</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def hello_world():
  return menu + "Olá, mundo! Este é meu site. (Natali Carvalho)"

@app.route("/sobre")
def sobre():
  return menu + "Jornalista cearense"

@app.route("/contato")
def contato():
  return menu + "Natali Carvalho | (85) 99222-9958"

@app.route("/textos")
def textos():
  return menu + "O presidente Lula disse, em evento com lideranças indígenas em Roraima, que a escravidão trouxe uma coisa boa ao Brasil: a miscigenação. No Twitter, lembraram o presidente que essa mistura de raças aconteceu com muita violência e abusos e que não há nada de bom nisso."

