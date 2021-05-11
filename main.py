import discord
from os import listdir
from user_manager import User
from colorama import init, Fore, Style

init(autoreset=True)
debug_mode = True

xp_per_msg = 30

def debug(msg):
    if debug_mode:
        print(msg)


class Cother_bot(discord.Client):

    async def on_ready(self):
        print('Logged on as ' + Fore.YELLOW + '{0}'.format(self.user))

    async def on_message(self, message):
        # print('Message from {0.author}: {0.content}'.format(message))

        # do nothing if the message is from the bot
        if message.author == self.user:
            return

        # message properties
        username_short = str(message.author).split('#')[0]
        username = str(message.author)
        userid = str(message.author.id)
        user_message = str(message.content)
        channel = str(message.channel.name)

        # print the message
        debug(Fore.LIGHTBLUE_EX +
              f'{username_short}: {user_message} ({channel})')

        # work only on cother-bot-test channel
        if message.channel.name == 'cother-bot-test':
            pass

        # replies to the author of the command
        if message.content.startswith('!cother'):
            await message.reply('Tu puta madre {}'.format(username_short), mention_author=True)

        # deletes all the messages on a channel
        if message.content.startswith('!purga'):
            deleted = await message.channel.purge(limit=100)
            await message.channel.send('Deleted {} message(s)'.format(len(deleted)))

        user = User(userid, username)
        user.add_text_xp(xp_per_msg)
        if user_message.startswith('!stats'):
            await message.reply(user.toString(), mention_author=True)

def discord_token():
    if 'bot_key' in listdir():
        with open('bot_key', 'r') as file:
            debug(Fore.GREEN + 'bot_key loaded')
            token = file.read()
            return token
    else:
        debug(Fore.RED + 'bot_key not found')
        token = input('Put the bot key here: ')
        with open('bot_key', 'w') as file:
            file.write(token)
        return token
    
    
def main():
    client = Cother_bot()
    client.run(discord_token())


if __name__ == '__main__':
    main()
