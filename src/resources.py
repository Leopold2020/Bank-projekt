



class Account:                                                 #Här skapar jag en class för att vara en mall för alla profil
    def __init__(self, name, information, money, debt): 
        self.name = name
        self.information = information
        self.money = money
        self.debt = debt

    def get_name(self):             #Används för att skriva ut namnet om det behövs
        return self.name

    def get_information(self):      #Används för att skriva ut personliga informationen om det behövs
        return self.information

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


def create_profile():
    print(f"You have chosen to create a new profile\n")

        

