compoundList = ["1. Annually", "2. Semi-annually", "3. Quarterly", "4. Monthly"]
compoundDict = {1:1, 2:2, 3:4, 4:12}
readBack = {1:"annually", 2:"semi-annually", 3:"quarterly", 4:"monthly"}
#Input
def userInput():
    startPrice = float(input("Enter the starting balance:\n$"))
    time = float(input("How many years is the money going to sit?\nYears: "))
    rate = float(input("What is the interest rate?\nPlease exclude the \"%\"\nInterest rate: "))
    print(compoundList)
    inputCompound = int(input("Choose the number corresponding with the compound: "))
    compound = compoundDict.get(inputCompound)
    print("Start price: $" + str(startPrice) + "\nYears: " + str(time) + "\nInterest rate: " + str(rate) + "%\nCompounded " + str(readBack.get(inputCompound)) + ".")
    rate = rate / 100
    while True:
        check = input("Is everything correct?\ny/n: ")
        if check == 'y':
            interestCalculator(startPrice, rate, time, compound)
            break
        elif check == 'n':
            print("Okay, we will restart.")
            userInput()
        else:
            print("Oops!... It looks like something went wrong! Make sure you are using lower case \"y\" and \"n\"")
#Calculator
def interestCalculator(startPrice, rate, time, compound):
    exponent = time * compound
    mathWord = 1 + (rate / compound)
    moreMath = mathWord ** exponent
    endPrice = startPrice * moreMath
    interestAccrued = endPrice - startPrice
    print("Ending balance: $%0.2f" % endPrice)
    print("Accrued Interest: $%0.2f" % interestAccrued)
#Startup
while True:
    decision = input("Would you like to calculate some interest?\ny/n: ")
    if decision == 'y':
        userInput()
        break
    elif decision == 'n':
        print("You make me sad...")
        break
    else:
        print("Oops!... It looks like something went wrong! Make sure you are using lower case \"y\" and \"n\"")
