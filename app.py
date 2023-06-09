import os

import gspread
import requests
from flask import Flask, request
from oauth2client.service_account import ServiceAccountCredentials
from tchan import ChannelScraper

from raspador import ultimas_promocoes


TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key("12uxnR1XPG3qExbp8YoCsmIDaI7i9DMNCU0XGdDNdVYY")
sheet = planilha.worksheet("teste")
app = Flask(__name__)
    
menu = """
<a href="/">Página inicial</a> | <a href="/promocoes">PROMOÇÕES</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def index():
  return menu + "Olá, mundo! Esse é o site da Natali Carvalho"

@app.route("/sobre")
def sobre():
  return menu + "Sou uma jornalista cearense formada pela Universidade Federal do Ceará"

@app.route("/contato")
def contato():
  return menu + "O meu email é natali.lima.carvalho@gmail.com"


@app.route("/promocoes")
def promocoes():
  conteudo = menu + """
  Encontrei as seguintes promoções no <a href="https://t.me/promocoeseachadinhos">@promocoeseachadinhos</a>:
  <br>
  <ul>
  """
  for promocao in ultimas_promocoes():
    conteudo += f"<li>{promocao}</li>"
  return conteudo + "</ul>"


@app.route("/promocoes2")
def promocoes2():
  conteudo = menu + """
  Encontrei as seguintes promoções no <a href="https://t.me/promocoeseachadinhos">@promocoeseachadinhos</a>:
  <br>
  <ul>
  """
  scraper = ChannelScraper()
  contador = 0
  for message in scraper.messages("promocoeseachadinhos"):
    contador += 1
    texto = message.text.strip().splitlines()[0]
    conteudo += f"<li>{message.created_at} {texto}</li>"
    if contador == 10:
      break
  return conteudo + "</ul>"

@app.route("/dedoduro")
def dedoduro():
  mensagem = {"chat_id": TELEGRAM_ADMIN_ID, "text": "Alguém acessou a página dedo duro!"}
  resposta = requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage", data=mensagem)
  return f"Mensagem enviada. Resposta ({resposta.status_code}): {resposta.text}"


@app.route("/dedoduro2")
def dedoduro2():
  sheet.append_row(["Natali", "Carvalho", "a partir do Flask"])
  return "Planilha escrita!"


@app.route("/telegram-bot", methods=["POST"])
def telegram_bot():
  update = request.json
  chat_id = update["message"]["chat"]["id"]
  message = update["message"]["text"]
  nova_mensagem = {
    "chat_id": chat_id,
    "text": f"Você enviou a mensagem: <b>{message}</b>",
    "parse_mode": "HTML",
  }
  resposta = requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=nova_mensagem)
  print(resposta.text)
  return "ok"


def enviar_foto():
  # Esboço
  ...
  chart.save("chart.png")
  with open("chart.png", mode="rb") as arquivo:
    conteudo = arquivo.read()
  mensagem = {"chat_id": ..., "caption": "gráfico X"}
  files = {"photo": ("grafico.png", conteudo)}
  resposta = requests.post(
    f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendPhoto", 
    data=mensagem, 
    files=files,
  )
