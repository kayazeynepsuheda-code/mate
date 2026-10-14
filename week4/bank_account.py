class Account:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit_money(self,amount):
        self.balance=self.balance+amount
        print(self.balance)
        return self.balance


    def withdraw_money(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print(self.balance)
            return self.balance
        else:
            print("insufficient balance")
            return None


person=Account("Jane")
person.deposit_money(200)
person.withdraw_money(70)
person.deposit_money(120)
person.withdraw_money(400)
print(f"Name: {person.name}   Money: {person.balance}")
    
        