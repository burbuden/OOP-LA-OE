print ("OE#2\nArdent Azrael Sayson\nBSIT2B\n")

class Phone:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def modify_properties(self, brand=None, model=None, year=None):
        if brand:
            self.brand = brand
        if model:
            self.model = model
        if year:
            self.year = year

    def delete_attributes(self):
        self.brand = None
        self.model = None
        self.year = None

phones = []

def display_phones():
    if not phones:
        print("No phones available.")
    else:
        for index, phone in enumerate(phones):
            print(f"{index + 1}: {phone.brand} {phone.model} ({phone.year})")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Add Phone")
        print("2. Modify Phone")
        print("3. Delete Phone Attributes")
        print("4. Delete Phone Object")
        print("5. Display Phones")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            phones.append(Phone(brand, model, year))
        
        elif choice == '2':
            display_phones()
            index = int(input("Select phone number to modify: ")) - 1
            if 0 <= index < len(phones):
                brand = input("Enter new brand (leave blank to keep current): ")
                model = input("Enter new model (leave blank to keep current): ")
                year = input("Enter new year (leave blank to keep current): ")
                phones[index].modify_properties(brand if brand else None, model if model else None, year if year else None)
        
        elif choice == '3':
            display_phones()
            index = int(input("Select phone number to delete attributes: ")) - 1
            if 0 <= index < len(phones):
                phones[index].delete_attributes()
        
        elif choice == '4':
            display_phones()
            index = int(input("Select phone number to delete: ")) - 1
            if 0 <= index < len(phones):
                del phones[index]
        
        elif choice == '5':
            display_phones()
        
        elif choice == '6':
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
