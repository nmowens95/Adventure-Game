import random
DECISION = "Y/N or q to quit"
STARTING_BALANCE = 100
BUYOUT = 500
decisions = ["y", "n", "q"]

print("Hello and welcome to Life's a Gamble! 🎲🎲🎲\n")
name = input("What's your name? ")
print('')

print(f"Okay {name} the rules will be quite simple, you will wager money on your decisions and if you can manage to make enough money you can buy yourself out.\n\nI shall be your host and guide you, now....")

play_input = input(f"Do you wish to play? {DECISION} ")
if play_input.lower() == "y":
    pass
elif play_input.lower() == "n" or play_input.lower() == "q":
    print("Maybe next time then.")
    exit()
else:
    print(f"Please type {DECISION}")

print("\n")

balance = 0
start = input(f"You have woken up in an unfamiliar place, it seems to be an abandoned casino...There's an envelope with ${STARTING_BALANCE}, pick it up? {DECISION} ")
if start.lower() == "y":
    balance += STARTING_BALANCE
    print(f"Your starting balance is now {balance}. Bet for your life. If you can obtain ${BUYOUT}, you can buy yourself out...otherwise think of your money as your lifeline.")
    pass
elif start.lower() == "n" or start.lower() == "q":
        print("Then you have made your choice. The afterlife awaits you...\n\n...You are dead 😵")
        exit()
else:
     print(f"Please type {DECISION}")


print("As you look ahead of you, what you will see is a door. This is the start of the fight for your life.")
print("\n")
door1 = input("We'll start easy. Guess a number between 1 and 2, if you're right the first door will open. If not you will have to continue to wager. ")
while door1.isdigit == True:
    if door1 == 1 or door1 == 2:
        door1.randint(1, 2) == door1
        balance += 10
        print("Looks like you've made it through phase one... Here is a little reward for you. You won $10 and your balance is now {balance}")
        break
    elif door1.isdigit == False:
         print("Enter either 1 or 2")
    else:
         print("Enter either a 1 or 2")

