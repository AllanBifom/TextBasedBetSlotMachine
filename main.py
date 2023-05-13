def getDeposit():
    while True:
        amount = input("How much would you like to deposit (min $10)? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 10:
                break
            else:
                print("Must be greater than 0.")
        else:
            print("Please enter a number")
    return amount
