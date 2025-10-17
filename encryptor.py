#Import the required modules
from cryptography.fernet import Fernet

#Open the Key File
with open('filekey.key','rb') as filekey:
    key = filekey.read()

#Use the Key
fernet = Fernet(key)

#Open file to be encrypted
with open('Video provides a powerful way to help you prove your point.docx','rb') as file:
    unencrypted = file.read()

#Encrypt the data
encrypted = fernet.encrypt(unencrypted)

#Write the encrypted data
with open('Video provides a powerful way to help you prove your point.docx','wb') as encrypted_file:
    encrypted_file.write(encrypted)
