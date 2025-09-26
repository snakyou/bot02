import telebot

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")


@bot.message_handler(commands=["hello"])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")


@bot.message_handler(commands=["bye"])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(
        message,
        """Привет, этот бот был создан специально для тестирования 
                на пайтон! Я знаю команды 
                /start-запускает бота,
                /hello-бот будет отвечать в ответ привет,
                /bye-бот будет прощаться""",
    )

@bot.message_handler(commands=["heh"])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['photo'])
async def photo_send(message: telebot.types.Message):
    with open('test.png', 'rb') as new_file:
        await bot.send_photo(message.chat.id, new_file)

@bot.message_handler(commands=["throw"])
def send_number(message):
    bot.reply_to(
        message, random.randint(1, 6)
    )

@bot.message_handler(commands=["coin"])
def send_coin(message):
    text = ["орёл", "решка"]

    bot.reply_to(
        message, random.choice(text)
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
