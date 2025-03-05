from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        '''

def load_key():
    file = open("secret.key", "rb")
    key = file.read()
    file.close()
    return key
    
key = load_key() 
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print(f"User: {user} , Password:", fer.decrypt(passw.encode()).decode())
            
def add():
    name = input("Enter the name of the account: ")
    pwd = input("Enter the password of the account: ")

    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

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


