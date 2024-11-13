import random

while True:

    user_pick = input("Lets play rock, paper, sissors! What do you pick?: ").strip().lower()
    computer_pick = random.randint(1,3)

    print(f"Player picks: {user_pick.upper()}")

    if(computer_pick == 1):
        print("Computer picks: ROCK")
        computer_pick = "rock"
    elif(computer_pick == 2):
        print("Computer picks: PAPPER")
        computer_pick = "papper"
    else:
        print("Computer picks: SISSORS")
        computer_pick = "sissors"

    def whoWins():
        if user_pick == "rock" and computer_pick == "rock":
            print("DRAW")
        elif user_pick == "rock" and computer_pick == "papper":
            print("COMPUTER WINS")
        elif user_pick == "rock" and computer_pick == "sissors":
            print("PLAYER WINS")

        elif user_pick == "papper" and computer_pick == "rock":
            print("PLAYER WINS")
        elif user_pick == "papper" and computer_pick == "papper":
            print("DRAW")
        elif user_pick == "papper" and computer_pick == "sissors":
            print("COMPUTER WINS")

        elif user_pick == "sissors" and computer_pick == "rock":
            print("COMPUTER WINS")
        elif user_pick == "sissors" and computer_pick == "papper":
            print("PLAYER WINS")
        elif user_pick == "sissors" and computer_pick == "sissors":
            print("DRAW")

    whoWins()
    play_again = str(input("Play again? (y/n): ")).strip().lower()

    if play_again == "n":
        break

