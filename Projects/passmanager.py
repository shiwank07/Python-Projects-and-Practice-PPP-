master_pwd = input("Enter the master password: ")

def view():
    pass

def add():
    name = input("Enter the name of the account: ")
    pwd = input("Enter the password of the account: ")

    with open('password.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')

while True:
    mode = input("Would like to add new password or view existing password? (add/view) or press Q to quit: ").lower()
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode. Please enter 'add', 'view', or q to quit.")
        continue


