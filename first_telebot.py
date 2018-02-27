import telebot
import random
import apiai
import json
import os
token = '517286465:AAEMyMb3b5QMoIaD6V-RBHAHVgadSerFvSI'
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['photo'])
def send_photo(message):
     st_random_photo = str(random.randint(1, 1000))
     url = 'https://picsum.photos/400/600/?image=' + st_random_photo
     bot.send_photo(message.chat.id, url)


@bot.message_handler(content_types=["text"])
def get_answer(message):
     request = apiai.ApiAI('32bc6874ecd548e08e19b9a87cd02cd8').text_request()
     request.lang = 'ru'
     request.session_id = str(message.chat.id)
     request.query = message.text
     requestJson = json.loads(request.getresponse().read().decode('utf-8'))
     response = requestJson['result']['fulfillment']['speech']
     if response:
          strt = str(response)
          bot.send_message(message.chat.id, strt)
     else :
          bot.send_message(message.chat.id, "Булат над мной издевается. Помогитееее")
if __name__ == '__main__':
     bot.polling(none_stop=True)