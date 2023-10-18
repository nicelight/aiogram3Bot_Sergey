import logging
import asyncio
# from datetime import datatime

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.types import FSInputFile
from random import randint

TELEGRAM_TOKEN ="6390700887:AAHoGnCMsJ9AkK51rmJrxsOalBl-LHiZtCY"
# TELEGRAM_TOKEN =""
GROUP_ID = '-1001674247269' 

# вывод отладочных сообщений в терминал
logging.basicConfig(level=logging.INFO)

# создали обьект bot
bot = Bot(token=TELEGRAM_TOKEN)

# создаем обьект диспетчер 
dp = Dispatcher()

# обрабатываем команду старт
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    image_from_pc = FSInputFile('hello.webp')
    await message.answer_photo(image_from_pc, caption='Пообщаемся?)')
    await asyncio.sleep(2)
    await message.answer("Рад тебя видеть, <b> {0.first_name} </b> !".format(message.from_user), parse_mode='html')

# обработчик команды рандом 
#  /rnd 1-30
# /random 5-10
@dp.message(Command(commands=['random', 'rand', 'rnd']))
async def get_random(message: types.Message, command: CommandObject, bot: Bot):
    # разбиваем аргументы команды символом "-"
    a, b = [int(n) for n in command.args.split('-')]
    rnum = randint(a, b)
    # в личку
    await message.reply(f'Случайное число от {a} до {b} получилось: \t {rnum}')
    # в группу



@dp.message(Command('image'))
async def upload_photo(message: types.Message):
    image_from_pc = FSInputFile('hello.webp')
    await message.answer_photo(image_from_pc, caption='Пообщаемся?)')

@dp.message(Command('mygroup'))
async def cmd_to_group(message: types.Message, bot: Bot):
    await bot.send_message(GROUP_ID, 'hello from Sergey ')

# команда забанить пользователя 
@dp.message(Command('ban'))
async def funkciya_zabanit(message: types.Message):
    # если команда без цитаты 
    if not message.reply_to_message:
        await message.reply('пиши команду ban в ответ на сообщение')
        return
    await message.bot.delete_message(chat_id=GROUP_ID, message_id=message.message_id)
    await message.bot.ban_chat_member(chat_id=GROUP_ID, user_id=message.reply_to_message.from_user.id)

# ping pong 
@dp.message()
async def echo(message: types.Message):
    print('message listened')
    # await message.answer('бот Сергея услышал: ' + message.text)



# непрерывный режим работы бота в АССИНХРОННОМ режиме 
async def main():
    await dp.start_polling(bot)
    # del all unhandled messages 
    await bot.delete_webhook(drop_pending_updates=True)

# основной цикл
if __name__ == '__main__':
    asyncio.run(main())

