from loader import bot
from utils.set_bot_commands import set_default_commands
from handlers.custom_handlers.sender import com

if __name__ == "__main__":
    com()
    set_default_commands(bot)
    bot.infinity_polling()
