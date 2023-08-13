import random

DECISION = "Y/N or q to quit"
STARTING_BALANCE = 100
BUYOUT = 400
new_line = "\n"
decisions = ["y", "n", "q"]


print("Hello and welcome to Life's a Gamble! 🎲🎲🎲\n")
name = input("What's your name? ")
print('') 
print(f"(Narrator): Okay {name} the rules will be quite simple, you will wager money on your decisions and if you can manage to make enough money you can buy yourself out.\n\nI shall be your host and guide you, now....")


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
            print(f"{new_line}(Narrator): Your starting balance is now {balance}. Bet for your life. If you can obtain ${BUYOUT}, you can buy yourself out...otherwise think of your money as your lifeline.")
            break
        elif play_input.lower() == "n" or play_input.lower() == "q":
            print(f"(Narrator): Then you have made your choice. The afterlife awaits you...{new_line}{new_line}...You are dead 😵")
            exit()
        else:
            if play_input.lower() not in decisions:
                print(f"{new_line}Please type {DECISION}")
                continue
    return balance


def obstacle1():
    balance = int(start())
    print(f"{new_line}(Narrator): As you look ahead of you, what you will see is a door. This is your beginning.")
    random_num = random.randint(1, 2)
    print(f"{new_line}(Narrator): We'll start easy. Guess a number between 1 and 2, if you're right the first door will open. If not you will have to continue to wager. ")
    while True:
        if balance <= 0:
            print(f"{new_line}(Narrator): Life is money and yours is up.\n\n...You are dead😵")
            quit()
        guess = input(f"{new_line}Pick 1 or 2: ")
        if guess.isdigit():
            guess = int(guess)
            if guess == random_num:
                balance += 10
                print(f"{new_line}(Narrator): Looks like you've made it through phase one... Here is a little reward for you. You won $10 and your balance is now ${balance}")
                break
            elif guess != random_num:
                balance -= 5
                print(f"{new_line}(Narrator): Guess you'll have to try again....your balance is now ${balance}")
                continue
            else:
                print(f"{new_line}Enter either 1 or 2: ")
                continue
    return balance


def obstacle2():
    balance = int(obstacle1())
    print(f"{new_line}(Narrator): Good, now in this room there is a slot machine with only one column. Take a guess on the choices. The buy in is now $20")
    print(f"{new_line}(Narrator): You may choose between: King/Queen/Jack ")
    slot_options = ["king", "queen", "jack"]
    random_guess = random.randint(0, 2)
    slot = slot_options[random_guess]
    while True:
        if balance <= 0:
            print(f"{new_line}(Narrator): Life is money and yours is up.\n\n...The royalty from the cards emerge from nowhere and cover your face...you are now dead😵")
            quit()
        guess = input(f"{new_line}Pick: King/Queen/Jack ")
        if guess.lower() == slot:
            balance += 40
            print(f"{new_line}(Narrator): That's your 2nd obstacle... Here is a little reward for you. You won $40 and your balance is now ${balance}")
            break
        elif guess.lower != slot:
            balance -= 20
            print(f"{new_line}(Narrator): Guess you'll have to try again....your balance is now ${balance}")
            continue
        else:
            print(f"{new_line}Enter King/Queen/Jack: ")
            continue
    return balance

# The way the even's and odds work is clunky. Plus it feels as if it is similar to obsacle one
def obstacle3():
    balance = int(obstacle2())
    print(f"{new_line}(Narrator): Ahh luck may be with you. Lets up the ante to $50.")
    print(f"{new_line}(Narrator): On the table to your right is a dice cube. Roll the dice and for this the name of the game is odds or evens. ")
    dice_roll = random.randint(1, 6)
    even = dice_roll % 2 == 0
    odd = dice_roll % 1 == 1
    while True:
        if balance <= 0:
            print(f"{new_line}(Narrator): Life is money and yours is up.\n\n...The dice grows 100,000 fold and rols over you...you are now dead😵")
            quit()
        guess = input(f"{new_line}Pick either 1 for odds or 2 for evens: ")
        if int(guess) == even or int(guess) == odd:
            balance += 80
            print(f"{new_line}(Narrator): ...Lucky enough. Your roll worked in your favor. Here is a little reward for you. You won $80 and your balance is now ${balance}")
            break
        elif int(guess) != even or int(guess) != odd:
            balance -= 50
            print(f"{new_line}(Narrator): Oh no looks like the dice isn't your kind of game!....your balance is now ${balance}")
            continue
        else:
            print(f"{new_line}Pick either 1 for odds or 2 for evens: ")
            continue
    return balance

# Need to create a new obstacle entirely, this is still obstacle 3 code
def obstacle4():
    balance = int(obstacle3())
    print(f"{new_line}(Narrator): Ahh luck may be with you. Lets up the ante to $50.")
    print(f"{new_line}(Narrator): On the table to your right is a dice cube. Roll the dice and for this the name of the game is odds or evens. ")
    dice_roll = random.randint(1, 6)
    even = dice_roll % 2 == 0
    odd = dice_roll % 1 == 1
    while True:
        if balance <= 0:
            print(f"{new_line}(Narrator): Life is money and yours is up.\n\n...The dice grows 100,000 fold and rols over you...you are now dead😵")
            quit()
        guess = input(f"{new_line}Pick either 1 for odds or 2 for evens: ")
        if int(guess) == even or int(guess) == odd:
            balance += 80
            print(f"{new_line}(Narrator): ...Lucky enough. Your roll worked in your favor. Here is a little reward for you. You won $80 and your balance is now ${balance}")
            break
        elif int(guess) != even or int(guess) != odd:
            balance -= 50
            print(f"{new_line}(Narrator): Oh no looks like the dice isn't your kind of game!....your balance is now ${balance}")
            continue
        else:
            print(f"{new_line}Pick either 1 for odds or 2 for evens: ")
            continue
    return balance

def obstacle5():
    balance = int(obstacle4())
    print(f"{new_line}*** A staircase in the corner of the room slides open revealing a passageway into the basement ***{new_line}")
    print(f"{new_line}(Narrator): Take the passage ahead.")
    print(f"{new_line}*** As you walk in you see the remnants of a bar...behind the counter is an old worn down mechanical bartender. ***")
    print(f"{new_line}(Narrator): This one is my favorite. We are truly betting on life itself this time. {new_line}You will have 3 drinks to choose from. Only one option isn't poisoned and this time the buy in is priceless, your taste will determine the price.")
    while True:
        if balance <= 0:
            print(f"{new_line}(Narrator): Life is money and yours is up.\n\n...You have drank the poison and now have died 😵")
            quit()
        if balance >= BUYOUT:
            print(f"{new_line}(Narrator): Life is money and you are overflowing with wealth. {new_line}{new_line}*** A platform lifts you to the roof of a building surrounded by water, at the top is a helicopter ***{new_line}{new_line}You've done it, you've won the game: Life's a Gamble!!!")
            quit()
        guess = input(f"{new_line}Pick either Whiskey, Water or Gin: ")
        if guess.lower() == "whiskey":
            balance += BUYOUT
            print(f"{new_line}(Narrator): ...I admire your selection. You've won $300 and your balance is now ${balance}")
            continue
        elif guess.lower() == "water" or guess.lower() == "gin":
            balance -= balance
            print(f"{new_line}(Narrator): Oh no your taste is awful and deadly....your balance is now ${balance}")
            continue
        else:
            print(f"{new_line}Pick either Whisky, Water or Gin: ")
            continue
    return balance
obstacle5()