from pyrogram import Client
from pyrogram import filters
from random import shuffle
from kelime_bot import USERNAME
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("cancel") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f"{i}   :   {oyun[m.chat.id]['oyuncular'][i]} Bal")
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**{m.from_user.mention}** Tarafından Oyun Bitirildi\n\nYeni Oyuna Başlamak İçin /turet Yaza Bilirsiniz\n\n 📝 Puan Listesi  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
    
