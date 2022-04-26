



class Account:                                                 #Här skapar jag en class för att vara en mall för alla profil
    def __init__(self, name, identification, money, debt): 
        self.name = name
        self.identification = identification
        self.money = money
        self.debt = debt

    def get_name(self):             #Används för att skriva ut namnet om det behövs
        return self.name

    def get_identification(self):      #Används för att skriva ut personliga identification om det behövs
        return self.identification

    def get_money(self):            #Används för att skriva ut pängar man har om det behövs
        return self.money

    def get_debt(self):             #Används för att skriva ut skulden man har om det behövs
        return self.debt
    
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


def create_profile():
    print(f"You have chosen to create a new profile\n")
    username = input("What is your name?: ")
    information = input("What is your identification?: ")

    return_account = Account(username, information, 0, 0)

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
            char = Account( data[0],
                            data[1],
                            int(data[2]),
                            int(data[3]))

            profiles.append(char)
    return profiles