class Budget:

    def __init__(self,**categories):
        self.categories = categories
        print(self.categories)

    def deposit(self,amount,category):
        self.categories[category] = self.categories[category] + amount
        print('You deposited the sum of $'+str(amount)+' '+ 'to '+category)
    
    def withdraw(self,amount,category):
        if amount > self.categories[category]:
            print("Insufficient Balance")
        else:

            self.categories[category] = self.categories[category] - amount
            print('You withdrew the sum of $'+str(amount)+' from '+ category)

    def transfer(self,amount,debitCategory,creditCategory):
        if amount > self.categories[debitCategory]:
            print('Insufficient Balance')
        else:
            self.categories[debitCategory] = self.categories[debitCategory] - amount
            self.categories[creditCategory] =  self.categories[creditCategory] + amount
            print('You transfered the sum of $'+ str(amount) + ' ' + 'from ' + debitCategory + ' to '+ creditCategory )
    
    def computeBalance(self,category):
        print('Your '+ category + ' budget balance is ' + str(self.categories[category]))
        

mybudget= Budget(food=5000, clothing=1800, rent=3700,entertainment=900)
mybudget.deposit(2700,'food')
mybudget.withdraw(1600,'rent')
mybudget.transfer(400,'entertainment','clothing')
mybudget.computeBalance('rent')