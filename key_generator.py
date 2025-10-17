'''Generates an Encryption Key'''

#Import the required modules
from cryptography.fernet import Fernet

#Generate a Key
key = Fernet.generate_key()

#Write the key to a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)