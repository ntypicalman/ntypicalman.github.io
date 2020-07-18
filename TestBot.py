import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix = '*')

@Bot.event
async def on_raw_reaction_add(payload):
    #Для удобства
    message_id = payload.message_id 
    emoji = payload.emoji.name

    if message_id == 734081585317412945: #Тут ставим id нашего сообщения
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, Bot.guilds)

        if emoji == '🌑':
            role = discord.utils.get(guild.roles, name = 'Member')
        elif emoji == '🌕':
            role = discord.utils.get(guild.roles, name = 'Moderator')
        elif emoji == '🌌':
            role = discord.utils.get(guild.roles, name = 'muted')
        elif emoji == '❤️':
            role = discord.utils.get(guild.roles, name = 'Administrator')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members) #Находим того, кто реакцию нажал
            if member is not None:
                await member.add_roles(role)

@Bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    emoji = payload.emoji.name

    if message_id == 734081585317412945:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, Bot.guilds)

        if emoji == '🌑':
            role = discord.utils.get(guild.roles, name = 'Member')
        elif emoji == '🌕':
            role = discord.utils.get(guild.roles, name = 'Moderator')
        elif emoji == '🌌':
            role = discord.utils.get(guild.roles, name = 'muted')
        elif emoji == '❤️':
            role = discord.utils.get(guild.roles, name = 'Administrator')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)

#token
Bot.run('NzA1MTE4MDU4MTkyMDQ0MTE0.Xqxe1g.1RDmbI0fyIGJ0x_OpFU4buGizOo')