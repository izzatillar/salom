from aiogram import types
from states.state import MainMenu, Info, Settings
from keyboards.default.markups import delivery, back_uz, menu, feedback, get_branches, settings, back_eng
from loader import dp, db


@dp.message_handler(text='🍽 Order', state=MainMenu.step_one_eng)
async def mane_uz(message: types.Message):
    await message.answer(text='Choose an action:', reply_markup=delivery['eng'])
    await MainMenu.step_two_eng.set()


@dp.message_handler(text='📖 My orders', state=MainMenu.step_one_eng)
async def history_uz(message: types.Message):
    await message.answer(text="There is no history, you need to fill it out 😊")


@dp.message_handler(text='☎️ Contact us', state=MainMenu.step_one_eng)
async def contact_us_uz(message: types.Message):
    await message.answer(text=f"""
You can write to us if you have Questions/Complaints/Suggestions: @Street77tech_bot

☎️ Phone number: 71-200-73-73 / 71 200-86-86
""")


@dp.message_handler(text='✍️ Leave a feedback', state=MainMenu.step_one_eng)
async def feedback_uz(message: types.Message):
    await message.answer(text="""
✅ Monitoring the Street 77 delivery service.
We thank you for your choice and we will be glad if you rate our work on a 5-point scale  
""", reply_markup=feedback['eng'])
    await MainMenu.step_two_eng.set()


@dp.message_handler(text="ℹ️ Information", state=MainMenu.step_one_eng)
async def info_uz(message: types.Message):
    await message.answer(text='Which branch are you interested in?',
                         reply_markup=get_branches('eng', message.from_user.id))
    await Info.step_one_eng.set()


@dp.message_handler(text='⚙️Settings', state=MainMenu.step_one_eng)
async def settings_uz(message: types.Message):
    await message.answer(text='Choose an action:', reply_markup=settings['eng'])
    await Settings.step_one.set()


@dp.message_handler(text=back_eng, state=MainMenu.step_two_eng)
async def back_menu(message: types.Message):
    await message.answer(text='Main menu', reply_markup=menu['eng'])
    await MainMenu.step_one_eng.set()
