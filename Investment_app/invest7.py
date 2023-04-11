def investment():
    try:
        name = input("Please input your name: ")
        amount = int(input("Please input your amount: N"))
    except ValueError:
        print("Invalid input. Please enter a valid figure amount.")
        return
    #this try: function above is a special function that prevent the user from inputing any other data type that is not Integer for the amount.

    welcome_bonus = 0.5  # assuming welcome bonus is 50% expressed as a decimal
    bonus_amount = amount * welcome_bonus
    total_amount = amount + bonus_amount
    
    print(f"Total balance: N{total_amount}")
    
    print(f"Thank you, {name}! Your initial investment of N{amount} has earned you a welcome bonus of N{bonus_amount} bringing your total investment balance to N{total_amount} ")
    
    Bal = total_amount
    VAT = 0.07  # assuming VAT is 7% expressed as a decimal

    try:
        withdrew = int(input("Input amount to withdraw: N"))
    except ValueError:
        print("Invalid input. Please enter a valid figure amount.")
        return

    if withdrew > Bal:
        print(" Amount Exceed Your Balance.")
        return

    if Bal and (withdrew + (withdrew * VAT)) > Bal:
        print("You cannot withdraw up to that amount 7% VAT inclusive.")
    else:
        Bal -= withdrew
        Bal -= (withdrew * VAT)
        print(f"Successful withdrawal. 7% VAT has been deducted from your wallet balance, current balance now: N{Bal} ")
        return Bal

investment()