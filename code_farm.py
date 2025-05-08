import datetime
import os
import csv

# Data file to store animal information
DATA_FILE = "animals.csv"

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays the main menu."""
    print("\nAnimal Farm Management System")
    print("1. Add Animal")
    print("2. View Animals")
    print("3. Edit Animal")
    print("4. Delete Animal")
    print("5. Search Animals")
    print("6. Generate Report")
    print("7. Settings")
    print("0. Exit")

def load_animals():
    """Loads animal data from the CSV file. Returns a list of dictionaries."""
    animals = []
    try:
        with open(DATA_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                animals.append(row)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        pass
    except Exception as e:
        print(f"Error loading data: {e}")
        input("Press Enter to continue...")
    return animals

def save_animals(animals):
    """Saves animal data to the CSV file."""
    if not animals:
        return  # if it is empty do nothing
    
    fieldnames = animals[0].keys() # gets the headers

    try:
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(animals)
    except Exception as e:
        print(f"Error saving data: {e}")
        input("Press Enter to continue...")

def add_animal():
    """Adds a new animal to the system."""
    clear_screen()
    animal_id = input("Enter Animal ID: ")
    species = input("Enter Species (e.g., Cow, Goat, Chicken): ")
    breed = input("Enter Breed: ")
    dob_str = input("Enter Date of Birth (YYYY-MM-DD): ")
    puchase_date_str = input("Enter Purchase Date (YYYY-MM-DD): ")
    try:
        dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        input("Press Enter to continue...")
        return

    animals = load_animals()
    # Check if the animal ID already exists
    if any(animal['Animal ID'] == animal_id for animal in animals):
        print("Error: An animal with this ID already exists.")
        input("Press Enter to continue...")
        return

    new_animal = {
        "Animal ID": animal_id,
        "Species": species,
        "Breed": breed,
        "Date of Birth": dob
    }
    animals.append(new_animal)
    save_animals(animals)
    print("Animal added successfully!")
    input("Press Enter to continue...")

def view_animals():
    """Displays all animals in the system."""
    clear_screen()
    animals = load_animals()
    if not animals:
        print("No animals in the system.")
        input("Press Enter to continue...")
        return

    print("--- Animal List ---")
    for animal in animals:
        print(f"Animal ID: {animal['Animal ID']}")
        print(f"Species: {animal['Species']}")
        print(f"Breed: {animal['Breed']}")
        print(f"Date of Birth: {animal['Date of Birth']}")
        print("-" * 20)
    input("Press Enter to continue...")

def edit_animal():
    """Edits an existing animal's information."""
    clear_screen()
    animal_id = input("Enter Animal ID to edit: ")
    animals = load_animals()

    for animal in animals:
        if animal['Animal ID'] == animal_id:
            print("--- Editing Animal ---")
            print(f"Animal ID: {animal['Animal ID']}")
            print(f"Species: {animal['Species']}")
            print(f"Breed: {animal['Breed']}")
            print(f"Date of Birth: {animal['Date of Birth']}")

            species = input(f"Enter new Species (current: {animal['Species']}): ") or animal['Species']
            breed = input(f"Enter new Breed (current: {animal['Breed']}): ") or animal['Breed']
            dob_str = input(f"Enter new Date of Birth (YYYY-MM-DD) (current: {animal['Date of Birth']}): ")
            dob = None #set default value
            if dob_str:
                try:
                    dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format.  Keeping current date.")
                    dob = animal['Date of Birth']
            else:
                dob = animal['Date of Birth'] #keep original

            animal['Species'] = species
            animal['Breed'] = breed
            animal['Date of Birth'] = dob
            save_animals(animals)
            print("Animal edited successfully!")
            input("Press Enter to continue...")
            return

    print("Animal not found.")
    input("Press Enter to continue...")

def delete_animal():
    """Deletes an animal from the system."""
    clear_screen()
    animal_id = input("Enter Animal ID to delete: ")
    animals = load_animals()
    for animal in animals:
        if animal['Animal ID'] == animal_id:
            animals.remove(animal)
            save_animals(animals)
            print("Animal deleted successfully!")
            input("Press Enter to continue...")
            return
    print("Animal not found.")
    input("Press Enter to continue...")

def search_animals():
    """Searches for animals based on Animal ID, Species, or Breed."""
    clear_screen()
    search_term = input("Enter search term: ").lower()
    animals = load_animals()
    results = []
    for animal in animals:
        if (search_term in animal['Animal ID'].lower() or
                search_term in animal['Species'].lower() or
                search_term in animal['Breed'].lower()):
            results.append(animal)

    if not results:
        print("No animals found matching the search term.")
        input("Press Enter to continue...")
        return

    print("--- Search Results ---")
    for animal in results:
        print(f"Animal ID: {animal['Animal ID']}")
        print(f"Species: {animal['Species']}")
        print(f"Breed: {animal['Breed']}")
        print(f"Date of Birth: {animal['Date of Birth']}")
        print("-" * 20)
    input("Press Enter to continue...")

def generate_report():
    """Generates a basic report on the animals in the system."""
    clear_screen()
    animals = load_animals()
    if not animals:
        print("No animals in the system to generate a report.")
        input("Press Enter to continue...")
        return

    print("--- Animal Report ---")
    print(f"Total Number of Animals: {len(animals)}")

    species_count = {}
    for animal in animals:
        species = animal['Species']
        species_count[species] = species_count.get(species, 0) + 1 #increment count

    print("\nSpecies Breakdown:")
    for species, count in species_count.items():
        print(f"{species}: {count}")

    # Calculate average age
    total_age_days = 0
    for animal in animals:
        dob = datetime.datetime.strptime(animal['Date of Birth'], "%Y-%m-%d").date()
        today = datetime.date.today()
        age_days = (today - dob).days
        total_age_days += age_days
    if total_age_days > 0:
        average_age_years = total_age_days / 365
        print(f"\nAverage Animal Age: {average_age_years:.2f} years")
    else:
        print(f"\nAverage Animal Age: 0 years")

    input("Press Enter to continue...")
def settings():
    """Placeholder for settings functionality."""
    clear_screen()
    print("--- Settings ---")
    print("No settings available at this time.")  # Placeholder
    input("Press Enter to continue...")

def main():
    """Main function to run the program."""
    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)  #convert choice to int
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
            continue #restart the loop

        if choice == 1:
            add_animal()
        elif choice == 2:
            view_animals()
        elif choice == 3:
            edit_animal()
        elif choice == 4:
            delete_animal()
        elif choice == 5:
            search_animals()
        elif choice == 6:
            generate_report()
        elif choice == 7:
            settings()
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()

