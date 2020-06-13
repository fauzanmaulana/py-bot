import telebot
from model import model
from model import conn
from app import tokenBot

bot = telebot.TeleBot(tokenBot)

welcomeReplay = '''
hello my name is ucup, my job is manage student data
you can write any commands bellow and i will do it :
/showall -*to show all student name in the class*
/showdetail #name -*to show all student name in the class*
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

    bot.reply_to(message, data)


@bot.message_handler(commands=['showdetail'], func=lambda message: True)
def detail_data_siswa(message):
    nama = message.text.split('#')
    resultSearch = model.searchData(conn, str(nama[1]))
    id = resultSearch[0]
    results = model.showData(conn, str(id))
    data = ''
    no = 0
    judul = ''
    for result in results:
        no += 1
        if no is 1:
            judul = 'nama'
        elif no is 2:
            judul = 'umur'
        elif no is 3:
            judul = 'ttl'
        else:
            judul = 'alamat'
        data += judul + " : " + str(result) + "\n"

    bot.reply_to(message, data)


bot.polling()