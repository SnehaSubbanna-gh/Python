import random

r = random.randint(1,9)
j = 0
while True:
    guess = input('Guess the number : ')
    j = j+1
    if int(guess) == r:
        print("You Win!!")
        break
    elif guess == 'Exit' or 'exit':
        break
    else:
        print("Try again!")

print (f'You took {j} chances to guess the number. The number is {r}')