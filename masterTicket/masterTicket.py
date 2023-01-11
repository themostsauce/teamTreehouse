from uuid import RFC_4122

TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):   
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE
    
# Run this code continuously until we run out of tickets 
while tickets_remaining >= 1:
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("What is your name? ")
    try:
        num_tickets = int(input("How many tickets would you like, {}? ".format(name)))
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print(("Oh no! We ran into an issue. {} Please try again...".format(err)))
    else: 
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        proceed = input("Would you like to proceed? (y/n) ")

        if proceed.lower() == "y" or "yes":
            # TO DO: gather credit card information and process it
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you, {}. Maybe another time!".format(name))
print("Sorry! We're sold out :(")