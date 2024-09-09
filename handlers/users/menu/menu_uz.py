from aiogram import types
from states.state import MainMenu, Info, Settings
from keyboards.default.markups import delivery, back_uz, menu, feedback, get_branches, settings
from loader import dp, db


@dp.message_handler(text='🍽 Menyu', state=MainMenu.step_one_uz)
async def mane_uz(message: types.Message):
    await message.answer(text='Harakat tanlang', reply_markup=delivery['uz'])
    await MainMenu.step_two_uz.set()


@dp.message_handler(text='📖 Buyurtmalar tarixi', state=MainMenu.step_one_uz)
async def history_uz(message: types.Message):
    await message.answer(text="Buyurtmalar tarixi yo'q, uni to'ldirishingiz kerak 😊")


@dp.message_handler(text='☎️ Biz bilan aloqa', state=MainMenu.step_one_uz)
async def contact_us_uz(message: types.Message):
    await message.answer(text=f"""
Agar sizda Savollar/Shikoyatlar/Takliflar bo'lsa bizga yozishingiz mumkin: @Street77tech_bot

☎️ Telefon raqam: 71-200-73-73 / 71 200-86-86
""")


@dp.message_handler(text='✍️ Fikr bildirish', state=MainMenu.step_one_uz)
async def feedback_uz(message: types.Message):
    await message.answer(text="""
✅ Street 77ni tanlaganingiz uchun rahmat.
Agar Siz bizning hizmatlarimiz sifatini yaxshilashga yordam bersangiz, bundan benihoya xursand bo'lamiz.
Buning uchun 5 ballik tizim asosida baholang    
""", reply_markup=feedback['uz'])
    await MainMenu.step_two_uz.set()


@dp.message_handler(text="ℹ️ Ma'lumot", state=MainMenu.step_one_uz)
async def info_uz(message: types.Message):
    await message.answer(text='Sizni qaysi filial qiziqtiryapti?',
                         reply_markup=get_branches('uz', message.from_user.id))
    await Info.step_one_uz.set()


@dp.message_handler(text='⚙️Sozlamalar', state=MainMenu.step_one_uz)
async def settings_uz(message: types.Message):
    await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])
    await Settings.step_one.set()


@dp.message_handler(text=back_uz, state=MainMenu.step_two_uz)
async def back_menu(message: types.Message):
    await message.answer(text='Bosh menu', reply_markup=menu['uz'])
    await MainMenu.step_one_uz.set()
