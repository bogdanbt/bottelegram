import json
import telebot
import requests
from flask import Flask, request, jsonify


app = Flask(__name__)

CHAT_ID='425745139'
BOTTOKEN='5545278299:AAHIqGnUM6mrgB0fe8DWsUMZrrpDU1BQ8jI'
bot=telebot.TeleBot(BOTTOKEN)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/test")
def hello_worldtest():
    return "<p>Hello, World!</p>"

@app.route("/webhook",methods=['POST'])

def webhook():
    data=json.loads(request.data)
    symbol=data['symbol']
    url='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols+'USDT'+'&period=5m&limit=1'
    data=requests.get(url).json()
    Vol=round(float(data[1]['buyVol']),0)+round(float(data[1]['sellVol']),0)
    last=round(float(data[0]['buyVol']),0)+round(float(data[0]['sellVol']),0)
    text=symbols+'signal'+Vol
    bot.send_message(CHAT_ID, text)
    return{"signal":"success"}


    #return{"signal":"success"}

if __name__ == 'main':
    app.run()


#   https://telebotbogdan.herokuapp.com/webhook
#   {"symbol":"Test","usdt":"5","signal":"list1"}
