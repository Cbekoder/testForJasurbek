from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import html
from states.registerStates import RegistrationStates
from keyboards.default.registerKeyboards import ask_phone
from data.saveData import checkUser
from keyboards.default.menuKeyboard import menu

from loader import dp

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    if not checkUser(message.from_user.id):
        await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!\n"
                             f"Ro'yxatdan o'tish uchun telefon raqamingizni kiriting:",
                             reply_markup=ask_phone)
        await state.set_state(RegistrationStates.phone)
    else:
        await message.answer(f"Quyidagi menudan kerakli bo'limni tanlang!", reply_markup=menu)

