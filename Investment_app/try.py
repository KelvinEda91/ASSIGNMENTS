def investment():
    try:
        name = input("Please input your name: ")
        amount = int(input("Please input your amount: N"))
    except ValueError:
        print("Invalid input. Please enter a valid figure amount.")
        return
    #this try: function above is a special function that prevent the user from inputing any other data type that is not Integer for the amount.


    bonus_amount = amount / 100 * 50
    total_amount = amount + bonus_amount
    
    print(f"Total balance: N{total_amount}")
    
    print(f"Thank you, {name}! Your initial investment of N{amount} has earned you a welcome bonus of N{bonus_amount} bringing your total investment balance to N{total_amount} ")
    
    Bal = total_amount

    try:
        withdraw = int(input("Input amount to withdraw: N"))
    except ValueError:
        print("Invalid input. Please enter a valid figure amount.")
        return
    
    VAT = withdraw / 100 * 7


    if Bal and withdraw + VAT > Bal:
        print("You cannot withdraw up to that amount 7% VAT inclusive.")
    else:
        Bal -= withdraw
        Bal -= (withdraw - VAT)
        print(f"Successful withdrawal. 7% VAT has been deducted from your wallet balance, current balance now: N{Bal} ")
        
        print("hello!! we are always here to serve you and to give you the best service. please don't forget to reach out to us whenever you have an issue")

        return Bal

investment()