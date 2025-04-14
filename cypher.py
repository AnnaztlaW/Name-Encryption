# This is the encrypting and decryption of the of the cypher
# No peeking unless you really need the answer
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# If your looking here you must want an answer!
# This is a caeser cypher!!!!
import random
secret_key = 0

def encrypt(text, redo =False):
    # this generate the key for encryption
    global secret_key
    if secret_key == 0 or redo:
        secret_key = random.randint(1, 25)
    result = ""
    # print(secret_key) #this will give you the key if uncommented 
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + secret_key) % 26 + shift)
        else:
            result += char
    return result

def correctGuess(guess):
    global secret_key
    return guess == secret_key

def decrypt(text):
    global secret_key
    secret_key = (-secret_key)
    return encrypt(text)
