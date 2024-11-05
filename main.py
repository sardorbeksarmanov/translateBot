from telebot import TeleBot, types

import trans

bot = TeleBot("6641668245:AAHBS1boZnrHN1DsdO-69AXNG2Q8kouZE44")

@bot.message_handler(["start"])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, "Assalomu alaykum, ushbu bot matnlarni tarjima qilishga yordam beradi!")

@bot.message_handler()
def translatechi(xabar: types.Message):
    bot.send_message(xabar.from_user.id, trans.tarjimon(xabar.text))

bot.polling()

#Bot manzili   https://t.me/tarjimon_elementaryBot




