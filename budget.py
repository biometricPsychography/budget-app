class Category :
    

    def __init__(self, nam):
        self.name = nam
        self.ledger = []
        self.current_total = 0
        print(self.name, 'constructed')

    def deposit(self, amount, desc='') :

        amount = float(amount)
        if amount <= 0 :
            print("You can't deposit a negative or 0 amount. Use positive numbers only.")
        else :
            self.current_total += amount
            self.ledger.append(
                {
                    'amount': amount,
                    'description': desc
                }
            )
        
        

    def withdraw(self, amount, desc='') :
        did_succeed = False

        amount = float(amount)
        if amount <= 0 :
            print("You can't withdraw a negative or 0 amount. Use positive numbers only.")
        elif not self.check_funds(amount) :
            print('Withdrawal failed! Not enough funds.')
        else :
            amount = - amount
            self.current_total += amount
            self.ledger.append(
                {
                    'amount': amount,
                    'description': desc
                }
            )
            did_succeed = True
        
        return did_succeed
        
    
    def get_balance(self) :
        return(self.current_total)

    def transfer(self, amount, destination) :
        did_succeed = False

        did_succeed = self.withdraw(amount, 'Transfer to ' + destination.name)
        if did_succeed : 
            destination.deposit(amount, 'Transfer from ' + self.name)
        

        return did_succeed

    def check_funds(self, amount) :
        
        amount = float(amount)
        
        if amount <= 0 :
            print("You can't check the presence of a negative or 0 amount. Use positive numbers only.")
        elif self.current_total - amount <= 0 :
            return False
        else :
            return True
    
    def get_raw_ledger(self) :
        return self.ledger
    



vg_budget = Category('Video Games')
vg_budget.deposit(127.72, 'Work')
vg_budget.withdraw(5)

food_budget = Category('Food')
food_budget.deposit(100, 'Work')

vg_budget.transfer(30, food_budget)

print(vg_budget.ledger)
print(food_budget.ledger)

# def create_spend_chart(categories):