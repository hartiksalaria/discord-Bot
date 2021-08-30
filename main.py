import discord
from gtts import gTTS
import os
from google_trans_new import google_translator

translator = google_translator()
token = "ODUyODQ2OTE0ODk4ODg2NjU4.YMMxlQ.oDyVlfE5tADF0MbGX88rHdlcUgw"
client = discord.Client()

commands = {
    "hello": "Greets the user",
    "help": "Shows all the available commands",
    "say": "Converts text to speech",
    "trans": 'converts english to any language format #trans <input lang> : <text> : <output lang>'
}


@client.event
async def on_message(message):
    if str(message.content[0]) == "#":
        if message.content.lower() == "#hello":
            await message.channel.send(f"Hi {message.author.mention} 🙂")
        elif message.content.lower() == "#help":
            embedVar = discord.Embed(title="Help",
                                     description="How to use the commands\nEvery command has '#' as prefix",
                                     color=0x00ff00)
            embedVar.add_field(name="hello", value="Greets the user", inline=False)
            embedVar.add_field(name="help", value="Shows all the available commands", inline=False)
            embedVar.add_field(name="say", value="Converts text to speech", inline=False)
            embedVar.add_field(name="trans",
                               value='converts english to any language format #trans <input lang> : <text> : <output lang>',
                               inline=False)
            await message.channel.send(embed=embedVar)
        elif "#say" in message.content:
            msg = message.content
            msg = msg.replace("#say", '')
            audio = gTTS(text=msg)
            audio.save("new.mp3")
            await message.channel.send(file=discord.File("new.mp3"))
            os.remove("new.mp3")
        elif "#trans" in message.content:
            input_text = message.content.replace("#say", '')
            main_list = input_text.split(':')
            input_lang = main_list[0].strip(" ")
            output_lang = main_list[2].strip(" ")
            main_text = main_list[1]
            translated_text = translator.translate(main_text, lang_tgt=output_lang, lang_src=input_lang)
            await message.channel.send(translated_text)

        else:
            await message.channel.send(f"Not a valid command 🥲\nType  #help  to see all the commands 😃")


client.run(token)
