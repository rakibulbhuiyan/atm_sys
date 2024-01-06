from HoldingCard import Card_Holder

def print_menu():
    print("Choose one following option:")
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Show Balance")
    print("4) Exit")


def deposite(Card_Holder):
    try:
        deposit=float(input("How much you want to deposite : "))
        Card_Holder.set_balance(Card_Holder.get_balance() + deposit)
        print("Thank you. Your new balance is : ", str(Card_Holder.get_balance()))
    except:
        print("Invalid Data")

def withdraw(Card_Holder):
    try:
        withdraw=float(input("How much you want to withdraw : "))
        if Card_Holder.get_balance() < withdraw:
            print("You dont have enough money")
        else:
            Card_Holder.set_balance(Card_Holder.get_balance() - withdraw)
            print("Successfully withdraw. Your new balance is : ", str(Card_Holder.get_balance()))
    except:
        print("Invalid Data")

def check_balance(Card_Holder):
    print("Your balance is :", Card_Holder.get_balance())


if __name__=='__main__':
    current_user=Card_Holder('','','','','')

    list_of_cardHolder=[]
    list_of_cardHolder.append(Card_Holder('12345',1234,'Jhon','Ch',300.00))
    list_of_cardHolder.append(Card_Holder('23456',1234,'Rohim','Khan',400.00))
    list_of_cardHolder.append(Card_Holder('34567',1234,'Kamrul','Hasan',100.00))
    list_of_cardHolder.append(Card_Holder('45678',1234,'Roni','Ch',600.00))
    list_of_cardHolder.append(Card_Holder('56789',1234,'Babu','Khan',700.00))

    # for card_Number
    while True:
        try:
            debitCardNumber=input('Enter Card number : ')
            debitMatch=[holder for holder in list_of_cardHolder if holder.card_Number==debitCardNumber]
            if (len(debitMatch)>0):
                current_user=debitMatch[0]
                break
            else:
                print("Invalid card Number. please try again!!")
        except: 
            print("Invalid Data")
    # for pin 
    while True:
        try:
            user_pin=int(input("Enter Pin Number : ").strip())
            if current_user.get_pin() == user_pin:
                break
            else:
                print("pin Not Matched!!!")
        except:
            print("Invalid Data")

    print(f"welcome {current_user.get_firstName()} ")
    option=0
    while True:
        print_menu()
        try:
            option=int(input())
        except:
            print("Invalid Input")
        if (option==1):
            deposite(current_user)
        elif (option==2):
            deposite(current_user)
        elif (option==3):
            deposite(current_user)
        elif (option==4):
            break
        else:
            option=0
    print("Have a nice day!!!")


        
