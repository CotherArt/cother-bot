import discord
import client_token #here is my client token

# client (the bot)
client = discord.Client()

# do stuff ------------------------------------------------------
@client.event
async def on_ready():
    print('Estoy loggeado como {}'.format(client.user))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    # diferent vehaviors in diferent channels
    if channel == 'cother-bot-test':
        print('esatan escribiendo en mi canal >:(')

    if message.content.startswith('!cother'):
        await message.reply('Tu puta madre {}'.format(username), mention_author=True)

@client.event
async def on_member_remove(member):
    print('{} nos ha dejado'.format(member.name))

# run the client on the server
client.run(token)

