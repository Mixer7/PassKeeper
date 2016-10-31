
import telebot
from classes import User
from classes import Account

testUser = User('name', 'surname', '123123123123')
token = '292439910:AAHd72nbGZz7dfsySHvZpb4-ih2KrGxYvJU'

bot = telebot.TeleBot(token)

def get_obj(num_of_obj, obj_list):

    start = obj_list[num_of_obj].find(':')
    end = len(obj_list[num_of_obj])
    obj = obj_list[num_of_obj][start + 1:end]
    return obj


@bot.message_handler(commands=['start'])
def create_user(message):

    this_user = User(message.from_user.first_name, message.from_user.last_name, message.from_user.id)
    bot.send_message(message.chat.id, 'Привет, {}!'.format(message.from_user.first_name))


@bot.message_handler(commands=['help'])
def list_commands(message):
    bot.send_message(message.chat.id, '/start - новый пользователь\n'
                                      '/new - запись нового аккаунта в базу\n'
                                      '/tellaccount - просмотр логина и пароля\n'
                                      '/sites - вывод сайтов в базе данных')


@bot.message_handler(commands=['new'])
def new_acc(message):
    mytext = (str(message.text)).split()
    if len(mytext) == 4:
        testUser.add_account(mytext[1], Account(mytext[2], mytext[3]))
        bot.send_message(message.chat.id, "Oke")
    else:
        bot.send_message(message.chat.id, "Not oke")


@bot.message_handler(commands=['sites'])
def give_sites(message):
    temp = "\n".join(testUser.return_sites())
    if temp != '':
        bot.send_message(message.chat.id, temp)
    else:
        bot.send_message(message.chat.id, "Not oke")

@bot.message_handler(commands=['tellaccount'])
def give_acc(message):
    mytext = (str(message.text)).split()
    if len(mytext) == 2:
        myacc = testUser.return_account(mytext[1])
        if myacc is None:
            bot.send_message(message.chat.id, "Not oke")
            return
        if myacc[0] is None:
            myacc[0] = ''
        if myacc[1][0] is None:
            myacc[1][0] = ''
        if myacc[1][1] is None:
            myacc[1][1] = ''

        bot.send_message(message.chat.id, "Site: " + myacc[0] + " Login: " + myacc[1][0] + " Password: " + myacc[1][1])
    else:
        bot.send_message(message.chat.id, "Not oke")


@bot.message_handler(content_types = ['text'])
def remember_acc(message):

    newtext = str(message.text)

    if ('site' in newtext) and ('login' in newtext) and ('pass' in newtext):

        acc_list = list(newtext.split('\n'))
        site = get_obj(0, acc_list)
        login = get_obj(1, acc_list)
        password = get_obj(2, acc_list)

        this_acc = Account(login, password)
        bot.send_message(message.chat.id, 'Запомнил!')

    else:
        bot.send_message(message.chat.id, 'Простите, я вас не понимаю')



if __name__ == "__main__":

    bot.polling(none_stop=True)
