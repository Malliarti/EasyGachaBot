from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.inline import back_to_main_keyboard
from utils.helpers import get_service_name

router = Router()

class OrderStates(StatesGroup):
    waiting_for_description = State()

@router.callback_query(F.data.startswith("service_"))
async def service_chosen(callback: CallbackQuery, state: FSMContext):
    parts = callback.data.split("_")
    game_code = parts[1]
    service_code = parts[2]

    data = await state.get_data()
    game_name = data.get("game_name", "???")

    service_name = get_service_name(service_code)

    await state.update_data(service_code=service_code, service_name=service_name)
    await state.set_state(OrderStates.waiting_for_description)
    print(f"Состояние waiting_for_description установлено для пользователя {callback.from_user.id}")

    text = (
        f"📝 Вы выбрали: **{service_name} | {game_name}**\n\n"
        "Пожалуйста, опишите задание максимально подробно.\n"
        "Можете прикрепить фото, видео или файлы – мы всё передадим администратору.\n\n"
        "✏️ Напишите ваше сообщение:"
    )
    await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard())
    await callback.answer()