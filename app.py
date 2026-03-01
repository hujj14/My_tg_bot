import sqlite3
import telebot
from tgToken import tgToken

DB_PATH="data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE message (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            text TEXT
            created_at INTEGER,
            chat_id INTEGET
                
        )
    """)
    conn.commit()
    conn.close()

def save_message(user_id, chat_id, text, created_at):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO messsage (user_id, chat_id, text, created_at) VALUES (?, ?, ?, ?)",
        (user_id, chat_id, text, created_at)
    )
    conn.commit()
    conn.close()

bot = telebot.TeleBot(tgToken)

init_db()

@bot.message_handler(content_types={"text"})
def main(message):
    bot.send_message(message.chat.id,"hello")
    save_message(
        user_id=message.from_user.id,
        chat_id = message.from_chat_id,
        text=message.text,
        created_at=message.date
    )
    bot.reply_to(message, "Данные записаны в базу")


bot.polling(non_stop=True)