from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

# master_password = input("Please enter your master password: ")
key= load_key() # + master_password.encode() converts into bytes and add to load_key()
fer = Fernet(key)   

''' key + password + text to encrypt = random text
random text + key + password = text to encrypt'''

def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print("User:",user,", Password:",fer.decrypt(passw.encode()).decode()) #adding and decrypting the password for our reference

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt",'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() +"\n") #adding and encrypting the password

while True:
    mode = input("Do you want to view or add passwords?(view/add) or enter 'q' to Quit: ")

    if mode == "q":
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Input Invalid")
    