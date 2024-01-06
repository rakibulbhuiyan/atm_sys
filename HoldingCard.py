class Card_Holder():
    def __init__(self,card_Number,pin,firstName,lastName,balance) -> None:
        self.card_Number=card_Number
        self.pin=pin
        self.firstName=firstName
        self.lastName=lastName
        self.balance=balance
    
    #getter data
    def get_cardNumber(self):
        return self.card_Number
    def get_pin(self):
        return self.pin
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_balance(self):
        return self.balance
    #setter data
    def set_cardNumber(self,newValue):
        self.card_Number=newValue
    def set_pin(self,newValue):
        self.pin=newValue
    def set_firstName(self,newValue):
        self.firstName=newValue
    def set_lastName(self,newValue):
        self.lastName=newValue
    def set_balance(self,newValue):
        self.balance=newValue
    #print all data
    def printData(self):
        print(f'Card Number : {self.card_Number}')
        print(f'Pin : {self.pin}')
        print(f'First Name : {self.firstName}')
        print(f'Last Name : {self.lastName}')
        print(f'Balance : {self.balance}')