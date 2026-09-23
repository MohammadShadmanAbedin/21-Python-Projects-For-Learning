from pathlib import Path

# Install dependency: python -m pip install cryptography
from cryptography.fernet import Fernet




def write_key():
    key = Fernet.generate_key()

    file_path = Path(__file__).parent / "key.key"

    with open(file_path, "wb") as key_file:
        key_file.write(key)

key_file = Path(__file__).parent / "key.key"

if not key_file.exists():
    write_key()




def load_key():
    file_path = Path(__file__).parent / "key.key"
    file = open(file_path, "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is your master password: ")

key=load_key()
fer=Fernet(key)


def view():
    file_path = Path(__file__).parent / "passwords.txt"

    with open(file_path, "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    file_path = Path(__file__).parent / "passwords.txt"

    with open(file_path, "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones?(view,add), press q to quit :"
    ).lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
