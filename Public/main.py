# -==== Import Things ====- #

import discord
import random
import json
from discord.ext import commands

# Prepare to Start #

client = commands.Bot(command_prefix = '<')
client.remove_command('help')

# 2021 EpicGiant
#  __        __    _ _
#  \ \      / /_ _| | |_ ___ _ __ ___  __ _ _ __ _   _ ___
#   \ \ /\ / / _` | | __/ _ \ '__/ __|/ _` | '__| | | / __|
#    \ V  V / (_| | | ||  __/ |  \__ \ (_| | |  | |_| \__ \
#     \_/\_/ \__,_|_|\__\___|_|  |___/\__,_|_|   \__,_|___/

# -==== Start Sequence ====- #

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f",help | dsc.gg/waltersaurus"))
    print('Waltersaurus is ready.')

# -==== Moderation ====- #

@client.command()
async def clear(ctx, amount=0):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit= amount+1)
        await ctx.send(f'__Cleared *{amount}* messages.__')

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if (ctx.message.author.permissions_in(ctx.message.channel).kick_members):
        await member.kick(reason=reason)

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if (ctx.message.author.permissions_in(ctx.message.channel).ban_members):
        await member.ban(reason=reason)

# -==== Commands Reagarding Waltersaurus ====- #

@client.command()
async  def invite(ctx):
    await ctx.message.author.send('Invite Waltersaurus to your server at **https://dsc.gg/invwlt**')

@client.command()
async def join(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        description = 'Press the above button to join to the Official Waltersaurus Community Discord Server.',
        colour = discord.Colour.blue(),
    )

    embed.set_author(name='Click to join', url='https://discord.gg/8bXFmFsCE2', icon_url='https://cdn.discordapp.com/attachments/848282294979788800/848282726880116746/logo.png')

    await author.send(embed=embed)

@client.command()
async def github(ctx):
    await ctx.message.author.send('View the github respository of Waltersaurus at https://github.com/EpicGiant27/Waltersaurus.')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        description = 'List of commands and how to use them.',
        colour = discord.Colour.blue(),
    )

    embed.set_author(name='Waltersaurus Help', url='https://discord.gg/8bXFmFsCE2', icon_url='https://cdn.discordapp.com/attachments/848282294979788800/848282726880116746/logo.png')
    embed.add_field(name=',help', value='Sends you this message.', inline=False)
    embed.add_field(name=',info', value='Displays info about the bot.', inline=False)
    embed.add_field(name=',invite', value='Send you a direct message containing the invite link for Waltersaurus.', inline=False)
    embed.add_field(name=',github', value='Sends you a link to the github respository containing Waltersaurus.', inline=False)
    embed.add_field(name=',join & ,server', value='Sends you a direct message containing the invite link to the Waltersaurus Community server.', inline=False)
    embed.add_field(name=',clear [number]', value='Clears a specified amount of messages. (NOTE: Requires delete messages permission.)', inline=False)
    embed.add_field(name=',kick [mention]', value='Kicks the mentioned member. (NOTE: Requires kick members permission.)', inline=False)
    embed.add_field(name=',ban [mention]', value='Bans the mentioned member. (NOTE: Requires bans members permission.)', inline=False)

    await author.send(embed=embed)

client.run('TOKEN')
