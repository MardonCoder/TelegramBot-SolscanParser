import telebot
import Parser
import time
from telebot import types
import threading

API_TOKEN = 'Token'
bot = telebot.TeleBot(API_TOKEN)

wallets = {}

thread = {}
threadChecker = {}



def passiveInfoSending(wallet_name, message, tranzactionCheckMsg,url: str):
    while threadChecker[wallet_name]:
        tranzactionMessage = Parser.getLastOperationInfo(url, wallet_name)
        if(tranzactionCheckMsg != tranzactionMessage and tranzactionMessage != ' '):
            bot.send_message(message.chat.id, tranzactionMessage)
            tranzactionCheckMsg = tranzactionMessage
        time.sleep(30)

def generate_main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Создать кошелёк')
    itembtn2 = types.KeyboardButton('Удалить кошелёк')
    markup.add(itembtn1, itembtn2)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Я бот для парсирования кошельков solscan, выберите действие", reply_markup=generate_main_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Создать кошелёк":
        if len(wallets) < 10:
            bot.send_message(message.chat.id, "Введите название кошелька:")
            bot.register_next_step_handler(message, get_wallet_name)
        else:
            bot.send_message(message.chat.id, "Достигнуто максимальное количество кошельков.", reply_markup=generate_main_keyboard())
    elif message.text == "Удалить кошелёк":
        if wallets:
            delete_keyboard = types.ReplyKeyboardMarkup(row_width=1)
            for wallet_name in wallets.keys():
                delete_keyboard.add(types.KeyboardButton(wallet_name))
            back_button = types.KeyboardButton("Назад")
            delete_keyboard.add(back_button)
            bot.send_message(message.chat.id, "Какой кошелёк удалить?", reply_markup=delete_keyboard)
            bot.register_next_step_handler(message, delete_wallet)
        else:
            bot.send_message(message.chat.id, "Нет созданных кошельков.", reply_markup=generate_main_keyboard())

def get_wallet_name(message):
    wallet_name = message.text
    bot.send_message(message.chat.id, "Введите ссылку на кошелёк:")
    bot.register_next_step_handler(message, get_wallet_link, wallet_name=wallet_name)

def get_wallet_link(message, wallet_name):
    if('https://solscan.io/account/' in message.text):
        wallet_link = message.text
        wallets[wallet_name] = wallet_link
        threadChecker[wallet_name] = True
        bot.send_message(message.chat.id, "Кошелёк успешно создан.", reply_markup=generate_main_keyboard())
        tranzactionCheckMessage = Parser.getLastOperationInfo(wallet_link, wallet_name)
        thread[wallet_name] = threading.Thread(target=passiveInfoSending(wallet_name, message, tranzactionCheckMessage,wallet_link))
    else:
        bot.send_message(message.chat.id, 'вы ввели неправильную ссылку')

def delete_wallet(message):
    if message.text == "Назад":
        bot.send_message(message.chat.id, "Возврат к основному меню.", reply_markup=generate_main_keyboard())
        return

    wallet_name = message.text
    threadChecker[wallet_name] = False
    if wallet_name in wallets:
        del wallets[wallet_name]
        bot.send_message(message.chat.id, f"Кошелёк '{wallet_name}' удалён.", reply_markup=generate_main_keyboard())
    else:
        bot.send_message(message.chat.id, "Этот кошелёк уже удалён.", reply_markup=generate_main_keyboard())

bot.polling()
