master_pwd = input("What is the master password？")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            website, userId, password = data.split("|")
            print("Website or app: ", website, "| User name or ID: ", userId, "| Password: ", password)


def add():
    name = input('website or app name: ')
    user_id = input('user name or ID: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + user_id + "|" + pwd + "\n")

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
