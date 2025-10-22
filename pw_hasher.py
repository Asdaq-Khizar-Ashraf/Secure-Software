import bcrypt

#store passrord
password = 'password123'

#convert password to an array of bytes
encode('utf-8')

#Generate the Salt
salt = bcrypt.gensalt()

hash = bcrypt.hashpw(bytes, salt)

print(hash)