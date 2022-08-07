from config.config import app

from pyrogram import filters


@app.on_message(filters.command(["start", "start@edbo_fict_bot"]))
def greeting(client, message):
    message.reply_text(text="""
Привіт 👋

Для розрахунку непрохідного бала з усіх спеціальностей відправ мені команду /marks

Якщо хочеш дізнатись інформацію про конкретну спеціальність, тицяй: 
/121 
/123 
/126
""")