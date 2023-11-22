class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '/'
    botID = '655dc8ee1348f1cacb2db8bb'
    botName = 'Dev1s0n_Bot'
    ownerName = 'Dev1s0n'
    roomName = '🕷🇺🇦🪩CLUB-Dev1s0n🪩🇺🇦🕷'
    coordinates = {
        'x': 10.8,
        'y': 0.80000,
        'z': 14.5,
        'facing': 'FrontLeft'
    }


class loggers:
    # The following settings are related to events. Each event log can be enabled or disabled. Note that turning these off will not affect their usage in the game.
    SessionMetadata = True
    messages = True
    whispers = True
    joins = True
    leave = True
    tips = True
    emotes = False
    reactions = False
    userMovement = False


class messages:
    # The following are optional and serve as a basic usage example for calling messages and replacing variables.
    invalidPosition = "Your position could not be determined."
    invalidPlayer = "{user} нету в этой комнате."
    invalidUser = "Игрок {user} не найден."
    invalidUsage = "Usage: {prefix}{commandName}{args}"
    invalidUserFormat = "Invalid user format. Please use '@username'."

    
class permissions:
    # You can add as many IDs as you want, for example: ['id1', 'id2'].
    owners = ['650b569d5bf4b935215c8b73']
    moderators = ['63ac9ebc424c69c68666e0fc']


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = '65359bd5a26a28e3a8328b81'
    token = 'c8fadf3c910d9b4272b705fbb8d91b65e8df46a28321fabfbd8509b74eee8177'
