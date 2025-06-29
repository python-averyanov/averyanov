import telebot
import degeneration
import re
TOKEN = '5322881710:AAHcr0lug4W8AajITpR1E48utwARkPn-umU'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Привет, введите запрос! ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text
    ans = degeneration.generate_answer(prompt)
    match = re.search(r'Answer:\s*(.*?)(?:<|\n|$)', ans, re.IGNORECASE)
    ans2 = match.group(1).strip()

    bot.reply_to(message, ans)

bot.polling(none_stop=True)
