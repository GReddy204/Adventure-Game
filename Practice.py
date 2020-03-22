
coin_earned = 500

def amount(coin_earned):    
    extra = input("Enter a number under 500 crowns:\n")
    if extra.isupper() or extra.islower():
        print("Please enter valid input")
        amount(coin_earned)
    elif int(extra) <= 350:
        coin_earned += int(extra)
        print("> The elder agrees")
        print(f"you now stand to earn {coin_earned} crowns\n")
        return coin_earned 
    elif int(extra) > 350:
        print("> The elder says that's too much.")
        print("*Try again*")
        

def haggling():
    print("> The elder offers you 500 Crowns to kill the"
    " monster.")
    print("*Do you want to haggle?*")
    haggle = input("yes - enter 'y'""\nno - enter 'n'\n")

    if haggle == "y":
        print("*How much more would you like?*")
        amount(500)
    elif haggle == "n":
        print("> You decide not to haggle")
    else:
        print("Please enter valid input")
        haggling()


haggling()
print(coin_earned)

