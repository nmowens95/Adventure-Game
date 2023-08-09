import random

DECISION = "Y/N or q to quit"
STARTING_BALANCE = 100
BUYOUT = 400
new_line = "\n"
decisions = ["y", "n", "q"]


print("Hello and welcome to Life's a Gamble! 🎲🎲🎲\n")
name = input("What's your name? ")
print('') 
print(f"Okay {name} the rules will be quite simple, you will wager money on your decisions and if you can manage to make enough money you can buy yourself out.\n\nI shall be your host and guide you, now....")


def play():
    while True:
        play_input = input(f"{new_line}Do you wish to play? {DECISION} ")   
        if play_input.lower() not in decisions:
            print(f"{new_line}Please type {DECISION}")
            continue
        elif play_input.lower() == "y":
            break
        else:
            if play_input.lower() == "n" or play_input.lower() == "q":
                print("Maybe next time then.")
                exit()
play()

def start():
    while True:
        play_input = input(f"{new_line}You have woken up in an unfamiliar place, it seems to be an abandoned casino...There's an envelope with ${STARTING_BALANCE}, pick it up? {DECISION} ")
        if play_input.lower() == "y":
            balance = 0
            balance += STARTING_BALANCE
            print(f"{new_line}Your starting balance is now {balance}. Bet for your life. If you can obtain ${BUYOUT}, you can buy yourself out...otherwise think of your money as your lifeline.")
            break
        elif play_input.lower() == "n" or play_input.lower() == "q":
            print(f"Then you have made your choice. The afterlife awaits you...{new_line}{new_line}...You are dead 😵")
            exit()
        else:
            if play_input.lower() not in decisions:
                print(f"{new_line}Please type {DECISION}")
                continue
    return balance


def obstacle1():
    balance = int(start())
    print(f"{new_line}As you look ahead of you, what you will see is a door. This is your beginning.")
    random_num = random.randint(1, 2)
    print(f"{new_line}We'll start easy. Guess a number between 1 and 2, if you're right the first door will open. If not you will have to continue to wager. ")
    while True:
        if balance <= 0:
            print(f"{new_line}Life is money and yours is up.\n\n...You are dead😵")
            quit()
        guess = input(f"{new_line}Pick 1 or 2: ")
        if guess.isdigit():
            guess = int(guess)
            if guess == random_num:
                balance += 10
                print(f"{new_line}Looks like you've made it through phase one... Here is a little reward for you. You won $10 and your balance is now ${balance}")
                break
            elif guess != random_num:
                balance -= 5
                print(f"{new_line}Guess you'll have to try again....your balance is now ${balance}")
                continue
            else:
                print(f"{new_line}Enter either 1 or 2: ")
                continue
    return balance


def obstacle2():
    balance = int(obstacle1())
    print(f"{new_line}Good, now in this room there is a slot machine with only one column. Take a guess on the choices. The buy in is now $20")
    print(f"{new_line}You may choose between: King/Queen/Jack ")
    slot_options = ["king", "queen", "jack"]
    random_guess = random.randint(0, 2)
    slot = slot_options[random_guess]
    while True:
        if balance <= 0:
            print(f"{new_line}Life is money and yours is up.\n\n...You are dead😵")
            quit()
        guess = input(f"{new_line}Pick: King/Queen/Jack ")
        if guess.lower() == slot:
            balance += 40
            print(f"{new_line}That's your 2nd obstacle... Here is a little reward for you. You won $40 and your balance is now ${balance}")
            break
        elif guess.lower != slot:
            balance -= 20
            print(f"{new_line}Guess you'll have to try again....your balance is now ${balance}")
            continue
        else:
            print(f"{new_line}Enter King/Queen/Jack: ")
            continue
    return balance


def obstacle3():
    balance = int(obstacle2())
    print(f"{new_line}Ahh luck may be with you. Lets up the ante to $50.")
    print(f"{new_line}On the table to your right is a dice cube. Pick odds or evens: ")
    dice_roll = random.randint(1, 6)
    even = dice_roll % 2 == 0
    odd = dice_roll % 1 == 1
    while True:
        if balance <= 0:
            print(f"{new_line}Life is money and yours is up.\n\n...You are dead😵")
            quit()
        guess = input(f"{new_line}Pick between 1 and 6: ")
        if guess == even or guess == odd:
            balance += 80
            print(f"{new_line}That's your 2nd obstacle... Here is a little reward for you. You won $40 and your balance is now ${balance}")
            break
        elif guess != even or guess != odd:
            balance -= 50
            print(f"{new_line}Guess you'll have to try again....your balance is now ${balance}")
            continue
        else:
            print(f"{new_line}Enter betweeen 1 and 6: ")
            continue
    return balance
obstacle3()