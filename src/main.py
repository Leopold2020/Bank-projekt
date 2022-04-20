from resources import Account, create_profile


def menu():
    print(f"Welcome to the bank-projekt, here you can look up your account \nyour persinal information saved here, your total saved money and your debt owed to us.")

user1 = Account("Ulle", 4002109543, 100, 1000)

if __name__ == "__main__":
    
    user = create_profile()

    while True:
        print(f"Hello {user.get_name()}, Welcome to this bank")
        choice1 = input(f"What would you like to do here? \n1: read out name and information. \n2. Take a loan \n3. Look at your debt and cry. \n4. Exit the bank. \n")

        if choice1 == "1":
            print()
            print(f"your account name is {user.get_name()} and your registered identification is {user.get_information()}\n") 
    
        if choice1 == "2":
            print()
            user.take_a_loan()
            print()
        
        if choice1 == "3":
            print()
            print(user.get_debt())
            print()

        if choice1 == "4":
            break