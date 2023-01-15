import telebot
from django.conf import settings
from shop.models import TeleAdmin

bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    current_chat_id = message.chat.id
    existing_admin = False

    admin_list = TeleAdmin.objects.all()
    for admin in admin_list:
        if str(current_chat_id) == admin.chat_id:
            existing_admin = True

    if existing_admin:
        admin = admin_list.objects.get(chat_id=current_chat_id)
        bot.reply_to(message, "Hi {}, what's up? Seems like we've met before".format(admin.name))
    else:
        answer_text = "Hi! I'm a telegram bot for HalalFood admins. \n" \
                      "If you're about to become a new HalalFood admin - " \
                      "send a message in the following format: \n" \
                      "/register your_name. \n After that you will need a " \
                      "confirmation in HalalFood admin panel. Welcome!"
        bot.reply_to(message, answer_text)


def user_check(chat_id, name):
    admin_list = TeleAdmin.objects.all()
    answer = True
    for admin in admin_list:
        if admin.chat_id == str(chat_id):
            bot.send_message(chat_id, 'You have already been registered', parse_mode="MARKDOWN")
            answer = False
            break
        elif admin.name == name:
            bot.send_message(chat_id, 'This name has already been reserved. Try another way', parse_mode="MARKDOWN")
            answer = False
            break

    if name == '':
        bot.send_message(chat_id, 'Please input the command in the following order:\n /register *your_name*', parse_mode="MARKDOWN")
        answer = False

    return answer


@bot.message_handler(commands=['register'])
def create_new_admin(message):
    user_message = message.text
    user_name = (user_message.split(' '))[1]

    if user_check(message.chat.id, user_name):
        new_admin = TeleAdmin()
        new_admin.name = user_name
        new_admin.chat_id = str(message.chat.id)
        new_admin.save()
        bot.reply_to(message, "*{}*, you've been successfully registered!".format(user_name), parse_mode="MARKDOWN")


def order_alarm(chat_id, name, order_info):
    message_text = 'Hi, {0}!\n\n'.format(name)
    message_text += order_info
    bot.send_message(chat_id, message_text, parse_mode="MARKDOWN")


def main():
    bot.infinity_polling()