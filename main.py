#!/usr/bin/env python

# This is a simple telegram bot script

import telebot

# Get your bot token from BotFather
bot_token = '5703457980:AAENe1sbyxwHK7SVOk7u8s1xe3AZog633WY'

bot = telebot.TeleBot(token=bot_token)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm a telegram bot")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
