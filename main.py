import telebot

# --- SOZLAMALAR ---
# Yangi API tokeningiz
TOKEN = '8568851239:AAHSva3qh2eo59ltfGVGaBSb4t8gLK-XgVI'
bot = telebot.TeleBot(TOKEN)
CREATOR = "Ozodbek Yusupov"

# --- SAVOL-JAVOBLAR BAZASI ---
smart_responses = {
    "salom": f"Assalomu alaykum! Men **Magnum AI** botiman. Sizga qanday yordam bera olaman? 😊",
    "qalaysan": "Rahmat, men juda yaxshiman! Sizning ishlaringiz va savdolaringiz qanday ketyapti?",
    "nima qila olasan": "Men siz bilan suhbatlasha olaman va treyding bo'yicha savollaringizga javob bera olaman. Kelajakda funksiyalarim ko'payadi!",
    "kim yaratgan": f"Meni **{CREATOR}** yaratgan. U professional treyder va dasturchi.",
    "rahmat": "Arziydi! Har doim xizmatingizdaman. Savollaringiz bo'lsa beravering.",
    "trading nima": "Treyding — bu bozorlarda aktivlarni sotib olish va sotish orqali foyda ko'rish san'atidir.",
    "magnum nima": "Magnum — bu savdo olamida sizning eng yaqin va aqlli yordamchingiz bo'lishi uchun yaratilgan loyiha.",
    "hayr": "Xayr! Salomat bo'ling, ishlaringizda omad tilayman! 👋"
}

# --- KOMANDALAR ---

@bot.message_handler(commands=['start'])
def start(message):
    text = (f"👋 **Salom! Men Magnum AI botiman.**\n\n"
            f"👤 **Yaratuvchi:** {CREATOR}\n\n"
            f"Men bilan shunchaki suhbatlashishingiz mumkin. "
            f"Menga 'Salom', 'Kim yaratgan?' yoki 'Trading nima?' kabi savollarni yozib ko'ring!")
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# --- ASOSIY JAVOB BERUVCHI ---

@bot.message_handler(func=lambda message: True)
def chat(message):
    user_text = message.text.lower().strip()
    
    # Lug'atdan mos javobni qidirish
    found_reply = None
    for key in smart_responses:
        if key in user_text:
            found_reply = smart_responses[key]
            break
    
    if found_reply:
        # Agar javob topilsa
        bot.reply_to(message, f"{found_reply}\n\n👤 **Yaratuvchi:** {CREATOR}", parse_mode="Markdown")
    else:
        # Agar savolni tushunmasa
        bot.reply_to(message, f"Hozircha bu savolga javobim yo'q, lekin men har kuni o'rganyapman! 🚀\n\n👤 **Yaratuvchi:** {CREATOR}")

# --- BOTNI ISHGA TUSHIRISH ---
if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.polling(none_stop=True)
