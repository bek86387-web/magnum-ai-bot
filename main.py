import os
import telebot
from openai import OpenAI

# GitHub Secrets yoki Environment Variables'dan ma'lumotlarni olish
# Bu usul kalitlarni ochiq qolishidan himoya qiladi
TELEGRAM_TOKEN = os.getenv('8568851239:AAHSva3qh2eo59ltfGVGaBSb4t8gLK-XgVI')
OPENAI_KEY = os.getenv('Magnum')

bot = telebot.TeleBot(8568851239:AAHSva3qh2eo59ltfGVGaBSb4t8gLK-XgVI)
client = OpenAI(api_key=Magnum)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men GitHub-da ishlovchi aqlli botman. Savol bering!")

@bot.message_handler(func=lambda message: True)
def handle_chat(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sen foydali yordamchisan."},
                {"role": "user", "content": message.text}
            ]
        )
        bot.reply_to(message, response.choices.message.content)
    except Exception as e:
        bot.reply_to(message, f"Xatolik: {e}")

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.infinity_polling()
