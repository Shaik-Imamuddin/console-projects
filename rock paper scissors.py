import random
options=("rock","paper","scissors")
while True:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("Enter a choice (rock, paper, scissors):")
    print(f"player:{player}")
    print(f"computer:{computer}")

    if player==computer:
        print("It's a Tie!!!")
    elif player=="rock" and computer=="scissors":
        print("You win!!!")
    elif player=="paper" and computer=="rock":
        print("You win!!!")
    elif player=="scissors" and computer=="paper":
        print("You win!!!")
    else:
        print("Computer win!!!")
    play=input("play Again?(yes/no):").lower()
    if play=="no":
        break
print("Thank you for playing!!!")
