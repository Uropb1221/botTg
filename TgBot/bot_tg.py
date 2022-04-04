import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.executor import start_webhook
from aiogram import Bot

import os, json, string


TOKEN = os.getenv('5150149062:AAGWhhdcohn2qfnne2RNEHnVf6Xrf8Ik_FA')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv('robotbinance22')

# webhook settings
WEBHOOK_HOST = f'https://robotbinance22.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


 if __name__ == '__bot_tg__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
async def on_startup(_):
	print('Бот вышел в онлайн')


'''*********************************Клиентская часть*************************************'''
@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, '🤖Привет, {0.first_name} ,меня зовут Robot_Binance ,я представляю вам бота для торговли криптовалютой, чем я могу помочь?👨🏼‍💻 \nhttps://t.me/Robot_Binance_Chat - Здесь вы можете задать любые вопросы,а так же узнать результаты наших клиентов😊  \nДля получения информации можете воспользоваться подсказками ниже⬇️'.format(message.from_user), reply_markup= kb_client)
		await message.delete()
	except:
		await message.reply('✅Общение с ботом через личные сообщения, напишите ему:\nhttp://t.me/Robot_BinanceBot👨🏼‍💻')

@dp.message_handler(commands=['help'])
async def command_help(message : types.Message):
	await message.reply('✅Общение с ботом через личные сообщения, напишите ему:\nhttp://t.me/Robot_BinanceBot👨🏼‍💻')

@dp.message_handler(commands=['Администраторы🔺'])	
async def command_admin(message : types.Message):
	await message.reply('✅Напишите ему:\nhttp://t.me/@rodlonov1\nЕсли он не отвечает, можете обратиться к ним: \nhttp://t.me/@uropb1221👨🏼‍💻  \nhttp://t.me/@timoX01👨🏼‍💻')

@dp.message_handler(commands=['Прайс🗒'])
async def command_admin(message : types.Message):
	await message.reply('📊Прайс лист по установке торгового бота: \nСтоимость первичной настройки: 149$ \nДополнительная настройка и постоянное обслуживание 10% от прибыли💯')

@dp.message_handler(commands=['Стратегия🔸'])	
async def command_admin(message : types.Message):
	await message.reply('Стратегия бота заключается в сеточной торговле. Бот выставляет защитные ордера на усреднение.\nУсловно, бот входит в сделку на 0,5-2% от депозита, и выставляет ордера. Если цена падает, бот усредняет позицию, как только происходит откат бот фиксирует прибыль. Сделок за день может быть не ограниченное количество, в зависимости от волатильности рынка. Торгует бот только в лонг и закрывает только прибыль.\nЧтобы убедиться в этом можете перейти к нам в канал, там мы транслируем каждый день результаты публичного аккаунта \nhttps://t.me/Robot_Binance_Chat ')

@dp.message_handler(commands=['Вопросы❓'])
async def command_admin(message : types.Message):
	await message.reply('✅Часто задаваемые вопросы: \n1️⃣По какой стратегии торгует бот?  \
\n- Бот торгует сеточной торговлей, высчитывает риск и сам усредняется при просадке рынка , при малейшем импульсе в лонг фиксирует прибыль и опять открывает сделки .\
\
 \n2️⃣С помощью чего бот выдерживает просадку?  \
\n-Бот выдерживает просадку благодаря страховочным ордерам , которые открываются при коррекции\
\
  \n3️⃣В чём основная сложность настройки бота?\
\n-Сложность в настройке бота состоит в том , чтобы правильно расставить страховочные ордера для того , чтобы он не слил депозит при мощном обвале рынка  \
\
  \n4️⃣На какой процент от депозита бот заходит в сделку?  \
\n-от 0,7% до 2%\
\
  \n5️⃣Торгует ли бот в шорт?  \
\n- Бот так же может торговать в шорт , но мы используем только лонг .  \
\
  \n6️⃣Где я могу посмотреть статистику по доходности бота?  \
\n-Графики с месячной доходностью вы можете проанилизировать в нашем беплатном канале.\nhttps://t.me/Robot_Binance_Chat \
\nТак же в нашем канале вы можете задать любой вопрос по работе, обслуживанию, доходности, статистики бота. Наша команда с большим удовольствием даст на них ответ.🦾🤖')

@dp.message_handler(commands=['Статистика📊📈'])
async def command_admin(message : types.Message):
	await message.reply('📊За время нашей работы нам удалось заметить, что бот приносит от 20-50% в месяц. \nПри хорошем рынке возможен и больший результат, но мы берём в среднем. Основной плюс бота в том, что он выдерживает любую коррекцию криптовалют, благодаря правильнй настройке и соблюдению рисков. Поиск правильных алгоритмов работы и тестирование различных стратегий у нас занял больше года, но мы добились результата. На протяжении последнего года мы используем одну и ту же стратегию с регулярной прибылью. Только после того, как мы сами убедились в нашей стратегии, команда приняла решение показать её вам и помочь заработать, в этом канале есть закреплённые сообщения с отчётами, результатами и ежедневная статистика публичного счёта. \nПрисоединяйся!🤝 \nhttps://t.me/Robot_Binance_Chat ')

b1 = KeyboardButton('/Администраторы🔺')
b2 = KeyboardButton('/Прайс🗒')
b3 = KeyboardButton('/Стратегия🔸')
b4 = KeyboardButton('/Вопросы❓')
b5 = KeyboardButton('/Статистика📊📈')




kb_client = ReplyKeyboardMarkup(resize_keyboard= True)

kb_client.row(b4, b3).row(b1, b2).add(b5)
# insert-ИЩЕТ ПОЛОЖЕНИЕ
# Row-в одну строку

# def register_hundlers_client(dp : Dispatcher):  Не понял что за команды, регистрация присвоенных сообщений
# 	dp.register_message_hundler(Price_command, commands=['Price'])
    # dp.register_message_hundler(Admin_command, commands=['Admin']
'''*********************************Админская часть*************************************'''

'''*********************************Общая часть*************************************'''

@dp.message_handler()
async def echo_send(message : types.Message):
	if message.text == 'Привет':
	   await message.answer('Привет,{0.first_name}🤚🏻'.format(message.from_user))

	if message.text == 'привет':
	   await message.answer('Привет,{0.first_name}🤚🏻'.format(message.from_user)) 

	if message.text == 'Здравствуйте':
	   await message.answer('Привет,{0.first_name}🤚🏻'.format(message.from_user)) 

	if message.text == 'Добрый день':
	   await message.answer('Привет,{0.first_name}🤚🏻'.format(message.from_user)) 

	if message.text == 'Спасибо':
	   await message.answer('Обращайтесь,{0.first_name}. Буду рад помочь!🤖'.format(message.from_user))   

	if message.text == 'спасибо':
	   await message.answer('Обращайтесь,{0.first_name}.Буду рад помочь!🤖'.format(message.from_user))      

	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
	    .intersection(set(json.load(open('Мат.json')))) !=set():
	    await message.reply('Мат запрещён!Будьте внимательны!⛔️⛔️⛔️')	
	    await message.delete()

async def echo_send(message : types.Message):
	if message.text == '?':
	   await message.answer('Я не могу ответить на этот вопрос😞 Спросите админимтратора.')
	else:
		await message.answer('Вполне возможно😊')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

