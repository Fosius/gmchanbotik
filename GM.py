import discord
from discord.ext import commands
import os

PREFIX = '$'
bad_words = [ 'Путин сила', 'Слава Аллаху' ]

client = commands.Bot( command_prefix = '$' )
client.remove_command ( 'help' )


hello_words = [ 'hello', 'hi', 'привет' ]
answer_words = [ 'узнать информацию о сервере', 'команды' ]


@client.event

async def on_ready():
	print( 'Доброе Утро!' )

# Filter
@client.event
async def on_message( message ):
	await client.process_commands( message )

	msg = message.content.lower()

	if msg in bad_words:
		await message.delete()
		await message.author.send( f'{message.author.name}, такие слова на нашем сервере запрещены!' )

# Clear Messages
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount )


# Kick
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )


async def kick( ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.kick( reason = reason )

# Ban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.ban( reason = reason )
	await ctx.send( f'ban user { member.mention } ' )

# Help
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def help( ctx ):
	emb = discord.Embed( title = 'Команды' )

	emb.add_field( name = '{}clear'.format( '$' ), value = 'Очистить чат' )
	emb.add_field( name = '{}kick'.format( '$' ), value = 'Исключение участника с сервера' )
	emb.add_field( name = '{}ban'.format( '$' ), value = 'Бан участника на сервере' )

	await ctx.send( embed = emb )


# Mute

@client.command()
@commands.has_permissions( administrator = True )

async def mute( ctx, member: discord.Member ):
	await ctx.channel.purge( limit = 1 )

	mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Muted' )

	await member.add_roles( mute_role )

@client.command()
async def send_a( ctx ):
	await ctx.author.send( 'Привет!' )

@client.command()
async def send_m( ctx, member: discord.Member ):
	await member.send( f'{member.name}, у нас проходит конкурс, загляни в новости!' )

@client.command()
async def allert( ctx, member: discord.Member ):
	await member.send( f'{member.name}, вы нарушили правила сервера и понесли наказание. В следующий раз будьте бдительны!' )



token = os.environ.get('BOT_TOKEN')