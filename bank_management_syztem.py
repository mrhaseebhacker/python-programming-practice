class Bank_Account:
    def __init__(self, acc_no, acc_bal):
        self.acc_no = acc_no
        self.acc_bal = acc_bal

    def cash_deposit(self, amount):
        self.acc_bal += amount
        print(amount, "Amount deposited")
        print("Total amount",self.total_balnce())

    def cash_withdraw(self,amount):
        if amount > self.acc_bal:
            print("\n❌ Insufficient funds! Withdrawal failed.")
        else:
            self.acc_bal -= amount
            print(amount,"Amount Withdraw")
            print("Total amount",self.total_balnce()) 
    
    def total_balnce(self):
        return self.acc_bal   
acc1 = Bank_Account(12345, 10000)
print(f"🏦 Account Created! Initial Balance: {acc1.acc_bal}")

print(acc1.acc_bal)
acc1.cash_deposit(100000) 
acc1.cash_withdraw(50000)     
acc1.cash_withdraw(70000)