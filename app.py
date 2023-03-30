from flask import Flask
from tchan import channelScraper

app = Flask(__name__)

def ultimas_promocoes():
  scraper = channelScraper()
  contador = 0
  resultado = []
  for message in scraper.messages("promocoeseachadinhos")
  contador += 1
  texto = message.text.strip().splitlines
  resultado.append(f"{message.created_at} {texto}")
  if contador == 10:
    return resultado

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

@app.rout("/promocoes")
def promocoes():
   conteudo = menu + """
   Encontrei as seguintes promoções no <a href="https://t.me/promocoeseachadinhos".@promocoeseachadinhos</a>
   <br>
   <ul>
   """
   for promocao in ultimas_promocoes():
     conteudo += f"<li>(promocao}</li>"
   return conteudo + "</ul>"
