from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Asosiy bo'lim"),
            KeyboardButton(text="Ma'lumotlar")
        ],
        [
            KeyboardButton(text="Info"),
            KeyboardButton(text="Aloqa")
        ]
    ]
)