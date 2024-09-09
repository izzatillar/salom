from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

product_cb = CallbackData('product', 'id', 'count', 'action')


def order_menu():
    manu = InlineKeyboardMarkup(inline_keyboard=[

        [
            InlineKeyboardButton(text="Krossoverlar", switch_inline_query_current_chat="Krossoverlar"),

            InlineKeyboardButton(text="SUV", switch_inline_query_current_chat="SUV")],
        [
            InlineKeyboardButton(text="Miniven", switch_inline_query_current_chat="Miniven"),

            InlineKeyboardButton(text="Pick-up", switch_inline_query_current_chat="Pick-up")],
        [
            InlineKeyboardButton(text="Premium", switch_inline_query_current_chat="Premium"),

            InlineKeyboardButton(text="Ekonom", switch_inline_query_current_chat="Ekonom")],



    ], resize_keyboard=True)
    return manu


def product_markup(items_id, count):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='➕', callback_data=product_cb.new(id=items_id, count=count, action='plus')),
         InlineKeyboardButton(text=f'{count}-kun', callback_data=product_cb.new(id=items_id, count=count, action='count')),
         InlineKeyboardButton(text='➖', callback_data=product_cb.new(id=items_id, count=count, action='minus'))],
        [InlineKeyboardButton(text='ijaraga olish', callback_data=product_cb.new(id=items_id, count=count, action='add'))],
        [InlineKeyboardButton(text='ortga⬅️',callback_data='back')]
    ])
    return markup

main_menu=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🚘mashina ijaraga olish',callback_data='🚘mashina ijaraga olish')],
    [InlineKeyboardButton(text='⚙️Sozlamalar',callback_data='⚙️Sozlamalar'),
     InlineKeyboardButton(text='✍️izoh qoldirish',callback_data='✍️izoh qoldirish')]
])

car=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='',callback_data='Krossoverlar'),
     InlineKeyboardButton(text='SUV',callback_data='SUV')],
    [InlineKeyboardButton(text='Miniven',callback_data='Miniven'),
     InlineKeyboardButton(text='Pick-up',callback_data='Pick-up')],
    [InlineKeyboardButton(text='Premium',callback_data='Premium'),
     InlineKeyboardButton(text='Ekonom',callback_data='Ekonom')]


])
