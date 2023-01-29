from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
#from aiogram.dispatcher.filters.state import State, StatesGroup
import datetime

from config import TOKEN
import logging
# Объект бота
bot = Bot(token=TOKEN)
#Диспетчер — объект, занимающийся получением апдейтов от Telegram с последующим выбором хэндлера для обработки принятого апдейта.
dp = Dispatcher(bot)

# Включаем логирование

logging.basicConfig(level=logging.INFO)
botlogfile = open('INFO_log.log')
botlogfile = open('Eror_log.log')
logging.basicConfig(level=logging.INFO,filename="INFO_log.log",filemode="w")
logging.basicConfig(level=logging.ERROR,filename="Eror_log.log",filemode="w")

'''
@dp.message_handler()
async def loggin(message: types.Message):
    dtn = datetime.datetime.now()S
    botlogfile = open('TestBot.log', 'a')
    tr= print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.reply(tr)
'''
#Хэндлер — асинхронная функция, которая получает от диспетчера/роутера очередной апдейт и обрабатывает его.

#class Form(StatesGroup):
#     count= State() 


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    
    kb = [ types.InlineKeyboardButton(text='Пополнить баланс',callback_data='press'),]
    keyboard = types.InlineKeyboardMarkup().add(*kb)
    #await Form.count.set()
    await message.reply(f'Привет, {message.from_user.first_name}, \nЯ - бот для пополнения баланса.\nНажмите на кнопку, чтобы пополнить баланс. \nСнизу инлайн кнопка с текстом  Пополнить баланс',reply_markup=keyboard)
   
'''
count=0
def enter_count():
    
    count=int(input('введие сумму:'))
    return count
'''

     
@dp.callback_query_handler(lambda c: c.data == 'press')
async def EnterSumm(callback_query_handler: types.CallbackQuery):
    #count=int(input('введие сумму:'))
    
    await callback_query_handler.answer('Введите сумму, на которую вы хотите пополнить баланс!')

@dp.message_handler(content_types="text")
async def Vvod(message: types.Message):
    await message.reply(f"Вы хотите положить на счет {message.text} рублей")




@dp.message_handler(commands=['admin'])
async def process_start_command(message: types.Message):
    kb = [ 
        [types.InlineKeyboardButton(text='Выгрузка пользователей с балансом',callback_data='спасибо')],
        [types.InlineKeyboardButton(text='Выгрузка логов',callback_data='спасибо')],
        [types.InlineKeyboardButton(text='Изменить баланс',callback_data='спасибо')],
        [types.InlineKeyboardButton(text='Заблокировать пользователя',callback_data='спасибо')]
         
        ]
 #ReplyKeyboardMarkup — объект, который создает клавиатуру.
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.reply(f'Админка,', reply_markup=keyboard)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)









if __name__ == '__main__':
    executor.start_polling(dp)