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

#we're registering the rental details and tenant details
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

    tenant = {
        
        'tenant_name': input("Enter tenant name: "),
        'contact': input("Enter contact number: "),
        'gender': input("Enter gender (M/F/O): ").upper(),
        'tenant_no': rental_no,
        'dependants': int(input("Enter number of dependants: "))
    }
    tenants.append(tenant)
    rental['status'] = 'Occupied'
    print(f"Tenant {tenant['tenant_no']} registered successfully!")

def record_payment():
    print("\nRecord Payment")
    
    payment = {
        
        'pay_date': input("Enter payment date (YYYY-MM-DD): "),
        'pay_month': int(input("Enter payment month (1-12): ")),
        'pay_method': input("Payment method (Cash/Bank Transfer/Mobile Money): ").title(),
        'amount': float(input("Enter amount: ")),
        'tenant_no': input("Enter the tenant number: "),
        'rental_no': int(input("Enter rental number: ")),
        'receipt_no' : input("Enter the receipt number: ")
    }
    
    payments.append(payment)
    print(f"Payment recorded with receipt number {payment['receipt_no']}")
    return payment

def display_records():
    print("\nRental Records:")
    for rental in rentals:
        print(f"{rental.get('rental_no')}: {rental.get('rental_type')}: {rental.get('status')}")
    
    print("\nTenant Records:")
    for tenant in tenants:
        print(f"{tenant['tenant_no']}: {tenant['tenant_name']} in {tenant['tenant_no']}")
    
    print("\nPayment Records:")
    for payment in payments:
        paid_payment = payment['pay_month'] * payment['amount']
        print(f"Receipt number: {payment['receipt_no']}\nShs.{payment['amount']} paid on {payment['pay_date']} by {tenant['tenant_name']} for rental {payment['rental_no']}")
        print(f"Shs.{paid_payment} paid for {payment['pay_month']} months.") 
        
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
            register_rental()
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

#if __name__ == "__main__":
main()

