import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# TODO: Замените текст ниже на ваш настоящий токен от @BotFather
TOKEN = "8975890986:AAHvueaoSTuFtpKoytaRiOOl968ZGRYKD1k"

# Ваша ссылка на игру уже успешно добавлена сюда
WEB_APP_URL = "https://kolisnichenkoandr99-coder.github.io/potuzhno/"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="🇺🇦 Грати в Козацький Клікер",
        web_app=WebAppInfo(url=WEB_APP_URL)
    ))
    
    welcome_text = (
        f"Привіт, {message.from_user.first_name}! 👋\n\n"
        "Вітаємо у **Козацькому Клікері**! 🌾\n"
        "Клікай на Паляницю, заробляй монети, купуй покращення! 🇺🇦\n\n"
        "Натискай кнопку нижче, щоб розпочати гру👇"
    )
    await message.answer(welcome_text, reply_markup=builder.as_markup(), parse_mode="Markdown")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
