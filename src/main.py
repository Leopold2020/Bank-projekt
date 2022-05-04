from resources import Account, create_profile, load_profiles, save_profile, login
from time import sleep

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
    
    if logged_in is True:

        print(f"Hello {user.get_name()}, Welcome to O.N.B")
        sleep(2)
        print(f"What would you like to do here? \n[1] read out name and identification. \n[2] Take a loan \n[3] Look at your debt and cry.\n[4] Save profile \n[5] Exit the bank. \n[6] pay your debts \n[7] Admin options")
        choice1 = input(">> ")
        sleep(1)
    
    else:
        choice1 = "5"



    while choice1 != "5" and logged_in:
       

        if choice1 == "1":
            option_information()
    
        elif choice1 == "2":
            option_loan()

            user.advertisment()
        
        elif choice1 == "3":
            option_debt()

        elif choice1 == "4":
            save_profile(user)

        elif choice1 == "6":
            user.pay_debts()

        elif choice1 == "7":
            print("You have slected the admin meny")

            version = user.get_version()

            print(version)
            
            if user.get_version() == "Admin":
                print("hello")
                user.change_intrest()

            else:
                print("You are not an Admin")
                sleep(2)

        else:
            print("Invalid option")

        user.advertisement()

        print(f"What would you like to do here? \n[1] read out name and identification. \n[2] Take a loan \n[3] Look at your debt and cry.\n[4] Save profile \n[5] Exit the bank. \n[6] pay your debts \n[7] Admin options")
        choice1 = input(">> ")
        sleep(1)

    else:
        print("You have exited the program")