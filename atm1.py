import sys          ##python programme er runtime enviornment stop korar jonno    
import getpass      ##eta pin enter korar somoy seta ke hide korar jonno

class ATMsoftware():            
    def __init__(self, User_id, pin, balance = 10000):          ##akta class niyechi ATMsoftware jar constructor er parameter gulo holo user_id, pin ar balance
        self.User_id = User_id
        self.pin = pin
        self.balance = balance
                                                            ##ebar ak ak kore function bananor pala
    def account_detail(self):
        print(f"User ID: {self.User_id}")
        print(f"Available balance: {self.balance}\n")
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        
    def withdrawl(self, amount):
        self.amount = amount
        if self.amount>self.balance:
            print("Insufficient Balance!!!")
        elif (self.amount<499):
            print("Withdrawl amount must be more than 500/-!")
        elif(self.amount%100!=0):
            print("Withdrawl amount must contain with minimum 100 rupee notes!")
        else:
            self.balance=self.balance-self.amount
            print(f"{amount} withdrawal successful!")
            
    def check_balance(self):
        print("Available balance: ", self.balance)

    def end(self):
        print("""
        Thank you
        Visit again
        Exiting Program...""")
        sys.exit()

    def menu(self):
        inp=int(input("""
            Select from the following menu:
            
            1. Check Balance
            2. Deposit
            3. Withdraw
            4. PIN change
            5. Exit
        
            """))

        if ((inp == 1) or (inp==2) or (inp==3) or (inp==4) or (inp==5)):    ##jodi user 1,2,3,4,5 chara onno kichu input dey tobe 69, 70 line print hobe ar abar menu te fire jabe
            if inp == 1:
                atm.check_balance()
                atm.end()

            elif inp == 2:
                amount = float(input("How much you want to deposit:"))
                atm.deposit(amount)
                atm.account_detail()
                atm.end()

            elif inp== 3:
                amount = float(input("How much you want to withdraw:"))
                atm.withdrawl(amount)
                atm.account_detail()
                atm.end()

            elif inp == 4:
                old_pin = str(getpass.getpass("Enter old PIN: "))
                if(old_pin==atm.pin):
                    new_pin = str(getpass.getpass("Enter new PIN: "))
                    if ((new_pin.isdigit()) and (new_pin != atm.pin) and (len(new_pin) == 4)):     ##.isdigit check kore je saob input gulo number e ache ki na
                        new_conformation_pin = str(getpass.getpass("Confirm new PIN: "))
                        if (new_conformation_pin != new_pin):
                            print("PIN did not match")
                        else:
                            atm.pin = new_pin
                            print("New PIN added")
                            atm.menu()
                    else:
                        print("New PIN must be within 4 numbers and different from the previous one")
                        atm.end()
                else:
                    print("Wrong PIN!!")
                    atm.menu()

            elif inp == 5:
                atm.account_detail()
                atm.end()
            sys.exit()
        else:
            print("Wrong input!!!")
            print("Read the menu carefully and try again")
            atm.menu()
            
while True:
    user_type=int(input("""Press '1' for new user
    Press '2' for existing user
    """))
    if (user_type==1):
        print("\t\t\tACCOUNT CREATION\t\t\t")        ##new account create hocche
        while True:
            User_id= input("Enter new 6 digit User ID: ")
            if ((len(User_id)==6) and (User_id.isdigit())):
                pin = str(getpass.getpass("Enter your 4 digit PIN number: "))    ##getpass korle pin ta hide thakbe
                if (len(pin)==4) and (pin.isdigit()):
                    confirm_pin=str(getpass.getpass("Enter PIN again to confirm: "))        #pin conformation
                    if (pin==confirm_pin):
                        atm = ATMsoftware(User_id, pin)
                        print("Congratulations! Account created successfully......\n")

                        while True:
                            transaction = input("""Do you want to do any transaction?:
                            Press 'Y' for yes
                            Press 'N' for no:
                            """).lower()                        ##.lower() method thakar karon eta sob input string ke lower case kore dey
                            if transaction == "y":
                                atm.menu()
                            elif transaction == "n":
                                atm.end()
                                break
                            else:
                                print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
                    else:
                        print("PIN did not match")
                        sys.exit()
                else:
                    print("PIN must be consist 4 digit only!")
            else:
                print("User id should be consist 6 digits only!")
    elif(user_type==2):
            print("\t\t\tACCOUNT LOGIN\t\t\t")        ##account login hocche
            for i in range(0,3):
                User_id= input("Enter 6 digit User ID: ")
                ####
                if ((len(User_id)==6) and (User_id.isdigit())):   
                    pin = str(getpass.getpass("Enter your 4 digit PIN number: "))    ##getpass korle pin ta hide thakbe
                    if (len(pin)==4) and (pin.isdigit()):    ####
                            atm = ATMsoftware(User_id, pin)
                            print(f"Congratulations! {User_id} Account logged in successfully......\n")
                            atm.menu()
                    else:
                        print("Incorrect PIN!!")
                else:
                    print("User id doesn't exists!!")
    else:
        print("Wrong input!!!\nTry again")