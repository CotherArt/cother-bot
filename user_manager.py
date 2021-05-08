import os, ast
from colorama import Fore, Style, init

init(autoreset=True)
debug_mode = True

def debug(msg):
    if debug_mode:
        print(msg)

class User:
    dict = {}

    def make_users_dir(self):
        # creates the users/ directory if it not exists
        if not 'users' in os.listdir():
            os.mkdir('users')
            debug(Fore.GREEN + 'users folder created')

    # return True if a userid is on the users folder
    def user_exist(self, userid):
        self.make_users_dir()
        userslist = os.listdir('users/')
        return (userid+'.txt') in userslist

    # save a user on the users/ directory
    def save_user(self):
        self.make_users_dir()
        if self.dict['userid'] == '':
            debug(Fore.RED + 'Error at saving user. User has no userid')
            return

        with open('users/' + self.dict['userid'] + '.txt', 'w') as file:
            file.write(str(self.dict))
            debug(Fore.GREEN + 'User saved!')
    
    # returns the dict from a user on user/ folder
    def load_user(self, userid):
        self.make_users_dir()
        if not self.user_exist(userid):
            debug(Fore.RED + 'User' + userid + ' not found')
            return

        with open('users/'+userid+'.txt') as file:
            data = file.read()
        
        # converts str data to a dict type
        d = ast.literal_eval(data)
        debug(Fore.GREEN + 'User loaded from the users folder')
        return d

    # get and set functions -----------------------------------------------
    def get_dic(self):
        return self.dict

    def get_username(self):
        return self.dict['username']

    def get_voice_level(self):
        if 'voice_level' not in self.dict.keys():
            self.dict['voice_level'] = 0
        return self.dict['voice_level']
        
    
    def get_text_level(self):
        if 'text_level' not in self.dict.keys():
            self.dict['text_level'] = 0
        return self.dict['text_level']
    
    def set_username(self, username):
        self.dict['username'] = username
    
    def set_voice_level(self, level):
        self.dict['voice_level'] = level

    def set_text_level(self, level):
        self.dict['text_level'] = level
        
    # contructors and destructors--------------------------------------------
    # loads the user from the users/ dir if it exist, and create it if it not
    def __init__(self, userid, username):
        if self.user_exist(userid):
            self.dict = self.load_user(userid)
            # updates the username if it changes
            if self.dict['username'] != username:
                self.dict['username'] = username
                debug(Fore.GREEN + 'username updated!')
        else:
            debug(Fore.GREEN + 'New user created!')
            self.dict = {'userid': userid, 'username': username}
            self.save_user()

    def __del__(self):
        self.save_user()

def main():
    usr = User('owouser123', 'Cother#1234')
    print(usr.get_voice_level())
    print(usr.get_text_level())
    print(usr.get_dic())


if __name__ == '__main__':
    main()
