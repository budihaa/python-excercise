# Create basic paper rock scissors games
player1 = input("Enter Player 1's choice: ")

print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")
print("* * * NO CHEATING * * *")

player2 = input("Enter Player 2's choice: ")


# if player1 == "rock" and player2 == "paper":
#     print("Player 2 wins!")
# elif player1 == "scissors" and player2 == "paper":
#     print("Player 1 wins!")
# elif player1 == "rock" and player2 == "scissors":
#     print("Player 1 wins!")
# elif player1 == "paper" and player2 == "scissors":
#     print("Player 2 wins!")
# elif player1 == "scissors" and player2 == "rock":
#     print("Player 2 wins!")
# elif player1 == "paper" and player2 == "rock":
#     print("Player 1 wins!")
# elif player1 == player2:
#     print("It's a tie!")
# else:
#     print("Error!")

# Refactoring that code ^
if player1 == player2:
    print("Its a tie")
elif player1 == "rock":
    if player2 == "paper":
        print("Player 2 wins")
    elif player2 == "scissors":
        print("Player 1 wins")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins")
    elif player2 == "scissors":
        print("Player 2 wins")
elif player1 == "scissors":
    if player2 == "rock":
        print("Player 2 wins")
    elif player2 == "paper":
        print("Player 1 wins")
else:
    print("error")
