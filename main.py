import random

# All Counstants Used
MAX_LINES = 5
MIN_BET = 1
MAX_BET = 1000
ROWS = 5
COLUMNS = 5

# each symbol and its count in each row
symbolCount = {
    "A": 8,
    "B": 10,
    "C": 11,
    "D": 18,
}

# each symbol and its multiplier on the winnings.
symbolMultiplier = {
    "A": 6,
    "B": 5,
    "C": 4,
    "D": 3
}

'''
pre-conditions: None
Post-conditions: None
Prompts the user to deposit an amount into the machine, would not stop until amount is greater than 9
returns: an integer number referring to the amount deposited.
'''


def getDeposit():
    while True:
        amount = input("How much would you like to deposit (min $10)? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 10:
                break
            else:
                print("Must be atleast $10.")
        else:
            print("Please enter a number")
    return amount


'''
pre-condition: None
Post-conditions: None
Prompts the user to enter the number of lines they wish to bet on.
returns: an integer referring to the number of lines the user bet's on
'''


def getNumberOfLines():
    while True:
        lines = input(
            "Enter the number of lines to bet (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines (1 - " + str(MAX_LINES) + ")")
        else:
            print("Please enter a valid option")
    return lines


'''
pre-conditions: None
post-conditions: None
Prompts the user to enter the amount they want to bet on each slot
returns: the integer amount they want to bet on each slot.
'''


def getPlayersBet():
    while True:
        amount = input("How much would you like to bet on each line (min $" +
                       str(MIN_BET) + " - " + "max $" + str(MAX_BET) + ")  ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount


'''
pre-conditions:
    rows: The number of rows in our slot machine, should be unchanged after.
    cols: The number of columns in our slot machine, should be unchanged after.
    symbols: A dictionary storing the symbols in our slot machine and their related count.
post-conditions: 
returns: a 2 dimensional list that gets the arrangement of the machine after the spin.
'''


def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(allSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


'''
'''


def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


'''
'''


def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)
    return winnings, winningLines

    """_summary_

    """


def spinTheSlots(userBalance):
    slotLines = getNumberOfLines()
    while True:
        bet = getPlayersBet()
        totalBet = bet * slotLines

        if totalBet > userBalance:
            print(
                f"You do not have enough money in your balance to bet that amount, your current balance is ${userBalance}"
            )
        else:
            break

    print(
        f"You are betting ${bet} on {slotLines} lines. Total bet is ${totalBet}"
    )
    slots = getSlotMachineSpin(ROWS, COLUMNS, symbolCount)
    printSlotMachine(slots)
    userWinnings, winningLines = checkWinnings(
        slots, slotLines, bet, symbolMultiplier)
    print(f"you won ${userWinnings}")
    print(f"on lines: ", *winningLines)
    return userWinnings - totalBet


"""
Main Program that runs slot machine.
"""


def main():
    userBalance = getDeposit()
    while True:
        print(f"Current balance is ${userBalance}")
        spinMachine = input("press any key to spin (q to quit).")
        if spinMachine == "q":
            break
        userBalance += spinTheSlots(userBalance)


main()
