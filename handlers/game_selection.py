from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.inline import games_keyboard, services_keyboard
from utils.helpers import get_game_name

router = Router()

@router.callback_query(F.data == "select_game")
async def select_game(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎮 Выберите игру, по которой нужна помощь:",
        reply_markup=games_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data.startswith("game_"))
async def game_chosen(callback: CallbackQuery, state: FSMContext):
    game_code = callback.data.split("_")[1]
    game_name = get_game_name(game_code)
    
    await state.update_data(game_code=game_code, game_name=game_name)
    
    await callback.message.edit_text(
        f"✨ Отлично! Теперь выберите услугу для игры **{game_name}**:",
        reply_markup=services_keyboard(game_code, game_name),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_games")
async def back_to_games(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎮 Выберите игру:",
        reply_markup=games_keyboard()
    )
    await callback.answer()