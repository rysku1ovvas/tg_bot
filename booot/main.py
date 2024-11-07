import telebot
from telebot import types
from dotenv import load_dotenv
import random
import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot('7664288465:AAEcPdGbb8edGfPPN_Tai_1zkWUdgYRILn0')

mems = [
    "Чакинул Пат",
    "э Оля",
    "стАловкадамын",
    "кетчи а",
    "адвАкАтный болгулачы"
]

girls = [
    "Бегимай - ходячяя катастрофа. Прозвище Бека. Привычка - в любой проблеме говорить 'лучше бы я умерла'.",
    "Мирай - ходячяя проблема. Настоящее имя Миргул, на клавиатуре иногда пишем Минай. Привычка - говорить мамбетские фразы.",
    "Айдана - вечный срыв. Прозвище Алкаш. Привычка - говорить 'Пошли бухать'.",
    "Элдана - другая планета. Прозвище - Эля. Привычка - 24/7 в наушниках.",
    "Аяна - пофигистка. Прозвище - Аян. Привычка - 'Маган поки маган поки'."
]

MUSIC_FOLDER = r'C:\ayan_songs'
PHOTOS_FOLDER = r'C:\ayan_songs\ayan_photos'

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_mems = types.KeyboardButton("Мемы компашки 🤡")
    button_music = types.KeyboardButton("Любимые треки 🎵")
    button_girl = types.KeyboardButton("Девочки 💅")
    button_photos = types.KeyboardButton("Фото🎨")
    markup.add(button_mems, button_music, button_girl, button_photos)

    inline_markup = types.InlineKeyboardMarkup()
    instagram_button = types.InlineKeyboardButton("Мой Instagram : ", url="https://www.instagram.com/rysku1ovvas/profilecard/?igsh=bzk5djR6NHVrZjMx")
    inline_markup.add(instagram_button)

    bot.send_message(message.chat.id, "Привет!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Мемы компашки 🤡")
def send_mem(message):
    mem = random.choice(mems)
    bot.send_message(message.chat.id, mem)

@bot.message_handler(func=lambda message: message.text == "Девочки 💅")
def send_mem(message):
    girl = random.choice(girls)
    bot.send_message(message.chat.id, girl)

@bot.message_handler(func=lambda message: message.text == "Любимые треки 🎵")
def send_music(message):
    if os.path.exists(MUSIC_FOLDER):
        music_files = [file for file in os.listdir(MUSIC_FOLDER) if file.endswith(('.mp3', '.m4a'))]
        if music_files:
            music_file = random.choice(music_files)
            with open(os.path.join(MUSIC_FOLDER, music_file), 'rb') as music:
                bot.send_audio(message.chat.id, music)

@bot.message_handler(func=lambda message: message.text == "Фото🎨")
def send_photo(message):
    photo_files = [file for file in os.listdir(PHOTOS_FOLDER) if file.endswith(('.jpg'))]
    if photo_files:
        photo_file = random.choice(photo_files)
        with open(os.path.join(PHOTOS_FOLDER, photo_file), 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    

if __name__ == '__main__':
  bot.polling(none_stop=True)

