import telebot
import time
CHAT_ID='425745139'
BOTTOKEN='5545278299:AAHIqGnUM6mrgB0fe8DWsUMZrrpDU1BQ8jI'
bot=telebot.TeleBot(BOTTOKEN)
#bot.reply_to('hi')
while True:
    bot.send_message(CHAT_ID, "hello")
    time.sleep(60)