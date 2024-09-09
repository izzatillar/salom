from aiogram import types
from aiogram.dispatcher import FSMContext


from keyboards.inline.inline import main_menu
from loader import dp, db, bot
from states.state import Register, MainMenu, I, R
from keyboards.default.markups import lang, uz, ru, eng, menu, feedback, izoh


@dp.message_handler(commands=['start'],state='*')
async def cm_start(message: types.Message):
    await message.answer_photo(photo='https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2019_13/2798361/190325-rental-cars-cs-229p.jpg',
                               caption=f"Salom!\n\nBu bot orqali siz bizning kompaniyadan mashinalarni haydovchi va haydovchisiz ijaraga olishingiz mumkin\nBizning xizmatimizdan foydalaning 👇",
                               reply_markup=main_menu)
    await MainMenu.step_one.set()

@dp.callback_query_handler(text='✍️izoh qoldirish',state=MainMenu.step_one)
async def ger(call:types.CallbackQuery):
    await call.message.answer('Marxamat',reply_markup=izoh)
    await I.step_one.set()

@dp.message_handler(state=I.step_one)
async def qab(mes:types.Message):
    await bot.send_message(chat_id=6109293710,text=f'{mes.text}-izoh')


@dp.message_handler(text='⬅️ Kategoriyaga',state='*')
async def qasb(mes: types.Message):
    await mes.answer_photo(
        photo='https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2019_13/2798361/190325-rental-cars-cs-229p.jpg',
        caption=f"Salom!\n\nBu bot orqali siz bizning kompaniyadan mashinalarni haydovchi va haydovchisiz ijaraga olishingiz mumkin\nBizning xizmatimizdan foydalaning 👇",
        reply_markup=main_menu)
    await MainMenu.step_one.set()

@dp.message_handler(commands=['rek'],state='*')
async def give(message:types.Message):
    await message.answer('Reklamani rasmini kiriting:')
    await R.step_one.set()
ph=[]
@dp.message_handler(content_types=types.ContentType.PHOTO,state=R.step_one)
async def qax(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['photo']=message.photo
    print(data['photo'])
    ph.append(message.photo[0].file_id)
    await message.answer('matn kiriting')
    await R.step_two.set()

@dp.message_handler(state=R.step_two)
async def ger(message:types.Message,state:FSMContext):
    await state.get_data()
    sql='select user_id from basket'
    f=db.execute(sql,fetchall=True)
    for i in f:
        await bot.send_photo(chat_id=i[0],photo=ph[0],caption=message.text

                             )
    await message.answer_photo(
        photo='https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2019_13/2798361/190325-rental-cars-cs-229p.jpg',
        caption=f"Salom!\n\nBu bot orqali siz bizning kompaniyadan mashinalarni haydovchi va haydovchisiz ijaraga olishingiz mumkin\nBizning xizmatimizdan foydalaning 👇",
        reply_markup=main_menu)
    await MainMenu.step_one.set()
