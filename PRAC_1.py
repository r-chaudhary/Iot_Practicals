import telepot
token = '1266263131:AAHihcotwCEGzrFeqqcp5TIp_osTF_N7b0E'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == "text":
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

TelegramBot.message_loop(handle)
