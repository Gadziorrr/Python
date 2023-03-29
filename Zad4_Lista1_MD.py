class Account(): 

    def __init__(self, balance: int):
        self.__balance = balance
    
    def pay(self):
        print('How much would you like to add to your balance?')
        value = input()
        self.__balance += int(value)
        
    def take(self):
        print('How much would you like to substract from your balance?')
        value = input()
        if(int(value) > self.__balance):
            print('Amount you want to substract is bigger than your balance. Action not completed')
        else:
            self.__balance -= int(value)
        
    def __str__(self):
        return (f'\nPrivate balance: {self.__balance}')
        
def main():
    firstAccount = Account(500)
    secondAccount = Account(1500)

    print('First account')
    print(firstAccount)
    firstAccount.pay()

    print(firstAccount)   
    firstAccount.take()
    print(firstAccount)
    
    print('\nSecond account')
    print(firstAccount)  
    secondAccount.take()
    
    print(firstAccount)
    secondAccount.pay()
    print(firstAccount)
    
main()