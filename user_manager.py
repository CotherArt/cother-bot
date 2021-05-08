import json, os, ast

class User:

    def __init__(self):
        # creates the users/ directory if it not exists
        if not 'users' in os.listdir():
            os.mkdir('users')

        self.dict = {
            'userid': '',
            'name': '',
            'xp': 0,
            'level': 0
        }

    # return True if a userid is on the users folder
    def exist(self, userid):
        userslist = os.listdir('users/')
        return (userid+'.txt') in userslist
    def save_user(self):
        if self.dict['userid'] == '':
            print('User has no userid')
            return

        with open('users/' + self.dict['userid'] + '.txt', 'w') as file:
            file.write(str(self.dict))
    
    def open_user(self, userid):
        if not self.exist(userid):
            print('User' + userid + ' not found')
            return

        with open('users/'+userid+'.txt') as file:
            data = file.read()
            
        d = ast.literal_eval(data)
        self.dict = d

    def new_user(self, userid, username):
        self.dict['userid'] = userid
        self.dict['name'] = username

def main():
    usr = User()
    usr.open_user('usuario')
    print(usr.toString())


if __name__ == '__main__':
    main()
