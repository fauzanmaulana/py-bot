import telebot
from model import model
from model import conn
from app import tokenBot

test = 'test'

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
def menu_data_siswa(message):
    results = model.selectAll(conn)
    data = ''
    no = 0
    for result in results:
        no += 1
        data += str(result) + "\n"
        data = data.replace('(', str(no) + '. ')
        data = data.replace(')', '')
        data = data.replace("'", '')
        data = data.replace(",", '')
        print(data)

    bot.reply_to(message, str(data))

bot.polling()