import random

def lottery_gen():
    min_number = 0
    max_number =50

    # Generate a random number between 0 and 50
    random_number = random.randint( min_number, max_number)

    # Get user name and input number
    user_name = input("please enter your name: ")
    user_number = (int(input("Please enter your number: ")))
    print (user_name)
    
    # the winning number
    winning_number = 30
    
    # Check if the user input is within the allowed range
    if user_number < min_number or user_number > max_number:
        print("Only numbers from 0 to 50 are acceptable. Please try again.")
        return
  
    # Check if the random number matches the winning number
    if random_number == user_number == winning_number:
        print(f"Congratulations {user_number}! Your lucky number is {winning_number}. You are the lucky winner!")
    else:
        print(f"you chose number {user_number}. sorry, the generated number is  {random_number} and it's not the winning number. Please try again. {user_name}")

# Call the lottery_gen() function to run the program
lottery_gen()