from aiogram.fsm.state import StatesGroup, State

class RegistrationStates(StatesGroup):
    id = State()
    full_name = State()
    username = State()
    email = State()
    phone = State()
