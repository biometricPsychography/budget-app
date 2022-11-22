
class Category :
    
    
    def __init__(self, nam):
        self.name = nam
        self.ledger = []
        self.current_total = 0
        self.withdrawal_total = 0
        print(self.name, 'constructed')

        # Pad cents to always have two digits
    def format_currency(self, string: str) :
        dollars_then_cents_list = string.split('.')
        if int(dollars_then_cents_list[1]) < 10 :
            formatted_amount = dollars_then_cents_list[0] + '.0' + dollars_then_cents_list[1]
        elif int(dollars_then_cents_list[1]) % 10 == 0 :
            formatted_amount = dollars_then_cents_list[0] + '.' + dollars_then_cents_list[1] + '0'
        else :
            formatted_amount = dollars_then_cents_list[0] + '.' + dollars_then_cents_list[1]
        return(formatted_amount)

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
            self.withdrawal_total += amount
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
        str_output_line_list = []
        title_scaffold = '******************************'

        # determine name placement in title_scaffold
        middle_offset = int(len(self.name) / 2)
        odd_off_extra_padding = 0
        if len(self.name) % 2 != 0 :
            odd_off_extra_padding = 1
            
        middle_index_int = 15
        title_left = title_scaffold[:middle_index_int - middle_offset - odd_off_extra_padding]
        title_right = title_scaffold[middle_index_int + middle_offset:]
        self.title = title_left + self.name + title_right

        str_output_line_list.append(self.title)


        for item in self.ledger :
            desc_overflow = item['description'][24:]

            formatted_amount = self.format_currency(str(item['amount']))
            
            amount_overflow = formatted_amount[8:]

            if len(desc_overflow) > 0 :
                string_left = item['description'][:24]
            else :
                string_left = item['description']

            if len(amount_overflow) > 0 :
                string_right = formatted_amount[:8]
            else :
                string_right = formatted_amount

            spacing = 30 - len(string_left) - len(string_right)
            ledger_line_string = string_left + ' ' * spacing + string_right
            
            str_output_line_list.append(ledger_line_string)
        
        str_output_line_list.append('Total: ' + self.format_currency(str(self.current_total)))

        return '\n'.join(str_output_line_list)


vg_budget = Category('Video Games')
vg_budget.deposit(127.72, 'Work')
vg_budget.withdraw(5)
vg_budget.deposit(2, 'HOLY 2 DOLLAR BILL ENCHANTED BY ELVES')

food_budget = Category('Food')
food_budget.deposit(100, 'Work')
food_budget.withdraw(25, 'Fast food')

vg_budget.transfer(30, food_budget)


 
def create_spend_chart(categories) :
    meta_withdrawal_total = 0
    percentage_meta_withdrawal_total_list = []
    category_and_percentage_list = []

    for category in categories :
        meta_withdrawal_total += category.withdrawal_total
    
    for category in categories :

        nearest_ten_rounded_down_percentage = 10 * int(category.withdrawal_total / meta_withdrawal_total * 10)

        (percentage_meta_withdrawal_total_list
            .append(nearest_ten_rounded_down_percentage)
        )

        category_and_percentage_list.append([category, nearest_ten_rounded_down_percentage])

    def build_chart_line(cat_and_percent_list) :

        line_list = []


        chart_scaffold = ''
        chart_left_axis_literal = (
'''
100| 
 90| 
 80| 
 70| 
 60| 
 50| 
 40| 
 30| 
 20| 
 10| 
  0| 
'''
        )

        reversed_line_list = chart_left_axis_literal.strip().split('\n')[::-1]
        reversed_line_list[0] += ' '

        list_of_item_bar_lists = []

        for item in cat_and_percent_list :

            this_item_bar_list = []

            bar_height = int(item[1]) / 10 + 1
            i = 0
            while i < bar_height :
                this_item_bar_list.append('o  ')
                i += 1
            
            graph_top_and_bar_height_diff = 11 - bar_height 

            graph_top_and_bar_height_diff
            i = 0
            while i < graph_top_and_bar_height_diff :
                this_item_bar_list.append('   ')
                i += 1

            list_of_item_bar_lists.append(this_item_bar_list)
        
        for list in list_of_item_bar_lists :
            i = 0
            for bar_element in list :
                reversed_line_list[i] += bar_element
                i += 1



        print(reversed_line_list)

        print('\n'.join(reversed_line_list[::-1]))
    
    build_chart_line(category_and_percentage_list)
            
                

# print(vg_budget)
create_spend_chart([vg_budget, food_budget])
