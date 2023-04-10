def investment():
    try:
        name = input("Please input your name: ")
        amount = int(input("Please input your amount: "))
    except ValueError:
        print("Invalid input. Please enter a valid figure amount.")
        return

    welcome_bonus = 0.5  # assuming welcome bonus is 50% expressed as a decimal
    bonus_amount = amount * welcome_bonus
    total_amount = amount + bonus_amount
    
    print(f"Total amount: {total_amount}")
    
    print(f"Thank you, {name}! Your initial investment of {amount} naira has earned you a welcome bonus of {bonus_amount} naira, bringing your total investment to {total_amount} naira.")
    
    Bal = total_amount
    VAT = 0.07  # assuming VAT is 7% expressed as a decimal

    try:
        withdrew = int(input("Input amount to withdraw: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer amount.")
        return

    if withdrew > Bal :
        print(" Amount Exceed Your Balance.")
        return

    if Bal and (withdrew + (withdrew * VAT)) > Bal:
        print("You cannot withdraw up to that amount 7% VAT inclusive.")
    else:
        Bal -= withdrew 
        Bal -= (withdrew * VAT)
        print(f"Successful withdrawal. Remaining balance: {Bal} naira")
        return Bal

investment()