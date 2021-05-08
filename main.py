import discord
from user_manager import User
from colorama import init, Fore, Style
from discord_token import token  # my discord key

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


def main():
    client = Cother_bot()
    client.run(token)


if __name__ == '__main__':
    main()
