import datetime
import time
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CallbackQueryHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram import InlineKeyboardButton
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert

p ='🤩'

cg = CoinGeckoAPI()

view = "Курс"
usd = '₿ --> $'
dsu = '$ --> ₿'
ablockchain = 'Графіки'

# Эта кнопка для просмотра курса
def button_view_handler(update: Update, context: CallbackContext):
    m = way(3)
    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    course = convert(amount=1, to=['RUB', 'EUR', 'UAH'])
    update.message.reply_text(
        text=(f"1 BTC to USD - {price['bitcoin']['usd']:.2f} USD"
        + f"\n1 BTC to EUR - {course['EUR']*price['bitcoin']['usd']:.2f} EUR"
        + f"\n1 BTC to UAH - {course['UAH']*price['bitcoin']['usd']:.2f} UAH")
    )

# Эта кнопка для конвертации ₿ --> $
def button_usd_handler(update: Update, context: CallbackContext,):
    way(1)
    update.message.reply_text(
        text = 'Введіть кількість ₿'
    )


# Эта кнопка для конвертации $ --> ₿
def button_dsu_handler(update: Update, context: CallbackContext):
    way(2)
    update.message.reply_text(
        text='Введіть кількість $'
    )


def covert(update: Update, context: CallbackContext):
    m = way(0)
    num = update.message.text
    num1 = float(num)
    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    if m == 1:
        update.message.reply_text(
            text=f"{num1*price['bitcoin']['usd']:.2f}" + ' $'
        )
    elif m == 2:
        update.message.reply_text(
            text=f"{num1 / price['bitcoin']['usd']:.6f}" + ' ₿'
        )

def way(n):
    global go
    if n == 1 or n == 2 or n == 3:
        go = n
        return (go)
    else:
        return (go)


# Эта кнопка для графиков
def button_ablockchain_handler(update: Update, context: CallbackContext):
    m = way(3)
    update.message.reply_text(
        text='https://cutt.ly/xbwvXZ1'
    )
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    try:
        text = float(text)
        return covert(update=update, context=context)
    except:
        if text == view:
            return button_view_handler(update=update, context=context)
        elif text == usd:
            return button_usd_handler(update=update, context=context)
        elif text == dsu:
            return button_dsu_handler(update=update, context=context)
        elif text == ablockchain:
            return button_ablockchain_handler(update=update, context=context)
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                KeyboardButton(text=view),
                KeyboardButton(text=usd),
                KeyboardButton(text=dsu),
                KeyboardButton(text=ablockchain)
                ],
            ],
            resize_keyboard=True,
        )
    update.message.reply_text(
        text=(f'Привіт {update.effective_user.first_name}! Колега готовий до співпраці!'),
        reply_markup=reply_markup,
    )

def main():
    print('Start')
    updater = Updater(
    token='1746386192:AAHip-qdUDgBJHSUxZ_H9F9OCIvgKMx9SGA',
    use_context=True,
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()