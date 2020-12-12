from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Developer 🔥", url="https://t.me/kalam_company")],
        [InlineKeyboardButton(
            "💬 Feedback 💬", url="https://t.me/kalam_feedback_bot")]
    ])
    welcomed = f"Welcome <b>{message.from_user.first_name}</b>\n\n<b>I'm A Simple But POWERFUL You Tube URL Uploader Bot With Permanent Thumbnail Support!!! 💯</b> \n\n<b>Please send me a You Tube video Link (or) Share me a Video from You Tube, I can upload to telegram as File/Video</b> \n\n 👉 <a href="https://t.me/Kalam_url_Bot">My God Father can do lot of Things more than Me...</a> 💯 \n\n/help for more details about me..."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
