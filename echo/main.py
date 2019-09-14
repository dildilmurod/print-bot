from subprocess import Popen
from subprocess import PIPE
from datetime import datetime

from telegram import Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from echo.config import TG_TOKEN
from echo.config import TG_API_URL


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hello. Send me something"
    )


def do_time(bot: Bot, update: Update):
    # res = Popen("date", stdout=PIPE)
    #
    # text, error = res.communicate()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # if error:
    #     text = "Error is happened. Time is unknown"
    # else:
    #     text = text.decode("utf-8")
    bot.send_message(
        chat_id=update.message.chat_id,
        text=current_time
    )


def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="This is test bot. That just prints"
    )


def do_print(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = "Your id {}\n\n{}".format(chat_id, update.message.text)
    bot.send_message(
        chat_id=chat_id,
        text=text,
    )


def main():
    bot = Bot(
        token=TG_TOKEN,
        base_url=TG_API_URL,
    )
    updater = Updater(
        bot=bot,
    )
    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    time_handler = CommandHandler("time", do_time)
    message_handler = MessageHandler(Filters.text, do_print)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
