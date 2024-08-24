# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    while True: # loop savings_balance input
        try:
            savings_balance = float(input("Enter the savings account balance: "))
            break # Exit the loop if the user enters a valid number.
        except ValueError:
            print("Whoops, please enter a valid number for the savings account balance.")
 
    while True: # loop savings_interest input
        try:
            savings_interest = float(input("Enter  savings account interest rate (APR): "))
            break # Exit the loop if the user enters a valid number.
        except ValueError:
            print("Whoops, please enter a valid number for the savings account interest rate.")

    while True: # loop savings_maturity input
        try:
            savings_maturity = int(input("Enter the number of months for the savings account: "))
            break # Exit the loop if the user enters a valid number.
        except ValueError:
            print("Whoops, please enter a valid number for the number of months for the savings account.")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nInterest earned on savings account after {savings_maturity} months: ${interest_earned:,.2f}")
    print(f"Updated savings account balance: ${updated_savings_balance:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    while True: # Loop cd_balance until the user enters a valid number.
        try:
            cd_balance = float(input("Enter the CD account balance: "))
            break # Exit the loop if the user enters a valid number.
        except ValueError:
            print("Whoops, please enter a valid number for the CD account balance.")
 
    while True: # loop cd_interest input
        try:
            cd_interest = float(input("Enter the CD account interest rate (APR): "))
            break # Exit the loop if the user enters a valid number.
        except ValueError:
            print("Whoops, please enter a valid number for the CD account interest rate.")

    while True: # loop cd_maturity input
        try:
            cd_maturity = int(input("Enter the number of months for the CD account: "))
            break # Exit the loop if the user enters a valid number.
        except ValueError:
            print("Whoops, please enter a valid number for the number of months for the CD account.")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\nInterest earned on cd account after {cd_maturity} months: ${interest_earned:,.2f}")
    print(f"Updated cd account balance: ${updated_cd_balance:,.2f} \n")

if __name__ == "__main__":
    # Call the main function.
    main()
