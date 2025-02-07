
from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dp)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dp)

    try:
        db.create_table_users()
    except Exception as err:
        print(f'Bazada xatolik {err}')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
