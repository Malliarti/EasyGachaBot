def get_game_name(game_code: str) -> str:
    games = {
        "arknights": "Arknights: Endfield",
        "hsr": "Honkai: Star Rail",
        "wuwa": "Wuthering Waves"
    }
    return games.get(game_code, game_code)

def get_service_name(service_code: str) -> str:
    services = {
        "farm": "Фарм ресурсов",
        "level": "Прокачка персонажей",
        "tasks": "Выполнение игровых задач",
        "custom": "Индивидуальные запросы",
        "clear": "Зачистка карты"
    }
    return services.get(service_code, service_code)