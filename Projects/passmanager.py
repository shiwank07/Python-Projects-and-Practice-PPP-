pwd = input("Enter the master password: ")

def view():
    pass

def add():
    pass

mode = input("Would like to add new password or view existing password? (add/view) or press Q to quit: ").lower()

while True:
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode. Please enter 'add', 'view', or q to quit.")
        continue

