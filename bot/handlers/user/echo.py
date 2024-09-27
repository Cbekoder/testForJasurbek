from aiogram.enums import ParseMode
from aiogram.types import Message

from bot.utils.gpt_request import send_request
from loader import dp, bot

@dp.message()
async def echo_handler(message: Message) -> None:
    await bot.send_chat_action(message.chat.id, "typing")
    response = send_request(message.text)
    await message.answer(response, parse_mode=ParseMode.MARKDOWN)
