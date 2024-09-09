from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db

uz = "🇺🇿 O'zbekcha"
ru = '🇷🇺 Русский'
eng = '🇬🇧 English'

back_uz = '⬅️ Ortga'
back_ru = '⬅️ Назад'
back_eng = '⬅️ Back'
lang = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text=uz), KeyboardButton(text=ru)],
    [KeyboardButton(text=eng)]
])

city = {
    'uz': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton('Toshkent'), KeyboardButton('Andijon')],
        [KeyboardButton(text='Samarqand')]
    ]),
    'eng': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton('Tashkent'), KeyboardButton('Andijan')],
        [KeyboardButton(text='Samarkand')]
    ]),
    'ru': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton('Ташкент'), KeyboardButton('Андижан')],
        [KeyboardButton(text='Самарканд')]
    ])
}

menu = {
    'uz': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton('🍽 Menyu')],
        [KeyboardButton(text='📖 Buyurtmalar tarixi'), KeyboardButton(text='✍️ Fikr bildirish')],
        [KeyboardButton(text="ℹ️ Ma'lumot"), KeyboardButton(text='☎️ Biz bilan aloqa')],
        [KeyboardButton(text='⚙️Sozlamalar')]
    ]),
    'eng': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton('🍽 Order')],
        [KeyboardButton(text='📖 My orders'), KeyboardButton(text='✍️ Leave a feedback')],
        [KeyboardButton(text='ℹ️ Information'), KeyboardButton(text='☎️ Contact us')],
        [KeyboardButton(text='⚙️Settings')]
    ]),
    'ru': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton('🍽 Меню')],
        [KeyboardButton(text='📖 Мои заказы'), KeyboardButton(text='✍️ Оставить отзыв')],
        [KeyboardButton(text='ℹ️ Информация'), KeyboardButton(text='☎️ Обратная связь')],
        [KeyboardButton(text='⚙️Настройки')]
    ])
}

delivery = {
    'uz': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='🚙 Yetkazib berish'), KeyboardButton('🏃 Olib ketish')],
        [KeyboardButton(text='⬅️ Ortga')]
    ]),
    'ru': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='🚙'), KeyboardButton('🏃')],
        [KeyboardButton(text=back_ru)]
    ]),
    'eng': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='🚙'), KeyboardButton('🏃')],
        [KeyboardButton(text=back_eng)]
    ]),
}
izoh=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Hammasi yoqdi ♥️')],
        [KeyboardButton(text='Yaxshi ⭐️⭐️⭐️⭐️')],
        [KeyboardButton(text='Yoqmadi ⭐️⭐️⭐️')],
        [KeyboardButton(text='Yomon ⭐️⭐️')],
        [KeyboardButton(text='Juda yomon 👎🏻')],
        [KeyboardButton(text='⬅️ Ortga')]])

feedback = {
    'uz': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Hammasi yoqdi ♥️')],
        [KeyboardButton(text='Yaxshi ⭐️⭐️⭐️⭐️')],
        [KeyboardButton(text='Yoqmadi ⭐️⭐️⭐️')],
        [KeyboardButton(text='Yomon ⭐️⭐️')],
        [KeyboardButton(text='Juda yomon 👎🏻')],
        [KeyboardButton(text='⬅️ Ortga')]
    ]),


    'ru': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='😊Все понравилось, на 5 ❤️')],
        [KeyboardButton(text='☺️Нормально, на 4 ⭐️⭐️⭐️⭐️')],
        [KeyboardButton(text='😐Удовлетворительно, на 3 ⭐️⭐️⭐️')],
        [KeyboardButton(text='☹️Не понравилось, на 2 ⭐️⭐️')],
        [KeyboardButton(text='😤Хочу пожаловаться 👎🏻')],
        [KeyboardButton(text='⬅️ Назад')]
    ]),

    'eng': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='😊Liked everything 5 ❤️')],
        [KeyboardButton(text='☺️Normal, at 4 ⭐️⭐️⭐️⭐️')],
        [KeyboardButton(text='😐Satisfactory, by 3 ⭐️⭐️⭐️')],
        [KeyboardButton(text='☹️Dont like it, 2 ⭐️⭐️')],
        [KeyboardButton(text='😤I want to complain 👎🏻')],
        [KeyboardButton(text='⬅️ Back')]
    ])
}
settings = {
    'uz': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Ismni o’zgartirish'), KeyboardButton('📱 Raqamni o’zgartirish')],
        [KeyboardButton(text="🏙 Shaharni o'zgartirish"), KeyboardButton("🇺🇿 Tilni o'zgartirish")],
        [KeyboardButton(text='⬅️ Ortga')]
    ]),

    'ru': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Сменить имя'), KeyboardButton('📱 Сменить номер')],
        [KeyboardButton(text="🏙 Изменить город"), KeyboardButton("🇷🇺 Изменить язык")],
        [KeyboardButton(text='⬅️ Назад')]
    ]),

    'eng': ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Change name'), KeyboardButton('📱 Change number')],
        [KeyboardButton(text="🏙 Change city"), KeyboardButton("🇬🇧 Change language")],
        [KeyboardButton(text='⬅️ Back')]
    ]),
}


def get_branches(language, chat_id, locations='no'):
    back = None
    if language == 'uz':
        city = db.execute(sql='select city from users where chat_id = ? ', parameters=(chat_id,), fetchone=True)[0]
        city_branches = db.execute(sql="""
SELECT name from filials JOIN  city on city.id = filials.city_id 
WHERE city.name_uz = ? """, parameters=(city,), fetchall=True)
        back = back_uz
    elif language == 'ru':
        city = db.execute(sql='select city from users where chat_id = ? ', parameters=(chat_id,), fetchone=True)[0]
        city_branches = db.execute(sql="""
SELECT name from filials JOIN  city on city.id = filials.city_id 
WHERE city.name_ru = ? """, parameters=(city,), fetchall=True)
        back = back_ru
    else:
        city = db.execute(sql='select city from users where chat_id = ? ', parameters=(chat_id,), fetchone=True)[0]
        city_branches = db.execute(sql="""
SELECT name from filials JOIN  city on city.id = filials.city_id 
WHERE city.name_eng = ? """, parameters=(city,), fetchall=True)
        back = back_eng
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if locations == 'yes':
        markup.add(KeyboardButton('📍 Eng yaqin fillialni aniqlash', request_location=True))

    markup.add(*[i[0] for i in city_branches])
    markup.add(back)
    return markup

d= ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Ha')],
        [KeyboardButton(text='Yo`q')]])