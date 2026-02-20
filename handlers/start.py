from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from keyboards.inline import main_menu_keyboard, back_to_main_keyboard
from utils.helpers import get_game_name, get_service_name

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # Тёплое приветствие
    text = (
        "Приветствуем тебя в **EasyGacha**! Мы поможем тебе прокачаться в любимых гача-играх.\n\n"
        "С нами ты сможешь:\n"
        "• Фармить ресурсы без устали\n"
        "• Прокачивать персонажей до максимума\n"
        "• Выполнять сложные игровые задачи\n"
        "• Зачищать карты и многое другое\n\n"
        "Мы ценим каждого клиента и подходим к заказам с душой. Выбери, что тебя интересует:"
    )
    await message.answer(text, reply_markup=main_menu_keyboard(), parse_mode="Markdown")

@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(
        "🌸 Главное меню",
        reply_markup=main_menu_keyboard()
    )
    await callback.answer()