import discord
import dex_commands

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!dex list":

        user_dex = dex_commands.get_dex(message.author.name)
        if len(user_dex) == 0:
            msg = "Oh? There aren't any pokemon in your dex yet! Why don't you try !dex add 'pokemon name here'"
        else:
            msg = user_dex

        await client.send_message(message.channel, msg)

    if message.content == "!get my name":
        await client.send_message(message.channel, message.author.name)

client.run('NTU2ODQ2ODAwMTQxNjgwNjQw.D2_8ww.zRzoHJrjb5WdawlfalW4Fxe1WV8')