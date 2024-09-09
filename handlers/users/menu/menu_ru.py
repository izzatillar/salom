from aiogram import types
from states.state import MainMenu, Info, Settings
from keyboards.default.markups import delivery, back_uz, menu, feedback, get_branches, settings, back_ru
from loader import dp, db


@dp.message_handler(text='🍽 Меню', state=MainMenu.step_one_ru)
async def mane_uz(message: types.Message):
    await message.answer(text='Выберите действие:', reply_markup=delivery['ru'])
    await MainMenu.step_two_ru.set()


@dp.message_handler(text='📖 Мои заказы', state=MainMenu.step_one_ru)
async def history_uz(message: types.Message):
    await message.answer(text="История отсутствует, надо его заполнить 😊")


@dp.message_handler(text='☎️ Обратная связь', state=MainMenu.step_one_ru)
async def contact_us_uz(message: types.Message):
    await message.answer(text=f"""
Вы можете написать нам, если у вас есть Вопросы/Жалобы/Предложения: @Street77tech_bot

☎️ Телефонный номер: 71-200-73-73 / 71 200-86-86
""")


@dp.message_handler(text='✍️ Оставить отзыв', state=MainMenu.step_one_ru)
async def feedback_uz(message: types.Message):
    await message.answer(text="""
✅ Контроль сервиса доставки Street 77.
Мы благодарим за сделанный выбор и будем рады, если Вы оцените нашу работу по 5 бальной шкале 
""", reply_markup=feedback['ru'])
    await MainMenu.step_two_ru.set()


@dp.message_handler(text="ℹ️ Информация", state=MainMenu.step_one_ru)
async def info_uz(message: types.Message):
    await message.answer(text='Какой филиал Вас интересует?',
                         reply_markup=get_branches('ru', message.from_user.id))
    await Info.step_one_ru.set()


@dp.message_handler(text='⚙️Настройки', state=MainMenu.step_one_ru)
async def settings_uz(message: types.Message):
    await message.answer(text='Выберите действие:', reply_markup=settings['ru'])
    await Settings.step_one.set()


@dp.message_handler(text=back_ru, state=MainMenu.step_two_ru)
async def back_menu(message: types.Message):
    await message.answer(text='Главное меню', reply_markup=menu['ru'])
    await MainMenu.step_one_ru.set()
