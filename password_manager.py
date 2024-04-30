from cryptography.fernet import Fernet

master_pwd = input("What is the master password？ ")

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            website, userId, password = data.split("|")
            print("Website or app: ", website, "| User name or ID: ", userId, "| Password: ", fer.decrypt(password.encode()).decode())

def add():
    name = input('website or app name: ')
    user_id = input('user name or ID: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + user_id + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

if master_pwd == "master" :

    key = load_key()
    fer = Fernet(key)

    while True:
        mode = input("Would you like to add a new password ot view existing ones (view, add)?, press q to quit ").lower()
        if mode == "q":
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue
else:
    print("Wrong password")
