DECISION = "Y/N or q to quit"
STARTING_BALANCE = 100
BUYOUT = 500

print("Hello and welcome to Life's a Gamble! 🎲🎲🎲\n")
name = input("What's your name? ")
print('')

print(f"Okay {name} the rules will be quite simple, you will wager money on your decisions and if you can manage to make enough money you can buy yourself out.\n\nI shall be your host and guide you, now....")

play = input(f"Do you wish to play? {DECISION} ")
if play.lower == "N" or play.lower =="Q":
    exit
pass
print("\n")

balance = 0
start = input(f"You have woken up in an unfamiliar place, it seems to be an abandoned casino...There's an envelope with $100, pick it up? {DECISION} ")
if start.lower == "Yes":
    balance += STARTING_BALANCE
    print(f"Your starting balance is now {balance}. Bet for your life. If you can obtain ${BUYOUT}, you can buy yourself out...otherwise think of your money as your lifeline.")
elif start.lower == "No":
        print("Then you have made your choice. The afterlife awaits you...\n\n...You are dead 😵")
        quit
else:
     if start.lower == "Q":
        quit