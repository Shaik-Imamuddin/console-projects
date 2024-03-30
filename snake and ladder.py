import random

ladder={4:38,9:27,21:42,32:66,44:78,59:89,77:95,82:97}

snakes={23:5,34:13,39:17,46:28,55:31,62:26,71:39,81:53,88:6,98:57}

pos1=0
pos2=0

def move(pos):
    dice=random.randint(1,6)
    print(f"Dice value:{dice}")
    pos+=dice
    if pos in snakes:
        print("Snake Bite")
        pos=snakes[pos]
        print(f"position:{pos}")
    elif pos in ladder:
        print("Ladder climf")
        pos=ladder[pos]
        print(f"position:{pos}")
    else:
        print(f"position:{pos}")
    print("\n")
    return pos
while True:
    player1=input("Player 1: Enter \"1\" to throw dice:")
    pos1=move(pos1)
    if pos1>100:
        print("Game Over!!!!\nPlayer 1 Won")
        break
    player2=input("Player 2: Enter \"2\" to throw dice:")
    pos2=move(pos2)
    if pos2>100:
        print("Game Over!!!!\nPlayer 2 Won")
        break
