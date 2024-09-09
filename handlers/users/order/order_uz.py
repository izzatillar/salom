from aiogram import types
from states.state import MainMenu, OrderState
from keyboards.default.markups import get_branches, back_uz, delivery, d
from keyboards.inline.inline import order_menu, product_markup, product_cb, main_menu
from aiogram.dispatcher import FSMContext
from loader import dp, db

@dp.callback_query_handler(text='🚘mashina ijaraga olish',state=MainMenu.step_one)
async def first_car(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Tanlang!',reply_markup=order_menu())
    await MainMenu.step_two.set()
    await call.answer()




@dp.callback_query_handler(text='back',state='*')
async def csd(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer('Tanlang!', reply_markup=order_menu())
    await MainMenu.step_two.set()
    await call.answer()


@dp.inline_handler(lambda x: x.query in db.get_category(), state=MainMenu.step_two)
async def inline_mode(inline: types.InlineQuery):
    msg = []
    sql = '''
select i.id, i.name, i.price, i.caption, i.photo from items as i
join category as c on i.category_id = c.id
where c.name = ?
    '''
    for id, name, price, caption, photo in db.execute(sql=sql, parameters=(inline.query,), fetchall=True):
        msg.append(
            types.InlineQueryResultArticle(
                id=id,
                title=name,
                input_message_content=types.InputMessageContent(
                    message_text=name
                ),
                thumb_url=photo,
                description=caption
            )

        )
    msg.append(
        types.InlineQueryResultArticle(
            id=str('back'),
            title=back_uz,
            input_message_content=types.InputMessageContent(
                message_text="⬅️ Kategoriyaga"
            ),
            thumb_url='https://cdn.pixabay.com/photo/2017/06/20/14/55/icon-2423347_1280.png',
            description="Ortga qaytish uchun tugmani bosing"

        )

    )
    await inline.answer(results=msg, cache_time=0)
    await OrderState.step_three_uz.set()


@dp.message_handler(state=OrderState.step_three_uz)
async def get_items(message: types.Message):
    sql = '''
select id, name, photo, price, caption from items
where name = ?
    '''
    id, name, photo, price, caption = db.execute(sql=sql, parameters=(message.text,), fetchone=True)

    await message.answer_photo(photo=photo,
                               caption=f'{name}\n\n{caption}\n\nNarxi: {price}',
                               reply_markup=product_markup(id, 1))
    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    await message.delete()


@dp.callback_query_handler(product_cb.filter(action='plus'), state=OrderState.step_three_uz)
@dp.callback_query_handler(product_cb.filter(action='minus'), state=OrderState.step_three_uz)
@dp.callback_query_handler(product_cb.filter(action='add'), state=OrderState.step_three_uz)
@dp.callback_query_handler(product_cb.filter(action='count'), state=OrderState.step_three_uz)
async def product(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    items_id = callback_data['id']
    count = int(callback_data['count'])
    action = callback_data['action']
    data = await state.get_data()
    print(data)
    if action == 'plus':
        count += 1
        sql = '''
        select  name,  price, caption from items
        where id = ?
            '''
        name, price, caption = db.execute(sql=sql, parameters=(items_id,), fetchone=True)

        mes = f'{name}\n\n{caption}\n\nNarxi: {price * count}'
        await call.message.edit_caption(mes, reply_markup=product_markup(items_id, count))

    elif action == 'minus':
        if count > 1:
            count -= 1
            sql = '''
                    select  name,  price, caption from items
                    where id = ?
                        '''
            name, price, caption = db.execute(sql=sql, parameters=(items_id,), fetchone=True)

            mes = f'{name}\n\n{caption}\n\nNarxi: {price * count}'
            await call.message.edit_caption(mes, reply_markup=product_markup(items_id, count))
        else:
            await call.answer(text='minum 1')

    elif action == 'count':
        await call.answer(text=f'{count}-kun')

    else:





        sql = """
insert into basket(user_id, item_id, count)
values(?, ?, ?)
        """
        db.execute(sql=sql, parameters=(call.from_user.id, items_id, count), commit=True)
        sql = 'select name from items where id = ?'
        items_name = db.execute(sql, parameters=(items_id,), fetchone=True)[0]
        sql = """
select sum(i.price * b.count)  from basket as b
join items as i on i.id = b.item_id
where b.user_id = ?

        """
        total_price = db.execute(sql=sql, parameters=(call.from_user.id,), fetchone=True)[0]
        await call.message.answer(text=f"Mahsulot: {items_name} savatga muvaffaqiyatli qo'shildi ✅")

        await call.message.answer(text='Davom etamizmi? 😉')
        await call.message.answer(text='Xaydovchi bilan olasizmi:', reply_markup=d)
        await call.message.delete()
        await OrderState.step_two_uz.set()

@dp.message_handler(text='Ha',state=OrderState.step_two_uz)
async def qwertyui(message:types.Message):
    await message.answer(f'Haydovchi muvaffaqiyatli qo`shildi(narxi({20}💰)\n'
                         f'Yunusobot tumanidagi ofisimizdan ilib ketishingiz mumkin!')
    sql='''update basket
set driver=1 where user_id=?'''

    db.execute(sql,parameters=(message.from_user.id,))
    await message.answer_photo(
        photo='https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2019_13/2798361/190325-rental-cars-cs-229p.jpg',
        caption=f"Salom!\n\nBu bot orqali siz bizning kompaniyadan mashinalarni haydovchi va haydovchisiz ijaraga olishingiz mumkin\nBizning xizmatimizdan foydalaning 👇",
        reply_markup=main_menu)
    await MainMenu.step_one.set()


@dp.message_handler(text='Yo`q',state=OrderState.step_two_uz)
async def qwertyufi(message:types.Message):
    await message.answer(f'Yunusobot tumanidagi ofisimizdan ilib ketishingiz mumkin!')
    await message.answer_photo(
        photo='https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2019_13/2798361/190325-rental-cars-cs-229p.jpg',
        caption=f"Salom!\n\nBu bot orqali siz bizning kompaniyadan mashinalarni haydovchi va haydovchisiz ijaraga olishingiz mumkin\nBizning xizmatimizdan foydalaning 👇",
        reply_markup=main_menu)
    await MainMenu.step_one.set()