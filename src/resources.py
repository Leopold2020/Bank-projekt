



class Account:                                                 #Här skapar jag en class för att vara en mall för alla profil
    def __init__(self, name, identification, money, debt, version): 
        self.name = name
        self.identification = identification
        self.money = money
        self.debt = debt
        self.version = version


    def get_name(self):             #Används för att skriva ut namnet om det behövs
        return self.name

    def get_identification(self):      #Används för att skriva ut personliga identification om det behövs
        return self.identification

    def get_money(self):            #Används för att skriva ut pängar man har om det behövs
        return self.money

    def get_debt(self):             #Används för att skriva ut skulden man har om det behövs
        return self.debt

    def get_version(self):
        return self.version
    
    def take_a_loan(self):                                          #En funktion där man ska kunna ta ett lån, den lägger själv också slkuld i self.debt variabeln
        print(f"In this menu you can take a loan.\n")
        loan = int(input(f"How much money would you want to take a loan on.\n"))
        
        self.money += loan
        self.debt += loan * 1.10

    def put_in_money(self):
        print(f"You have selected to put in money in this account\n")
        addition = int(input("how much would you like to add to your bank account?: "))      

        self.money += addition

    def profile_data(self):
        return self.name, self.identification, self.money, self.debt
    
    def ad(self):
        possible_ad = self.version

        if possible_ad == "1":
            print("We just noticed that you have a standar account, and we would be so happy if you took the time to consider getting a uppgrade")


def create_profile():
    print(f"You have chosen to create a new profile\n")
    username = input("What is your name?: ")
    information = input("What is your identification?: ")
    
    
    while True:
        print("[1] for standard account \n[2] for premium account")
        what_version = input(">> ")

        if what_version =="1":
            this_version = "1"
            fee = 0
            break
        
        if what_version =="2":
            this_version = "2"
            fee = 200
            break

        else:
            print("Choose a valid option!")


    return_account = Account(username, information, 0, 0 + fee, this_version )

    print(f"\n{return_account} this account has now been created")
    print()
    return return_account



def save_profile(profile : Account):
    save_list = []
    #for profiles in line:
    name, identification, money, debt = profile.profile_data()
    save_string = f"{name}/{identification}/{money}/{debt}\n"
    save_list.append(save_string)

    with open("saved_profiles.txt", "w", encoding="utf8") as f:
        for line in save_list:
            f.write(line)
        print("profile has been saved")





def load_profiles():
    profiles = []
    with open("saved_profiles.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            data = line.split("/")
            acont = Account( data[0],
                            data[1],
                            int(data[2]),
                            int(data[3]),
                            data[4])

            profiles.append(acont)
    return profiles


def login(users):
    tries = 3
    print("Please log in with your credentials")
    print(f"You have {tries} remaining before you are locked out of the system.")

    while tries > 0:
        user_name = input("\nUsername >> ")
        password = input("Password >> ")
        for user in users:
            if(user_name == user.name and password == user.identification):
                return True, user
        else:
            print("Username or password does not match.")
            tries -= 1
    else:
        return False, None
