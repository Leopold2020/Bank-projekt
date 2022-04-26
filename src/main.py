from resources import Account, create_profile, load_profiles, save_profile


def menu():
    print(f"Welcome to the bank-projekt, here you can look up your account \nyour personlig identification saved here, your total saved money and your debt owed to us.")


def option_information():
    print(f"your account name is {user.get_name()} and your registered identification is {user.get_identification()}\n") 
    
    input("Press enter to continue")

def option_loan():
    user.take_a_loan()

    input("Press enter to continue")

def option_debt():
    print(f"You have {user.get_debt()} $ in debt")
    
    input("Press enter to continue")



if __name__ == "__main__":
    
    print("[1] create a new profile")
    print("[2] Load a profile")
    
    first_choice = input(">> ")

    if first_choice == "1":
        user = create_profile()

    if first_choice == "2":
        user = load_profiles()

    print(f"What would you like to do here? \n1: read out name and identification. \n2. Take a loan \n3. Look at your debt and cry.\n4. Save profile \n5. Exit the bank. \n")
    choice1 = input(">> ")

    while choice1 != "5":
        print(f"Hello {user.get_name()}, Welcome to this bank")

    

        if choice1 == "1":
            option_information()
    
        elif choice1 == "2":
            option_loan()
        
        elif choice1 == "3":
            option_debt()

        elif choice1 == "4":
            save_profile(user)

        else:
            print("Invalid option")

        print(f"What would you like to do here? \n1: read out name and identification. \n2. Take a loan \n3. Look at your debt and cry.\n4. Save profile \n5. Exit the bank. \n")
        choice1 = input(">> ")

    
    else:
        print("You have exited the program")