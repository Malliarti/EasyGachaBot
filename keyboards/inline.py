from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="🎮 Выбор игры", callback_data="select_game"))
    builder.add(InlineKeyboardButton(text="💬 Написать админу", url="https://t.me/EG_Malliarti"))
    builder.adjust(1)
    return builder.as_markup()

def games_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Arknights: Endfield", callback_data="game_arknights"))
    builder.add(InlineKeyboardButton(text="Honkai: Star Rail", callback_data="game_hsr"))
    builder.add(InlineKeyboardButton(text="Wuthering Waves", callback_data="game_wuwa"))
    builder.add(InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main"))
    builder.adjust(1)
    return builder.as_markup()

def services_keyboard(game_code: str, game_name: str):
    # game_code нужно для callback, game_name для отображения
    builder = InlineKeyboardBuilder()
    services = [
        ("farm", "Фарм ресурсов"),
        ("level", "Прокачка персонажей"),
        ("tasks", "Выполнение игровых задач"),
        ("custom", "Индивидуальные запросы"),
        ("clear", "Зачистка карты")
    ]
    for code, name in services:
        callback = f"service_{game_code}_{code}"
        text = f"{name} | {game_name}"
        builder.add(InlineKeyboardButton(text=text, callback_data=callback))
    builder.add(InlineKeyboardButton(text="🔙 Назад к играм", callback_data="back_to_games"))
    builder.adjust(1)
    return builder.as_markup()

def back_to_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="🏠 Главное меню", callback_data="back_to_main"))
    return builder.as_markup()