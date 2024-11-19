import csv

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Contact added: {name} - {phone}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact found: {name} - {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")
            

def calculate_average_grades(filename):
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            name = row['Name']
            grades = [float(row['Grade1']), float(row['Grade2']), float(row['Grade3'])]
            
            average_grade = sum(grades) / len(grades)
            
            print(f"{name}: Average Grade = {average_grade:.2f}")
            

def main():
    address_book = AddressBook()

    while True:
        print("___________________________________________________________________")
        action = input("\nEnter 'add' to add a contact,\n'search' to search for a contact,\n'grade' to search for average grade,\n'exit' to quit: ").lower()
        
        if action == 'add':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address_book.add_contact(name, phone)
        elif action == 'search':
            name = input("Enter name to search: ")
            address_book.search_contact(name)
        elif action == 'grade':
            filepath = input("Please enter absolute file path: ")
            calculate_average_grades(filepath)
        elif action == 'exit':
            break
        else:
            print("Invalid option. Please try again.")
    print("___________________________________________________________________\n")
  
if __name__=="__main__":
    main()

