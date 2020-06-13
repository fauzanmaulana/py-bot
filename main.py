import telebot
from model import model
from model import conn
from app import tokenBot

bot = telebot.TeleBot(tokenBot)

welcomeReplay = '''
hello my name is ucup, my job is manage student data
you can write any commands bellow and i will do it :
/showall -*to show all student name in the class*
'''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, welcomeReplay, parse_mode= 'Markdown')

@bot.message_handler(commands=['showall'])
def send_all_data(message):
	bot.reply_to(message, 'ini semua data siswa')

bot.polling()