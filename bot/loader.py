from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from data.config import GPT_TOKEN
from data.config import BOT_TOKEN
from openai import OpenAI
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

client = OpenAI(api_key=GPT_TOKEN)