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

symbols_list=['1INCH','AAVE','ADA','ALGO','ALICE','ALPHA','ANKR','ANT','APE','API3','AR','ARPA','ATA','ATOM','AUDIO','AVAX','AXS'

,'BAKE','BAL','BAND','BAT','BCH','BEL','BLZ','BNB','BNX','BTC','C98','CELO','CELR','CHR','CHZ','COMP','COTI','CRV',

'CTK',
'CTSI',
'CVC',
'DAR',
'DASH',
'DENT',
'DGB',
'DOGE',
'DOT',
'DUSK',
'DYDX',
'EGLD',
'ENJ',
'ENS',
'EOS',
'ETC',
'ETH',
'FIL',
'FLM',
'FLOW',
'FTM',
'FTT',
'GAL',
'GALA',
'GMT',
'GRT',
'GTC',
'HBAR',
'HNT',
'HOT',
'ICX',
'IMX',
'INJ',
'IOST',
'IOTA',
'IOTX',
'JASMY',
'KAVA',
'KLAY',
'KNC',
'KSM',
'LINA',
'LINK',
'LIT',
'LPT',
'LRC',
'LTC',
'MANA',
'MASK',
'MATIC',
'MKR',
'MTL',
'NEAR',
'NEO',
'NKN',
'OCEAN',
'OGN',
'OMG',
'ONE',
'ONT',
'OP',
'PEOPLE',
'QTUM',
'RAY',
'REEF',
'REN',
'RLC',
'ROSE',
'RSR',
'RUNE',
'RVN',
'SAND',
'SFP',
'SKL',
'SNX',
'SOL',
'SRM',
'STMX',
'STORJ',
'SUSHI',
'SXP',
'THETA',
'TOMO',
'TRB',
'TRX',
'UNFI',
'UNI',
'VET',
'WAVES',
'WOO',
'XEM',
'XLM',
'XMR',
'XRP',
'XTZ',
'YFI',
'ZEC',
'ZEN',
'ZIL',

]

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
    if data['signal']=="btcstart":
        for s in range(len(symbols_list)):
            text=symbols_list[s]+'test'
            bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list[s]+'USDT'+'&period=5m&limit=1'
            url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list[s]+'USDT'+'&period=5m&limit=5'
            data=requests.get(url).json()
            data0=requests.get(url0).json()
            my_list2=[]
            for i in range(5):
                my_list2.append(round(float(data[i]['sumOpenInterest']),0))
            my_min=min(my_list2)
            last=round(float(data[0]['sumOpenInterest']),0)


            if last > my_min:
                q=round((last/my_min),3)
            else:
                q=0

            if q>1.5:
                text=symbols_list[s]+'signal'
                bot.send_message(CHAT_ID, text)

    return{"signal":"success"}


if __name__ == 'main':
    app.run()

