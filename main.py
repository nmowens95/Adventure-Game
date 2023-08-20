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
        elif guess == str(guess):
                print(f"{new_line}Enter either 1 or 2: ")
                continue
        if guess > 2 or guess < 1:
            print(f"{new_line}Enter either 1 or 2: ")
            continue 
        elif guess == random_num:
            balance += 10
            print(f"{new_line}(Narrator): Looks like you've made it through phase one... Here is a little reward for you. You've won $10 and your balance is now ${balance}")
            break
        else:
            balance -= 5
            print(f"{new_line}(Narrator): Guess you'll have to try again....your balance is now ${balance}")
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
        guess = input(f"{new_line}Pick - King/Queen/Jack: ")
        if guess.lower() not in slot_options:
            print(f"{new_line}The options are - King/Queen/Jack: ")
            continue
        elif guess.lower() == slot:
            balance += 40
            print(f"{new_line}(Narrator): That's your 2nd obstacle... Here is a little reward for you. You've won $40 and your balance is now ${balance}")
            break
        else:
            balance -= 20
            print(f"{new_line}(Narrator): Guess you'll have to try again....your balance is now ${balance}")
            continue               
    return balance


def obstacle3():
    balance = int(obstacle2())
    print(f"{new_line}(Narrator): Ahh luck may be with you. This one your chances wont be so good. The anti is only $25.")
    print(f"{new_line}(Narrator): On the table to your right is a dice cube. Roll the dice and we'll see what your odds really are. ")
    dice_roll = random.randint(1, 6)
    while True:
        if balance <= 0:
            print(f"{new_line}(Narrator): Life is money and yours is up.\n\n...The dice grows 100,000 fold and rolls over you...you are now dead😵")
            quit()
        guess = input(f"{new_line}Pick a number between 1-6: ")
        if guess.isdigit():
            guess = int(guess)
        elif guess == str(guess):
            print(f"{new_line}Not quite, has to be a number between 1-6: ")
            continue
        if guess >= 7 or guess < 0:
            print(f"{new_line}Not quite, has to be a number between 1-6: ")
            continue
        if guess == dice_roll:
            balance += 80
            print(f"{new_line}(Narrator): ...Lucky enough, that's 3 down. Your roll worked in your favor. Here is a little reward for you. You've won $80 and your balance is now ${balance}")
            break
        else: 
            balance -= 25
            print(f"{new_line}(Narrator): Oh no looks like the dice isn't your kind of game!....your balance is now ${balance}")
            continue
    return balance


def obstacle4():
    balance = int(obstacle3())
    print(f"{new_line}(Narrator): You've done well thus far. This round will cost you $80.")
    print(f"{new_line}(Narrator): Now to your left is a horse race simulator. You can bet on Zues, Hercules, Helen or Aphrodite to win the race.")
    horses = ['zues', 'hercules', 'helen', 'aphrodite']
    horse_winner = random.choice(horses)
    while True:
        if balance <= 0:
            print(f"{new_line}(Narrator): Life is money and yours is up.\n\nA Horse emerges from the screen, trampling you in the process...you are now dead😵")
            quit()
        guess = input(f"{new_line}Pick between - Zeus, Hercules, Helen or Aphrodite: ")
        if guess == int:
            print(f"{new_line}The choices are... Zeus, Hercules, Helen or Aphrodite: ")
            continue
        elif guess.lower() not in horses:
            print(f"{new_line}The choices are... Zeus, Hercules, Helen or Aphrodite: ")
            continue
        if guess.lower() == horse_winner:
            balance += 120
            print(f"{new_line}(Narrator): ...HAH! This 4th was a doosey. You have a keen eye. Here is a little reward for you. You've won $120 and your balance is now ${balance}")
            break
        else:
            balance -= 80
            print(f"{new_line}(Narrator): Oh no seems you don't know horses all too well!....your balance is now ${balance}")
            continue
    return balance


def obstacle5():
    balance = int(obstacle4())
    print(f"{new_line}*** A staircase in the corner of the room slides open revealing a passageway into the basement ***{new_line}")
    print(f"{new_line}(Narrator): Take the passage ahead.")
    print(f"{new_line}*** As you walk in you see the remnants of a bar...behind the counter is an old worn down mechanical bartender. ***")
    print(f"{new_line}(Narrator): This one is my favorites. We are truly betting on life itself this time. {new_line}You will have 3 drinks to choose from. Only one of the options aren't poisoned{new_line}Oh! by the way this time the buy in is priceless...its's your taste that will determine the price.")
    while True:
        if balance <= 0:
            print(f"{new_line}(Narrator): Life is money and yours is up.\n\n...You have drank the poison and now have died 😵")
            quit()
        elif balance >= BUYOUT:
            print(f"{new_line}(Narrator): Life is money and you are overflowing with wealth. {new_line}{new_line}*** A platform lifts you to the roof of a building surrounded by water, at the top is a helicopter ***{new_line}{new_line}You've done it, you've won the game: Life's a Gamble!!!")
            quit()
        guess = input(f"{new_line}Pick either Whiskey, Water or Gin: ")
        if guess.lower() == "whiskey":
            balance += BUYOUT
            print(f"{new_line}(Narrator): ...I admire your selection. You've won ${BUYOUT} and your balance is now ${balance}")
            continue
        elif guess.lower() == "water" or guess.lower() == "gin":
            balance -= balance
            print(f"{new_line}(Narrator): Oh no your taste is awful and deadly....your balance is now ${balance}")
            continue
        else:
            print(f"{new_line}Are you for real? Pick either Whisky, Water or Gin: ")
            continue
obstacle5()
