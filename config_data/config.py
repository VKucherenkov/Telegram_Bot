from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str                  # Токен для доступа к телеграм-боту
    admin_ids: list[int]        # Список id администраторов бота
    weather_api: str            # api на сайте погоды
    host: str                   # URL базы данных
    login_psql: str             # логин для подключения к базе данных
    password_psql: str          # пароль для подключения к базе данных
    db_name: str                # имя базы данных


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(
                    token=env('BOT_TOKEN'),
                    admin_ids=list(map(int, env.list('ADMIN_IDS'))),
                    weather_api=env('WEATHER_API'),
                    host=env('HOST_DB'),
                    login_psql=env('LOGIN_PSQL'),
                    password_psql=env('PASSWORD_PSQL'),
                    db_name=env('DB_NAME')))