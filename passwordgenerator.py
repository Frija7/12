import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("\Enter password length"))
password = ''
for i in range(length):
    password += random.choice(symbols)
    
print(password)
