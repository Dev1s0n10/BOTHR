from highrise import User


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = 'help'
        self.description = "Есть вопросы? Ображщайтесь к @Dev1s0n или @1fxd1"
        self.aliases = ['info', 'hmm']  # you can add as much aliases as u want
        # its optional to add permissions, i dont have the permission example in config.permissions.json
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        # now notice that we used self.bot.highrise and not self.highrise, keep this in mind
        await self.bot.highrise.chat('Команды: /emote. Есть вопросы? Ображщайтесь к @Dev1s0n или @1fxd1')
        # now you can use this template for all commands just copy and paste it
        # i hope this helped !
