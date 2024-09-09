from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    lang = State()

    city_uz = State()
    city_ru = State()
    city_eng = State()


class MainMenu(StatesGroup):
    step_one = State()
    step_two = State()
    step_three = State()
    step_four= State()

class R(StatesGroup):
    step_one = State()
    step_two=State()
class I(StatesGroup):
    step_one = State()


class Info(StatesGroup):
    step_one_uz = State()
    step_two_uz = State()

    step_one_ru = State()
    step_two_ru = State()

    step_one_eng = State()
    step_two_eng = State()


class Settings(StatesGroup):
    step_one = State()

    set_name_uz = State()
    set_city_uz = State()
    set_lang_uz = State()
    set_contact_uz = State()

    set_name_ru = State()
    set_city_ru = State()
    set_lang_ru = State()
    set_contact_ru = State()

    set_city_eng = State()
    set_lang_eng = State()
    set_contact_eng = State()
    set_name_eng = State()


class OrderState(StatesGroup):
    step_one_uz = State()
    step_two_uz = State()
    step_three_uz = State()
    step_four_uz = State()

