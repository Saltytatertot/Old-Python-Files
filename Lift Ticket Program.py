#Lift Ticket Program
#Tatum Gray
#4/16/2016
import sys
print("Welcome to Bridger Bowl!")
print()

def purchase_lift_ticket(budget):
    print()
    print("   1. One-Day Ticket.")
    print("   2. Half-Day Ticket.")
    print()
    typeTicket = int(input("What type of ticket do you want to purchase? >> "))
    age = -1
    while age < 0:      #Makes sure that a valid age is given
        age = int(input("How old are you? >> "))
    else:                                           
        if(age > 17 and age < 66):  #Checks age range for ticket and equate for given range
            if(typeTicket == 1):
                ticketPrice = 45
            else:
                ticketPrice = 45 * 0.5
        else:
            if(typeTicket == 1):    #Equates price if the above fails
                ticketPrice = 30
            else:
                ticketPrice = 30 * 0.5
        tax = ticketPrice * 1.05    #Factoring in taxes       
    return tax

def create_ski_day_budget():
    budget = int(input("What is your starting budget in dollars? >> "))
    final_balance = (budget - purchase_lift_ticket(budget))
    if final_balance < 0:
        print("You have gone over budget.")
    else:
        print("You were in budget." , "You still have $", final_balance)
create_ski_day_budget()


