import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot('7682780191:AAFQ84fQaBmHG5LKeBT42kV0sXhIMVoZx6g')

ADMIN_ID = 6279429922


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        '''  
Привіт! 👋 Я бот — DOLIFMP Games 🎰

Це розважальний бот з різноманітними іграми, щоб забезпечити тебе чудовим настроєм!
Зі мною ти точно не занудьгуєш! Ти можеш грати як один, так і з друзями. 🔥
А ось тут всі ігри — /game
·········································· 
Є питання? — не проблема 👉 /help

version: 0.1 BETA
        '''
    )


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id,
        '''
✨ Ось перелік всіх команд:    

🔶 /game - Перелік всіх доступних ігор.    
🔶 /info - Інформація о боте  
🔶 /authors - Автори бота  
🔶 /reportbug - Репорт багів                         
🔶 /ID - Дізнатися свій Telegram ID
        '''
    )


@bot.message_handler(commands=['reportbug'])
def report_bug(message):
    bot.send_message(
        message.chat.id,
        '''
✍️ Опишіть знайдену помилку або проблему.  
Будь ласка, надайте якомога більше інформації:  
- Що саме не працює?  
- Які дії ви виконували?  
- Повідомлення про помилку, якщо воно було.  

Введіть ваш репорт:
        '''
    )
    bot.register_next_step_handler(message, preview_bug_report)


def preview_bug_report(message):
    if not message.text.strip():
        bot.send_message(
            message.chat.id,
            'Ваше повідомлення порожнє. Будь ласка, опишіть проблему більш детально.'
        )
        return

    bug_report_text = message.text
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    preview_text = f'''
📋 **Ваш репорт виглядає так:**  

⁉️ **Причина:**  
{bug_report_text}  

⏱️ **Час відправлення:**  
{current_time}  

➕ Натисніть кнопку нижче, щоб підтвердити відправлення репорта.
    '''

    markup = types.InlineKeyboardMarkup()
    send_button = types.InlineKeyboardButton("✅ Відправити репорт", callback_data=f"send_report:{bug_report_text}")
    markup.add(send_button)

    bot.send_message(
        message.chat.id,
        preview_text,
        parse_mode='Markdown',
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("send_report"))
def send_report(call):
    _, bug_report_text = call.data.split(":", 1)
    user = call.from_user

    bot.send_message(
        ADMIN_ID,
        f'''
🚨 **Новий баг-репорт:**  
Від: @{user.username or "Без імені"}  
ID користувача: {user.id}  

**Текст звіту:**  
{bug_report_text}  

Час отримання: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        ''',
        parse_mode='Markdown'
    )

    bot.send_message(
        call.message.chat.id,
        '✅ Ваш репорт успішно відправлено! Дякуємо за співпрацю. 😊'
    )


@bot.message_handler(commands=['ID'])
def ID(message):
    bot.send_message(
        message.chat.id,
        f"Ваш Telegram ID: {message.from_user.id}"
    )





while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка: {e}", exc_info=True)
