#Import the required modules
from cryptography.fernet import Fernet

#Open the Key File
with open('filekey.key','rb') as filekey:
    key = filekey.read()

#Use the Key
fernet = Fernet(key)

#Open the encrypted file
with open('Video provides a powerful way to help you prove your point.docx','rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = fernet.decrypt(encrypted)


#Writes the decrypted the file
with open('Video provides a powerful way to help you prove your point.docx', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
    