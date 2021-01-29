p1 = input("Player1: Rock/Paper/ Scissor ? : ")
p2 = input("Player2: Rock/Paper/ Scissor ? : ")

if p1 == 'Paper' and p2 == 'Rock':
    print("Player 1 is the Winner!")
elif p1 == 'Rock' and p2 == 'Scissor':
    print("Player 1 is the Winner!")
elif p1 == 'Scissor' and p2 == 'Paper':
    print("Player 1 is the Winner!")
elif p1 == 'Paper' and p2 == 'Scissor':
    print("Player 2 is the Winner!")
elif p1 == 'Rock' and p2 == 'Paper':
    print("Player 2 is the Winner!")
elif p1 == 'Scissor' and p2 == 'Rock':
    print("Player 2 is the Winner!")
else:
    print("Rematch!!")
