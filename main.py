import random

DECISION = "Y/N or q to quit"
STARTING_BALANCE = 100
BUYOUT = 500
new_line = "\n"
decisions = ["y", "n", "q"]

print("Hello and welcome to Life's a Gamble! 🎲🎲🎲\n")
name = input("What's your name? ")
print('') 
print(f"Okay {name} the rules will be quite simple, you will wager money on your decisions and if you can manage to make enough money you can buy yourself out.\n\nI shall be your host and guide you, now....")

        
def play(input):
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
    
play(input)

def start(input):
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
    

start(input)

def obstacle1(input):
    print(f"{new_line}As you look ahead of you, what you will see is a door. This is the start of the fight for your life.")
    print("\n")
    while True:
        random_num = random.randint(1, 2)
        guess = input("We'll start easy. Guess a number between 1 and 2, if you're right the first door will open. If not you will have to continue to wager. ")
        if guess.isdigit():
            guess = int(guess)
            if guess == random_num:
                balance += 10
                print("Looks like you've made it through phase one... Here is a little reward for you. You won $10 and your balance is now {balance}")
                break
            elif guess != random_num:
                balance -= 5
                print(f"Guess you'll have to try again....your balance is now ${balance}")
            elif balance == 0:
                print("Life is money and yours is up.\n\n...You are dead😵")
                quit()
            else:
                print("Enter either 1 or 2")
                continue
    return balance

obstacle1(input)

def main():
    balance = start()
    while True:
        if obstacle1 > 0:
            balance = obstacle1()

main()