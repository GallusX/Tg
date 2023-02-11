from aiogram import Bot, Dispatcher, executor, types
import openai
API_TOKEN = '6197118714:AAGqKHQSNrl15MgxaHUS1DIvzgssrLDJQ3k' 
openai.api_key = "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"
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Проверка подписки пользователя на канал
    is_subscribed = await bot.get_chat_member(chat_id='@gallusbots', user_id=message.from_user.id)
    if is_subscribed.status == 'member':
        # Пользователь подписан, бот работает
        await message.answer('Привет! Напиши что ты хочешь узнать и я обязательно отвечу')
    else:
        # Пользователь не подписан, бот не работает
        await message.answer('Пожалуйста, подпишитесь на наш канал @gallusbots, чтобы использовать ChatGPT.')
@dp.message_handler()
async def echo_all(message: types.Message):
    is_subscribed = await bot.get_chat_member(chat_id='@gallusbots', user_id=message.from_user.id)
    if is_subscribed.status == 'member':
        # Пользователь подписан, бот работает
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message.text, 
            max_tokens=2048,
            n = 1,
            stop=None,
            temperature=0.5,
        )
        await message.answer(response["choices"][0]["text"])
    else:
        # Пользователь не подписан, бот не работает
        await message.answer('Пожалуйста, подпишитесь на наш канал @gallusbots, чтобы использовать ChatGPT.')
    

if __name__ == '__main__':
    executor.start_polling(dp)
