# Create game paper rock scissors VS Computer
from random import randint

# ============ Computer scripts ================
# randint = create random from 0 - 2
numb = randint(0, 2)

if numb == 0:
    computer = "paper"
elif numb == 2:
    computer = "rock"
else:
    computer = "scissors"

# ========== Calculate player's input with computer =============
player = input("Enter paper/rock/scissors: ")

print("You: " + player)
print("Computer: " + computer)

if player == computer:
    print("It's a tie!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("Computer's win")
elif player == "rock" and computer == "paper":
    print("Computer's win")
elif player == "scissors" and computer == "rock":
    print("Computer's win")
elif player == "paper" and computer == "scissors":
    print("Computer's win")
else:
    print("Error!")
