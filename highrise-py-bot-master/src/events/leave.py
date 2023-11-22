from highrise.models import User
from config.config import loggers


async def on_leave(bot, user: User) -> None:
    if loggers.leave:
        print(f"Игрок вышел😢: {user.username}:{user.id}")
    await bot.highrise.chat(f"{user.username} Выходит с комнаты😢!")
