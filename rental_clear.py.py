rentals = []
tenants = []
payments = []

def find_rental(rental_no):
    for rental in rentals:
        if rental['rental_no'] == rental_no:
            return rental
    return None

def find_tenant(tenant_no):
    for tenant in tenants:
        if tenant['tenant_no'] == tenant_no:
            return tenant
    return None


def register_rental():
    print("\nRegister New Rental Property")
    rental = {
        'rental_no' : int(input("Enter the rental number: ")),
        'rental_type': input("Enter rental type (Apartment/House/Room): ").capitalize(),
        'no_of_rooms': int(input("Enter number of rooms: ")),
        'has_toilet': input("Has toilet? (y/n): ").lower() == 'y',
        'has_kitchen': input("Has kitchen? (y/n): ").lower() == 'y',
        'water': input("Water source (Borehole/Municipal/Tank): ").capitalize(),
        'status': 'Vacant'
    }
    rentals.append(rental)
    print(f"Rental {rental['rental_no']} registered successfully!")

def register_tenant():
    print("\nRegister New Tenant")
    if not rentals:
        print("No rentals available. Please register a rental first.")
        return
    
    print("Available rentals:")
    for rental in rentals:
        if rental['status'] == 'Vacant':
            print(f"{rental['rental_no']} {rental['rental_type']} ({rental['no_of_rooms']} rooms)")
    
    rental_no = int(input("Enter rental number: "))
    rental = find_rental(rental_no)
    
    if not rental or rental['status'] != 'Vacant':
        print("Invalid or occupied rental number")
        return
