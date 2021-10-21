""" ATM CASH WITHDRAWAL SYSTEM """

class atm_cash() :
    def __init__(self,name):
        self.name = name
        print(f"Welcom to the {self.name} bank ")

    def atm_pin (self):
        pin = int(input("enter your pin : "))
        if pin == 4635 :
            print("\nyour PIN is correct \n"
                  "please select any option to move further ")
            print("\n"
                  "Cash withdrawal - 1 \n"
                  "Balance check - 2 \n"
                  "cash deposit - 3 \n"
                  "Exit - 0 \n ")

            while (1):
                pref = int(input("\nEnter your preffernce : "))
                cash = 10000
                if pref == 1 :
                    print("\n * CASH WITHDRAWAL *")
                    ammt = int(input("\nEnter your ammount : "))

                    if ammt > cash :
                        print("you have not enogh account balance to withdraw \n"
                              "please check your balance and try again ")

                    else :
                        two_thd = 0
                        five_hd = 0
                        if ammt >= 2000:
                            two_thd = ammt//2000

                        #if ammt > (two_thd * 2000) or ammt < (two_thd * 2000):
                        print(two_thd)




                        print("\n withdawal successful \n"
                              f"account balance = {cash - ammt}")
                        break

                if pref == 2 :
                    print("\n * BALANCE ENQIRY *")
                    print(f"balance in your account : {cash}")
                    break

                if pref == 3 :
                    print("\n * CASH DEPOSIT * ")
                    amt = int(input("\n Enter your ammount : "))
                    print("cash deposited successfully \n"
                          f"account balance = {cash + amt}")
                    break
                if pref == 0 :
                    print("Exit successfuly ")

                    break
                else :
                    print('Please enter correct prefferance code')
                    continue
        else:
            print("worng passward please try again ")

bank = atm_cash("HDFC")
print(bank.atm_pin())