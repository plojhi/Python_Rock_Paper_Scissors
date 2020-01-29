# Write your code here
import random

players = {}
with open("rating.txt") as rating:
    for line in rating:
        (key, val) = line.split()
        players[key] = int(val)

name = input("Enter your name: ")
print(f"Hello, {name}")

game = input()
if game == "":
    options = ["rock", "paper", "scissors"]
else:
    options = game.split(",")

print("Okay, let's start")

while True:

    computer = random.choice(options)
    player = input()

    if player == computer:
        print(f"There is a draw ({player})")
        players[name] += 50
    elif player in options:
        options2 = options * 2

        for words in range(len(options2)):
            if options2[words] == player:
                win = options2[(words+1):(words + 1 + len(options)//2)]     # The player won


                lost = options2[(words + 1+ len(options)//2):(words + 1 + 2 * (len(options)//2))]           # The player lost


                if computer in lost:
                    print(f"Well done. Computer chose {computer} and failed")
                    players[name] += 100

                if computer in win:
                    print(f"Sorry, but computer chose {computer}")
                break
    elif player == "!exit":
        break
    elif player == "!help":
        print("rock beats scissors, scissors beat paper, paper beat rock")
    elif player == "!rating":
        print("Your rating:", int(players[name]))
print("Bye!")

with open("rating.txt", "w") as f:
    for i in players:
        f.write(f"{i} {players[i]}\n")

