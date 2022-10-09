import json
import telebot
import requests
from flask import Flask, request, jsonify
from binance.client import Client
from binance.enums import *
api_keys='MJXjYzcIxaPjYELP5L6DLieRDhtcPkQndqqIy0aILO6b1pCIWcavtTf82RbAoNxx'
api_secret='aDBRznWCHBQCzbALB3B1biPuyfuR9PDO2v9W03pJ8E2psO4fLDkvcBlWxIdB2NZq'
client=Client(api_key=api_keys, api_secret=api_secret,testnet=False)
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
    if data['signal']=="testmono":
        text=symbol+'signaltest'
        bot.send_message(CHAT_ID, text)