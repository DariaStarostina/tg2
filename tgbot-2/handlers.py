# Import library
from main import bot, dp
from aiogram import types
from aiogram.types import Message

keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

#Array for keyboard
array_keyboard = ["/start","/bye"]

# Send message to admin
async def send_to_admin(dp):
	await bot.send_message(chat_id=admin_id, text="Bot start")

    #Function of start bot
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
        await message.answer(text='Сао, брат', reply_markup=keyboard_markup)

        #Function of start bot
@dp.message_handler(commands=['bye'])
async def send_welcome(message: types.Message):
        keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
        await message.answer(text='Бай, брат', reply_markup=keyboard_markup)
