from highrise.models import User
from config.config import loggers, config


async def on_chat(bot, user: User, message: str) -> None:
    if loggers.messages:
        print(f"User {user.username}: Привет красавиц(-а)! {message}")
    if message.lstrip().startswith(config.prefix):
        await bot.command_handler.handle_command(user, message)
