#2.  Create a Bank account with members account number, name, type of account and balance.
#Write constructor and methods to deposit at the bank and withdraw an amount from the bank
class bank:
    def __init__(self):
        self.name=str(input("enter the name:"))
        self.accountnumber=int(input("enter the account number:"))
        self.balance=0
        self.typeofaccount=str(input("enter the type of account savings/current:"))
    def deposite (self):
        deposite=int(input("enter the amount to be deposited:"))
        self.balance=self.balance+deposite
        print(self.balance)
       
    def withdraw (self):
        wdamount=int(input("enter the withdrawamount:"))
        if self.balance>=wdamount:
            self.balance=self.balance-wdamount
            print("the withdrawamount",self.balance)
        else:
            print("insufficcient balance")
    def display(self):
        print("the net balance",self.balance)
b_aobj=bank()
while(True):
    print("\n 1.Deposite money \n 2.withdraw money\n 3.exit(0)")
    ch=int(input("enter the choice:"))
    if(ch==1):
        b_aobj.deposite()
        b_aobj.display()
    elif(ch==2):
        b_aobj.withdraw()
        b_aobj.display()
    else:
        exit(0)
b_aobj.display()
a=bank()
a.deposite()
a.withdraw()
a.display()
  
        
        
    