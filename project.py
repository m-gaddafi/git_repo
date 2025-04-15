#A PROJECT ABOUT THE RENTAL SYSTEM
rentals= [
    {"rental_number": "R001",
     "rental_type": "apartment",
     "number_of_rooms": 2,
     "items":"[toilet, bathroom, sink]",
     "status": "taken",
     "amount": 400000,
    },
  
    {
        "rental_number": "R002",
     "rental_type": "apartment",
     "number_of_rooms": 4,
     "items": ['toilet','bathroom','sink'],
     "status": "not taken",
     "amount": 450000,
    },
     {
        "rental_number": "R003",
     "rental_type": "apartment",
     "number_of_rooms": 1,
     "items": ['toilet','shower'],
     "status": "taken",
     "amount": 200000,
    },
    {
         "rental_number": "R004",
     "rental_type": "house",
     "number_of_rooms": 3,
     "items": ['toilet','bathroom','kitchen'],
     "status": "not taken",
     "amount": 190000, 
    }
]

tenants = []
payments = []

def register_tenant():
    tenant_name = input("Enter your name: ")
    tenant_contact =input(f"Enter your number: ")
    room_number = input(f"Enter room number (rental number): ")
    
    for rental in rentals:
        rental_found = False
        if rental["rental_number"] == room_number:
            rental_found = True
            if rental["status"] == "taken":
                print("room is already taken")
                break
            else:
                rental["status"] == "not taken"
                print("room is available")
                continue
            
                   
    #if not rental_found:
        #print(f"Rental number not found")
    tenant_gender = input("Enter your gender: ")
    tenant_dependants = input("Enter dependants (comma to separate): ")
    tenants.append(tenant_name) 
    print("Tenant registered successfully")   
    return None

register_tenant()

#def record_payment():



    