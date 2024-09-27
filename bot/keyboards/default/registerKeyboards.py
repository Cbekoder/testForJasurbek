from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ask_phone = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Telefon raqam", request_contact=True)],
    ]
)
