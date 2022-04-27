from resources import Account, create_profile, load_profiles, save_profile, login


def menu():
    print(f"Welcome to the bank-projekt, here you can look up your account \nyour persinal identification saved here, your total saved money and your debt owed to us.")


def option_information():                                                                                                       #Den läser upp ens namn och id som är nedskriven i ens profil.
    print(f"your account name is {user.get_name()} and your registered identification is {user.get_identification()}\n") 
    
    input("Press enter to continue")

def option_loan():          #En kallelse på funktionen där man kan ta ett lån och få skuld beroende på hur mycket man lånade.
    user.take_a_loan()

    input("Press enter to continue")

def option_debt():                                  #Funktionen
    print(f"You have {user.get_debt()} $ in debt")
    
    input("Press enter to continue")



if __name__ == "__main__":
    users = load_profiles()

    # print("[1] create a new profile")
    
    # first_choice = input(">> ")

    # if first_choice == "1":     
    #     user = create_profile()      #Här kommer koden som kallar på funktionen där man skapar en profil

    # if first_choice == "2":
    #     user = load_profiles()         #Här kan man ladda en redan gjord profil

    logged_in, user = login(users)
    print(f"What would you like to do here? \n1: read out name and identification. \n2. Take a loan \n3. Look at your debt and cry.\n4. Save profile \n5. Exit the bank. \n")
    print(f"Hello {user.get_name()}, Welcome to this bank")
    choice1 = input(">> ")

    while choice1 != "5" and logged_in:

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