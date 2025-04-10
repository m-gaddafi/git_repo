#rental project 

rental = {
    "rental": { # rental information
        "rental_id": 1,     # rental id
        "car_id": 1,        # car id                            
        "customer_id": 1,   # customer id
       "rental_date": "2023-10-01", # rental date 
        "return_date": None, # return date
        "status": "rented"   # rental status (rented, returned)
    }}
    
rental_properties = {}

while True:
    item = input("Enter the item you want to rent (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    price = float(input("Enter the rental price: "))
    duration = input("Enter the rental duration (e.g., days, weeks): ")
    rental_properties[item] = {"price": price, "duration": duration}

print("\nRental Properties:")
for item, details in rental_properties.items():
    print(f"{item}: Price: {details['price']}, Duration: {details['duration']}")
    
rate_policy = {
    "Daily": 50,
    "Weekly": 300,
    "Monthly": 1000,
    # Add more rate policies
}
