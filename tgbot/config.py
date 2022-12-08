from dataclasses import dataclass

from environs import Env


# @dataclass
# class DbConfig:
#     host: str
#     password: str
#     user: str
#     database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    # db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token="5257942822:AAFqBBqGZs6UJZsF3fJ6fY-f8pCFQelxXRw",
            admin_ids=(762342298,),
            use_redis=False,
        ),
        # db=DbConfig(
        #     host=env.str('DB_HOST'),
        #     password=env.str('DB_PASS'),
        #     user=env.str('DB_USER'),
        #     database=env.str('DB_NAME')
        # ),
        misc=Miscellaneous()
    )
