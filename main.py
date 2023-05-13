import random

MAX_LINES = 5
MIN_BET = 1
MAX_BET = 1000

ROWS = 5
COLUMNS = 5

symbolCount = {
    "A": 3,
    "B": 7,
    "C": 9,
    "D": 6,
}

symbolMultiplier = {
    "A": 9,
    "B": 4,
    "C": 2,
    "D": 5
}


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


def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def checkWinnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol] * bet
    return winnings


def main():
    userBalance = getDeposit()
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


main()
