import os
import subprocess
from cryptography.fernet import Fernet
from colors import *

if not os.path.exists(".git"):
    subprocess.run(["git", "init"])

gh_version = subprocess.run(["gh", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if gh_version.returncode != 0:
    print("GitHub CLI (gh) is not installed. Please install it.")
    exit(1)

key = os.getenv("SECRET_KEY")
if not key:
    if not os.path.exists(".key"):
        key = Fernet.generate_key()
        with open(".key", "wb") as f:
            f.write(key)
    else:
        with open(".key", "rb") as f:
            key = f.read()

try:
    fernet = Fernet(key)
except Exception as e:
    print(RED+"[-] Error: "+RESET, e)
    print(GREEN+"[+]"+GRAY+" Please delete the "+CYAN+".key"+GRAY+" file or remove the "+CYAN+ "SECRET_KEY"+GRAY+" environment variable.")
    exit(1)

secret_string = input("Enter the secret string: ")
encMessage = fernet.encrypt(secret_string.encode())

print("original string: ", secret_string)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)


# Create an issue in the repo with the secret (implement this)