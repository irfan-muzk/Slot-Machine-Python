import random

bet = 0
deposit = 0
roll = 0
paying = 0

letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
          "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
          "U", "V", "W", "X", "Y", "Z"]

winner = {
    "AAA": 100, "BBB": 15, "CCC": 10, "DDD": 5, "EEE": 5, 
    "FFF": 1, "GGG": 1, "HHH": 1, "III": 1, "JJJ": 1, "KKK": 1,
    "LLL": 1, "MMM": 1, "NNN": 1, "OOO": 1, "PPP": 1, "QQQ": 1,
    "RRR": 1, "SSS": 1, "TTT": 1, "UUU": 1, "VVV": 1, "WWW": 1,
    "XXX": 1, "YYY": 1, "ZZZ": 1
}

def user_deposit():
    global deposit
    add_deposit = input("enter how much you want to deposit: $")
    convert_deposit = int(add_deposit)
    deposit += convert_deposit
    print(f"You have add ${convert_deposit} to your deposit.")

def user_bet():
    global deposit
    global bet
    global roll
    global paying
    if deposit >= 0:
        input_bet = input("enter your bet: $")
        spin_count = input("how many times you want to spin? ")
        bet_convert = int(input_bet)
        spin_convert = int(spin_count)
        bet += bet_convert
        roll += spin_convert
        pay = bet_convert*spin_convert
        paying += pay
        deposit -= pay
    else:
        print("you dont have enough deposit!")

def spin():
    global deposit
    global bet
    global roll
    global paying
    times = 1
    while True:
        #slot 1
        spin1 = random.choice(letter)
        #slot 2
        spin2 = random.choice(letter)
        #slot 3
        spin3 = random.choice(letter)
        #show spin result
        spin = f"{spin1}{spin2}{spin3}"
        print(f"You get: {spin}")
        times += 1

        if spin in winner.keys():
            print(f"you win! '{spin}' in {times} rolls.")
            winning = winner[spin]*bet
            deposit += winning
            print(f"you earned: ${winning}")
            print(f"your current deposit is: ${deposit}")
            break
        elif times > roll:
            print("you lose! try again next time.\n")
            print(f"you spend: ${paying}")
            print(f"your current deposit is: ${deposit}")
            break
        else:
            continue
    roll = 0
    paying = 0

def ask_user():
    check = 0
    ask = input("do you want to play again? (enter 'y' or 'n')")
    while True:
        if ask == "y":
            while True:
                ask_deposit = input("do you want to add your deposit?" 
                            "(enter 'y' or 'n')")
                if ask_deposit == "y":
                    user_deposit()
                    print(f"Your current deposit is: ${deposit}\n")
                    break
                elif ask_deposit == "n":
                    break
                else:
                    continue
            user_bet()
            spin()
            break
        elif ask == "n":
            check += 1
            break
        else:
            continue
    return check

user_deposit()
user_bet()
spin()
while ask_user() < 1:
    ask_user()