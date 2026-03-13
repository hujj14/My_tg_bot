import sqlite3
import telebot
import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from tgToken import tgToken
from parser import Parser

scheduler = BackgroundScheduler()
bot = telebot.TeleBot(tgToken)
DB_PATH="data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE timetable (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Monday TEXT,
            Tuesday TEXT,
            Wednsday TEXT,
            Thursday TEXT,
            Friday TEXT,
            Saturday TEXT,
            Sunday TEXT
                
        )
    """)
    conn.commit()
    conn.close()

def insertDB():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO timetable (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) VALUES (?, ?, ?, ?, ?, ?, ?)",
                ("A|J-19:00, I-21:00","", "M-17:00, A|M-21;00,", "F-19:00", "A|J-19:00, I-21:00", "F|2-17:00", "M|2-13:00, I-21:00"))
    conn.close()

def sendmessage():
    daytoday = datetime.now().strftime("%A")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    quary = f"SELECT {daytoday} FROM timetable"
    cur.execute(quary)
    rows = cur.fetchall()

    conn.close()
    return rows

init_db()
insertDB()

@bot.message_handler(commands={"start"})
def main(message):
    bot.send_message(message.chat.id,"hello")

scheduler.add_job(sendmessage,"cron", hour=15, minutes=0)


bot.polling(non_stop=True)