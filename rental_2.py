# Rental Management System
rentals = [
    {"rental_number": "R001",
    "rental_type": "apartment",
    "number_of_rooms": 2,
    "items": ['toilet', 'bathroom', 'sink'],
    "status": "taken",
    "amount": 400000},
    
    {"rental_number": "R002",
    "rental_type": "apartment",
    "number_of_rooms": 3,
    "items": ['toilet', 'bathroom', 'sink'],
    "status": "not taken",
    "amount": 450000},
    
    {"rental_number": "R003",
    "rental_type": "apartment",
    "number_of_rooms": '5',
    "items": ['toilet', 'bathroom', 'sink'],
    "status": "not taken",
    "amount": 600000},
    
    {"rental_number": "R004",
    "rental_type": "apartment",
    "number_of_rooms": 6,
    "items": ['toilet', 'bathroom', 'sink'],
    "status": "not taken",
    "amount": 800000}
]

def add_rental():
    rental_number = input("Enter rental number: ")
    rental_type = input("Enter the rental type: ")
    number_of_rooms = input("Enter the number of rooms: ")
    no_of_items = 3
    if no_of_items < 3:
        items = input("Enter the item name: ")
    status = input("Enter the status of the room: ")
    amount = int(input("Enter the amount to be paid: "))
    
    details = {
        "rental_number": rental_number,
        "rental_type": rental_type,
        "number_of_rooms": number_of_rooms,
        "items": items,
        "status": status,
        "amount": amount
    }
    rentals.append(details)
        
        
tenants = []

def register_tenant():
    tenant = {'tenant_name': input("Enter tenant name: ") ,
            'tenant_contact' : input("enter tenant contact") ,
            'gender' : input("enter the gender: "),
            'rental number' : input ("enter rental number: "),
            'dependents' : int(input("enter dependents: ")),
            
            }
    tenants.append(tenant)


for rental in rentals:
        
    print (f"{rental.get('rental_number')} {rental.get('rental_type')} {rental.get('number_of_rooms')} {rental.get('items')} {rental.get('status')} {rental.get('amount')}")
     
payments = []

def record_payment():
    payment ={ 'reciept nuber' : input("enter the number: "),
            'date ' : input("enter date: "),
            'month' : input("enter month: "),
            'year' : input("enter year: "),
            'payment_method' : input("enter the payment method (cash only )")          
    }     
    payments.append(payment)


def compute_amount():
    number_of_months = int(input("enter the number of months to be rentaled : "))
    
def display_records():
    print("\nRental Records:")
    for rental in rentals:
        print(f"{rental.get('rental_no')}: \t {rental.get('rental_type')}: \t {rental.get('status')}")
    
    print("\nTenant Records:")
    for tenant in tenants:
        print(f"{tenant['tenant_no']}: {tenant['tenant_name']} in {tenant['rental_no']}")
    
    print("\nPayment Records:")
    for payment in payments:
        print(f"{payment['receipt_no']}: {payment['amount']} paid on {payment['pay_date']}")
        print(f"   by {payment['tenant_no']} for {payment['rental_no']}") 
    
def main():
    while True:
        print("\nRental Management System")
        print("1. Register Rental Property")
        print("2. Register Tenant")
        print("3. Record Payment")
        print("4. View All Records")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_rental()
        elif choice == '2':
            register_tenant()
        elif choice == '3':
            record_payment()
        elif choice == '4':
            display_records()
        elif choice == '5':
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")
main()
    
    
    
    
    
        
        
        


