import discord
from user_manager import User
from colorama import init, Fore, Style
from discord_token import token #my discord key

init(autoreset=True)

class Cother_bot(discord.Client):

    async def on_ready(self):
        print('Logged on as '+ Fore.YELLOW +'{0}'.format(self.user))

    async def on_message(self, message):
        # print('Message from {0.author}: {0.content}'.format(message))

        username_short = str(message.author).split('#')[0]
        username = str(message.author)
        userid = str(message.author.id)
        user_message = str(message.content)
        channel = str(message.channel.name)

        print(f'{username_short}: {user_message} ({channel})')

        if message.author == self.user:
            return

        # work only on cother-bot-test channel
        if channel == 'cother-bot-test':
            pass

        if user_message.startswith('!cother'):
            await message.reply('Tu puta madre {}'.format(username_short), mention_author=True)

        # deletes all the messages on a channel
        if user_message.startswith('!purga'):
            deleted = await message.channel.purge(limit=100)
            await message.channel.send('Deleted {} message(s)'.format(len(deleted)))

    def is_me(self, m):
        return m.author == self.user

    

def main():
    client = Cother_bot()
    client.run(token)

if __name__ == '__main__':
    main()
