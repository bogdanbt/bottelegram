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

symbols_list1=['1INCH','AAVE','ADA','ALGO','ALICE','ALPHA','ANKR','ANT','APE','API3','AR','ARPA','ATA','ATOM','AUDIO','AVAX','AXS'

,'BAKE','BAL','BAND','BAT','BCH','BEL','BLZ','BNB','BNX','BTC','C98','CELO','CELR','CHR','CHZ','COMP','COTI','CRV']

symbols_list2=[
'CTK',
'CTSI',
'CVC',

'DAR',
'DASH',
'DENT',
'DGB',
'DOGE',
'DOT',
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
'FTT']
symbols_list3=['GAL',
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
'LPT']
symbols_list4=['LRC',
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
'REN']
symbols_list5=['RLC',
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
'UNFI']
symbols_list6=['UNI',
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
    if data['signal']=="list1":
        for s in range(len(symbols_list1)):
            #text=symbols_list1[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=1'
            #url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=1'
            #url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=5'
            url='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=5'

            data=requests.get(url).json()
            data0=requests.get(url0).json()
            Vol=round(float(data[1]['buyVol']),0)+round(float(data[1]['sellVol']),0)
            last=round(float(data[0]['buyVol']),0)+round(float(data[0]['sellVol']),0)
            '''
            my_list2=[]
            for i in range(5):
                my_list2.append(round(float(data[i]['buyVol']),0)+float(data[i]['sellVol']) )
            my_min=min(my_list2)
            last=round(float(data[0]['buyVol']),0)+round(float(data[0]['sellVol']),0)
'''

            if last > Vol:
                q=round((last/Vol),3)
            else:
                q=0

            if q>4:
                text=symbols_list1[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest1'+Vol+'/'+last
        bot.send_message(CHAT_ID, text)
        return{"signal":"success"}
    if data['signal']=="list2":
        for s in range(len(symbols_list2)):
            #text=symbols_list1[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list2[s]+'&period=5m&limit=1'
            #url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=1'
            #url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=5'
            url='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list2[s]+'&period=5m&limit=10'

            data=requests.get(url).json()
            data0=requests.get(url0).json()
            my_list2=[]
            for i in range(5):
                my_list2.append(round(float(data[i]['buyVol']),0)+round(float(data[i]['sellVol']) ))
            my_min=min(my_list2)
            last=round(float(data[0]['buyVol']),0)+round(float(data[0]['sellVol']),0)


            if last > my_min:
                q=round((last/my_min),3)
            else:
                q=0

            if q>2.5:
                text=symbols_list2[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest2'
        bot.send_message(CHAT_ID, text)
        return{"signal":"success"}
    if data['signal']=="list3":
        for s in range(len(symbols_list3)):
            #text=symbols_list1[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list3[s]+'&period=5m&limit=1'
            #url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=1'
            #url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=5'
            url='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list3[s]+'&period=5m&limit=10'

            data=requests.get(url).json()
            data0=requests.get(url0).json()
            my_list2=[]
            for i in range(5):
                my_list2.append(round(float(data[i]['buyVol']),0)+round(float(data[i]['sellVol']) ))
            my_min=min(my_list2)
            last=round(float(data[0]['buyVol']),0)+round(float(data[0]['sellVol']),0)


            if last > my_min:
                q=round((last/my_min),3)
            else:
                q=0

            if q>2.5:
                text=symbols_list3[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest3'
        bot.send_message(CHAT_ID, text)
        return{"signal":"success"}
    if data['signal']=="list4":
        for s in range(len(symbols_list4)):
            #text=symbols_list1[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list4[s]+'&period=5m&limit=1'
            #url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=1'
            #url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=5'
            url='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list4[s]+'&period=5m&limit=10'

            data=requests.get(url).json()
            data0=requests.get(url0).json()
            my_list2=[]
            for i in range(5):
                my_list2.append(round(float(data[i]['buyVol']),0)+round(float(data[i]['sellVol']) ))
            my_min=min(my_list2)
            last=round(float(data[0]['buyVol']),0)+round(float(data[0]['sellVol']),0)


            if last > my_min:
                q=round((last/my_min),3)
            else:
                q=0

            if q>2.5:
                text=symbols_list4[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest4'
        bot.send_message(CHAT_ID, text)
        return{"signal":"success"}
    if data['signal']=="list5":
        for s in range(len(symbols_list5)):
            #text=symbols_list1[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list5[s]+'&period=5m&limit=1'
            #url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=1'
            #url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=5'
            url='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list5[s]+'&period=5m&limit=10'

            data=requests.get(url).json()
            data0=requests.get(url0).json()
            my_list2=[]
            for i in range(5):
                my_list2.append(round(float(data[i]['buyVol']),0)+round(float(data[i]['sellVol']) ))
            my_min=min(my_list2)
            last=round(float(data[0]['buyVol']),0)+round(float(data[0]['sellVol']),0)


            if last > my_min:
                q=round((last/my_min),3)
            else:
                q=0

            if q>2.5:
                text=symbols_list5[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest5'
        bot.send_message(CHAT_ID, text)
        return{"signal":"success"}
    if data['signal']=="list6":
        for s in range(len(symbols_list6)):
            #text=symbols_list1[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list6[s]+'&period=5m&limit=1'
            #url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=1'
            #url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list1[s]+'USDT'+'&period=5m&limit=5'
            url='https://www.binance.com/futures/data/takerlongshortRatio?symbol='+symbols_list6[s]+'&period=5m&limit=10'

            data=requests.get(url).json()
            data0=requests.get(url0).json()
            my_list2=[]
            for i in range(5):
                my_list2.append(round(float(data[i]['buyVol']),0)+round(float(data[i]['sellVol']) ))
            my_min=min(my_list2)
            last=round(float(data[0]['buyVol']),0)+round(float(data[0]['sellVol']),0)


            if last > my_min:
                q=round((last/my_min),3)
            else:
                q=0

            if q>2.5:
                text=symbols_list6[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest6'
        bot.send_message(CHAT_ID, text)
        return{"signal":"success"}

'''
    if data['signal']=="list2":
        for s in range(len(symbols_list2)):
            #text=symbols_list2[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list2[s]+'USDT'+'&period=5m&limit=1'
            url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list2[s]+'USDT'+'&period=5m&limit=5'
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
                text=symbols_list2[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest2'
        #bot.send_message(CHAT_ID, text)
        return{"signal":"success"}

    if data['signal']=="list3":
        for s in range(len(symbols_list3)):
            #text=symbols_list3[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list3[s]+'USDT'+'&period=5m&limit=1'
            url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list3[s]+'USDT'+'&period=5m&limit=5'
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
                text=symbols_list3[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest3'
        #bot.send_message(CHAT_ID, text)
        return{"signal":"success"}


    if data['signal']=="list4":
        for s in range(len(symbols_list4)):
            #text=symbols_list4[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list4[s]+'USDT'+'&period=5m&limit=1'
            url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list4[s]+'USDT'+'&period=5m&limit=5'
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
                text=symbols_list4[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest4'
        #bot.send_message(CHAT_ID, text)
        return{"signal":"success"}

    if data['signal']=="list5":
        for s in range(len(symbols_list5)):
            #text=symbols_list5[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list5[s]+'USDT'+'&period=5m&limit=1'
            url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list5[s]+'USDT'+'&period=5m&limit=5'
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
                text=symbols_list5[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest5'
        #bot.send_message(CHAT_ID, text)
        return{"signal":"success"}

    if data['signal']=="list6":
        for s in range(len(symbols_list6)):
            #text=symbols_list6[s]+'test'
            #bot.send_message(CHAT_ID, text)
            url0='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list6[s]+'USDT'+'&period=5m&limit=1'
            url='https://www.binance.com/futures/data/openInterestHist?symbol='+symbols_list6[s]+'USDT'+'&period=5m&limit=5'
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
                text=symbols_list6[s]+'signal'
                bot.send_message(CHAT_ID, text)
        text='endtest6'
        #bot.send_message(CHAT_ID, text)
        return{"signal":"success"}

'''
    #return{"signal":"success"}

if __name__ == 'main':
    app.run()


#   https://telebotbogdan.herokuapp.com/webhook
#   {"symbol":"Test","usdt":"5","signal":"list1"}