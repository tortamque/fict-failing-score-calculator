from config.config import app
from edbo.edbo_results import *

from pyrogram import filters


@app.on_message(filters.command(["marks", "marks@edbo_fict_bot"]))
def calculate(client, message):
    result = get_result()

    message.reply_text(text=result, reply_to_message_id=message.id)


@app.on_message(filters.command(["121", "121@edbo_fict_bot"]))
def calculate_121(client, message):
    result = get_result_121()

    message.reply_text(text=result, reply_to_message_id=message.id)


@app.on_message(filters.command(["123", "123@edbo_fict_bot"]))
def calculate_123(client, message):
    result = get_result_123()

    message.reply_text(text=result, reply_to_message_id=message.id)


@app.on_message(filters.command(["126", "126@edbo_fict_bot"]))
def calculate_126(client, message):
    result = get_result_126()

    message.reply_text(text=result, reply_to_message_id=message.id)

