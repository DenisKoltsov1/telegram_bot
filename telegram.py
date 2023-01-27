from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from config import TOKEN
import logging
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
#Диспетчер — объект, занимающийся получением апдейтов от Telegram с последующим выбором хэндлера для обработки принятого апдейта.
dp = Dispatcher(bot)
# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Хэндлер на команду /start
#Хэндлер — асинхронная функция, которая получает от диспетчера/роутера очередной апдейт и обрабатывает его.
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    cd_inline=CallbackData("post",'action',"data")
    kb = [ types.InlineKeyboardButton(text='Пополнить баланс',callback_data='спасибо'),]
    
    #keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    keyboard = types.InlineKeyboardMarkup().add(*kb)
    #await message.reply(f'Привет, {message.from_user.first_name} \nЯ - бот для пополнения баланса.\nНажмите на кнопку, чтобы пополнить баланс.',reply_markup=keyboard)
    await message.reply(f'Привет, {message.from_user.first_name}, \nЯ - бот для пополнения баланса.\nНажмите на кнопку, чтобы пополнить баланс. \nСнизу инлайн кнопка с текстом  Пополнить баланс',reply_markup=keyboard)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")



@dp.message_handler(commands=['admin'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)