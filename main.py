import discord
from user_manager import User
from colorama import init, Fore, Style
from client_token import token

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
        
        # diferent vehaviors in diferent channels
        if channel == 'cother-bot-test':
            print('esatan escribiendo en mi canal >:(')

            usuario = User()
            if usuario.exist(userid):
                usuario.open_user(userid)                
            else: 
                usuario.new_user(userid, username)
                usuario.save_user()

            print(usuario.toString())


        if message.content.startswith('!cother'):
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
