import random
import string


def GetPassword(length):
    password_char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_char) for i in range(length))
    print("Your Password is: ", password)


strength = input("How strong do you want your password to be? Select among Strong/ Medium/ Weak : ").upper()

if strength == 'STRONG':
    length_strong = random.randint(15, 25)
    GetPassword(length_strong)
elif strength == 'MEDIUM':
    length_medium = random.randint(8,15)
    GetPassword(length_medium)
elif strength == 'WEAK':
    length_weak = random.randint(4, 8)
    GetPassword(length_weak)
else:
    print("I do not understand, please try again!")