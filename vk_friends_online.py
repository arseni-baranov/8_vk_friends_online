import vk
import getpass

APP_ID = -1

def get_user_login():
    return input('Enter user login/mobile: ')


def get_user_password():
    return getpass.getpass('Enter user password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    

    friend_ids = api.friends.getOnline()

    return api.users.get(user_ids=friend_ids)


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':

    while True:        
        try:
            login = get_user_login()
            password = get_user_password()
        except:
            print('Authorization error. Please re-enter login and password')
        else:
            friends_online = get_online_friends(login, password)
            print()
            print('Friends online:')
            print()
            output_friends_to_console(friends_online)
            break
