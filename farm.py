#entering recodes for the animals on the farm 
goats_list = []

while True:
    goat_name = input("Enter the goat tag number(pass Q to stop): ")
    
    if goat_name.upper()== "Q":
        break
    
    goat_agenda = input("goat_genda(m/y): ").lower()=='y'
    age = input("Enter the month of the goat: ")
    goat_color = input("Goat color: ")
    weight = input("Enter the goat weight in (KGs): ")
    date = input("Enter the date the goat has got the farm: " )
    
   
    
    