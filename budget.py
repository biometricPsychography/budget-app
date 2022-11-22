
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
    
    def __str__(self) :
        self.title_scaffold = '******************************'

        # determine name placement in title_scaffold
        middle_offset = int(len(self.name) / 2)
        odd_off_extra_padding = 0
        if len(self.name) % 2 != 0 :
            odd_off_extra_padding = 1
            
        middle_index_int = 15
        title_left = self.title_scaffold[:middle_index_int - middle_offset - odd_off_extra_padding]
        title_right = self.title_scaffold[middle_index_int + middle_offset:]
        self.title = title_left + self.name + title_right

        self.ledger_line_scaffold = '                              '


        for item in self.ledger :
            item_ledger_string = item
            item_overflow = item['description'][28:]

            if len(item_overflow) > 0 :
                item_ledger_string = item['description'][:28]
            print(item_ledger_string)

        return ''


vg_budget = Category('Video Games')
vg_budget.deposit(127.72, 'Work')
vg_budget.withdraw(5)
vg_budget.deposit(2, 'HOLY 2 DOLLAR BILL ENCHANTED BY ELVES')

food_budget = Category('Food')
food_budget.deposit(100, 'Work')

vg_budget.transfer(30, food_budget)

print(vg_budget.ledger)
print(food_budget.ledger)

print(vg_budget)
# def create_spend_chart(categories):