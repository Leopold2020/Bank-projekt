from time import sleep



class Account:                                                 #Här skapar jag en class för att vara en mall för alla profil
    def __init__(self, name, password, identification, money, debt, version): 
        """En klass för alla profiler

        Args:
            name (str): Namnet på profilerns användare
            password (str): Lösenordet för profilen
            identification (int): id alltås år månad och dag man är född, 
            (obs skriv detta är en uppgift och inte en säker ställe och skriva sitt tiktiga id, skriv ett fejk när man testar)
            money (int): Hur mycket pengar som man har på ett konto
            debt (int): Hur mycket skuld man har
            version (str): Här ska det stå om man har standard, premium eller admin profil
        """

        self.name = name
        self.password = password
        self.identification = identification
        self.money = money
        self.debt = debt
        self.version = version


    def get_name(self):             #Används för att skriva ut namnet om det behövs
        """En funktion för att få namnet
        """
        return self.name
        

    def get_password(self):
        """En funktion för att få lössenordet
        """
        return self.password
        

    def get_identification(self):      #Används för att skriva ut personliga identification om det behövs
        """En funktion för att få identifieraren
        """
        return self.identification
        

    def get_money(self):            #Används för att skriva ut pängar man har om det behövs
        """En funktion för att få veta hur mucket penagar man har
        """
        return self.money
        

    def get_debt(self):             #Används för att skriva ut skulden man har om det behövs
        """En funktion för att få veta hur mycket skuld man har
        """
        return self.debt
        

    def get_version(self):
        """En funktion för att se vad för veriation man har på sin profil
        """
        return self.version
        
    
    def take_a_loan(self):                                          #En funktion där man ska kunna ta ett lån, den lägger själv också slkuld i self.debt variabeln
        """En funktion för att ta ett lån, den lägger också till skuld atomatiskt
        """

        print(f"In this menu you can take a loan.\n")
        loan = int(input(f"How much money would you want to take a loan on.\n>>"))
        
        self.money += loan


        with open("intrest_rate.txt", "r",encoding="utf8") as f:    #öpnar en text fil.
        
            intrest = int(f.read())     #Läser av hela filen

            end_result = intrest / 100      #Uträckningen görs för att i intrest_rate filen så skriver man procent i (utan att ha procent tecknet) så man behöver då dela det med hundra för att få det till matematematiskt tal

            end_result += 1     #Det plusas på med ett för att man ska öka med procenten i intrest_rate.


        self.debt += loan * end_result      #Skuld ska vara lika mycket som lånet med ränta så då gångras lånet med räntan


    def put_in_money(self):
        """En funktion för att kunna lägg in pengar, pengarna bara kommer upp utan någon skuld.
        """
        print(f"You have selected to put in money in this account\n")
        addition = int(input("how much would you like to add to your bank account? \n>> "))      

        self.money += addition  #Pengar man har plusas ihop med pengar man ska lägga in.

    
    def pay_debts(self):
        """En funktion för att betala ens skulder.
        """

        if self.debt > 0:
            print("You have selected to pay your debts.\n")

            amount = 0

            while amount != "x":
                sleep(2)
                print(f"\nYou have {self.debt} in debt, and {self.money} in stored money in this bank.")
                print("\nHow much do you want to pay off?")
                print("If you want to quit this meny write [x]")
                amount = int(input(">> "))
                


                if amount > self.money:     #Ifall att man försöker betala mer än vad man själ har pengar
                    print("You have selected to pay off more money than you posses, please select a possible transaction")

                elif amount > self.debt:        #Så man inte betalar mer än vad man har i skuld, så att banken inte står i skuld till den personen
                    print("You have selected to pay off more than you have in debt, that is not an option.")

                elif amount > 0:
                    self.debt -= amount
                    self.money -= amount

                    if self.debt == 0:
                        print("You have now paid of all of your debts.")
                        break

                    else:
                        print(f"You now have {self.debt} in debt left.")
                        break
                
                else:
                    print("That is not a valid option, the only walid options are a number that is above zero, more or equal to the money you have save on this bank and less or equall to the amount of debt you have.")
            
                
        else:
            print("You do not have any debt to pay here.")

    def profile_data(self):
        """En funktion för att ta fram all data samtidigt ur en profil.

        Returns:
            list: namn, lössenord, id, sparade pengar, skulder, verision, 
        """
        return self.name, self.password, self.identification, self.money, self.debt, self.version
    
    def advertisement(self):
        """En funktion för att kalla på reklam som frågar dig att uppgradera till premium, den aktiveras bara om man har ett standard profil veriation.
        Det enda saken som premium gör är att man slipper reklamer, annars har det ingen nytta.
        """
        possible_ad = self.version

        if possible_ad == "Standard":       #Programmet kollar om man har ett standard profil, om man har så fortsätter denna funktion
            print("We just noticed that you have a standard account, and we would be so happy if you took the time to consider getting a uppgrade")
            sleep(4)
            while True:
                print("Would you like to uppgrade to premium account? y/n")
                account_option = input(">> ")
                if account_option == "y":
                    self.version = "Premium"        #Om man vill uppgradera till ett premium profil så kostar det en 200, vilket blir tillagd till skulder
                    self.debt += 200
                    break

                if account_option == "n":
                    print("what would it take to make you reconsider your choice?")     #Programmet frågar en hur man kan förbättra sig, men klagomålet tas inte till hänsyn elelr sparas inte på något sätt.
                    input(">> ")
                    sleep(3)
                    print("Thank you for informing us how to better our services")
                    break
                
                else:
                    print("Please choose a valid option")

    
    def admin_privliges(self):
        """En fuktion för att kunna få ett admin account
        """
        print(f"You have selected to log in as a admin, you have to posses a password administered by the owner of this bank. If you do not posses a allowence it is illigal to hack youre way through")
        
        decision = []
        while decision != "solved":     #While loppen fortsätter så länge det inte står "solved" i variabeln "decision"

            print("\n[1] log in as admin\n[2] Exit admin meny")
            adminmeny = input(">> ")

            if adminmeny == "1":
                print("You have selected to login as an administrator, write the password you have been handed")
                admin_login = input(">> ")

                if admin_login == "fuckoff":        #Ett lösenord som man bara kan hitta i koden, för det står ingenstans i programmet som användaren kan se.
                    self.version = "Admin"          #Om man har lössenordet så får man ett admin konto.
                    decision = "solved"
                            

            if adminmeny == "2":
                print("you have exited the admin meny.")        #Ett alternativ för komma ut ur while loppen
                decision = "solved"

            else:
                print("\nThat is not a valid option, please read options carfully\n")
                sleep(3)


    def change_intrest(self):
        """En funktion där man kan ändra räntan på lån, den ska placeras bakom en if sats för att kolla om man är en admin!
        """

        print("What is the new intrest rate? You write in precent, but do not write the procent sign.")
        intrest_change = input(">> ") 
        with open("intrest_rate.txt", "w", encoding="utf8") as f:       #Öppnar en fil som heter intrest_rate för att ändra ränta
            
                f.write(intrest_change)                                 #Byter ut texten i filen med den nya räntan
                print("Intrest has been changed has been saved")





def create_profile():
    """En funktion för att skapa en ny profil.

    Returns:
        list: Alla saker som en Account behöver i denna kod, namn, lössenord, id, 
        sparade pengar och skuld som är både aoutomatiskt 0 förutom om man upgraderar till premium i skapandet då börjar man med 200 i skuld, sen veration på profilen
    """
    print(f"You have chosen to create a new profile\n")
    username = input("What is your name?: ")
    secretholder = input("Write password: ")
    information = input("What is your identification?: ")
    
    
    while True:
        print("[1] for standard account \n[2] for premium account")
        what_version = input(">> ")

        if what_version =="1":
            this_version = "Standard"
            fee = 0
            break
        
        if what_version =="2":
            this_version = "Premium"    #Om man vill ha ett premium profil så kostar det en 200, som blir tillagd i skulder
            fee = 200
            break

        else:
            print("Choose a valid option!")


    return_account = Account(username, secretholder ,information, 0, 0 + fee, this_version )        #En lista för all information för alla delar som gör upp en profil i detta program

    print(f"\n{return_account} this account has now been created")
    print()
    return True, return_account



def get_intrest():
    """En funktion för att på hämta räntan

    Returns:
        int: räntan borde vara skriven som ett nummer utan procent tecken sen låter man funktionen göra sin magi för att omvandla talet till 1.(något) för att man ska sen gångra det man lånade.
    """
    with open("intrest_rate.txt", "r",encoding="utf8") as f:
        
        intrest = f.read()

        end_result = intrest / 100      #Uträckningen görs för att i intrest_rate filen så skriver man procent i (utan att ha procent tecknet) så man behöver då dela det med hundra för att få det till matematematiskt tal

        end_result += 1     #Det plusas på med ett för att man ska öka med procenten i intrest_rate.

        return end_result





def save_profile(profile : Account):
    """En funktion för att spara ens profil.

    Args:
        profile (Account): Här så skrivs ens information ner i ett txt dokument för att man ska senare kunna logga in som den senare. Det som sparas är, namn, lössenor, id, sparade pengar, skuld och varation på profilen.
    """
    save_list = []
    #for profiles in line:
    name, password,  identification, money, debt, account = profile.profile_data()
    save_string = f"\n{name}/{password}/{identification}/{money}/{debt}/{account}\n"      #Här så tar man alla delar som gör upp en profil sen lägger man emällan alla delar ett / för att datorn ska kunna skilja alla delar åt när man loggar in som en profil
    save_list.append(save_string)

    with open("saved_profiles.txt", "a", encoding="utf8") as f:
        for line in save_list:
            f.write(line)
        # print("profile has been saved")



def load_profiles():
    """En funktion för att ladda ner alla profiler.

    Returns:
        list: En lista med all profiler, för att man ska sen slänga in i en funktion där man läser av alla och loggar in i en av dom.
    """
    profiles = []
    with open("saved_profiles.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            data = line.split("/")      #Man skiljer alla delar på en profil med ett /
            acont = Account(data[0],
                            data[1],
                            data[2],
                            int(data[3]),
                            int(data[4]),
                            data[5].rstrip("\n"))       #Datorn laddar upp 6 olika delar av sparad text separerade med ett /, om man har mer än 6 saker seraperade med ett / så kommer dom inte laddas.

            profiles.append(acont)
    return profiles


def login(users):
    """En funktion som man använder för att kunna logga in i en redan gjord profil, man behöver skriva in rätt namn och lössenord för att man ska
    kunna logga in. Man har bara tre försök innan man blir uteslängd.
    Den fungerar genom att alla profiler blir nedladdade sen går man genom dom en itaget för att se vilken som matchar den man skrrev ner.

    Args:
        users (list): en variabel för att ha alla gjorda profiler.

    Returns:
        list: Antigen så returnar man ens profil och ett True för att kunna logga in i banken, men om man inte skrev in rätt andvändar namn eller lösenord tre gånger så returnar funktionen ett False statment.
    """

    tries = 3
    print("Please log in with your credentials")
    print(f"You have {tries} remaining before you are locked out of the system.")

    while tries > 0:                            #Om tries blir mindre än 0 så låter programmet inte en att fortsätta att logga in
        user_name = input("\nUsername \n>> ")
        password = input("Password \n>> ")
        for user in users:      #Datorn kollar igenom alla profiler för att gemföra.
            if(user_name == user.name and password == user.password):       #Dotorn kollar om användar namnet och lössenordet stämmer med en sparad profil på saved_profiles filen.
                return True, user       #Om man lyckas logga in så returnar datorn ett True och själva profilen, True är till för att låta porgrammet vidare i banken
        else:
            tries -= 1
            print(f"Username or password does not match, You have {tries} attepmts left.")
    else:
        return False, None      #Om man inte lyckas logga in så returnar datorn ett False och en None, då kan man inte komma vidare i programmet.
