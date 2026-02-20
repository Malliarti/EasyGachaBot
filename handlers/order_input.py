from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from config import ADMIN_ID
from keyboards.inline import back_to_main_keyboard, main_menu_keyboard
from handlers.service_selection import OrderStates

router = Router()

@router.message(StateFilter(OrderStates.waiting_for_description))
async def receive_description(message: Message, state: FSMContext):
    user_data = await state.get_data()
    game_name = user_data.get("game_name", "???")
    service_name = user_data.get("service_name", "???")

    user_info = f"@{message.from_user.username}" if message.from_user.username else f"ID: {message.from_user.id}"

    admin_text = (
        f"🔔 Новый заказ!\n"
        f"От: {user_info} (ID: {message.from_user.id})\n"
        f"Игра: {game_name}\n"
        f"Услуга: {service_name}\n\n"
        f"Описание:\n{message.text or '[Медиа-сообщение]'}"
)

    await message.bot.send_message(ADMIN_ID, admin_text)

    if message.photo:
        await message.bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption="📎 Фото к заказу")
    if message.video:
        await message.bot.send_video(ADMIN_ID, message.video.file_id, caption="📎 Видео к заказу")
    if message.document:
        await message.bot.send_document(ADMIN_ID, message.document.file_id, caption="📎 Документ к заказу")

    await message.answer(
        "✅ Спасибо! Ваш запрос отправлен администратору.\n"
        "Ожидайте ответа в личные сообщения (обычно в течение часа).\n"
        "Если хотите сделать ещё заказ – нажмите кнопку ниже.",
        reply_markup=main_menu_keyboard()
    )
    await state.clear()

@router.callback_query(F.data == "back_to_main", StateFilter(OrderStates.waiting_for_description))
async def cancel_order(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        "🌸 Главное меню",
        reply_markup=main_menu_keyboard()
    )
    await callback.answer()