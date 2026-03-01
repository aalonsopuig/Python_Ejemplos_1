# Biomedical Equipment Inventory Management System

# Global variables
inventory = []
next_id = 1

def add_equipment():
    """Adds new equipment to the inventory after getting user input."""
    name = input("Enter the equipment name (cannot be empty): ")
    if name == "":
        print("Equipment name cannot be empty.")
        return

    department = input("Enter the department: ")
    status = input("Enter the status (Available, In Repair, Out of Service): ")
    
    global next_id
    equipment = {
        'ID': next_id,
        'Name': name,
        'Department': department,
        'Status': status
    }
    inventory.append(equipment)
    print(f"Equipment added with ID: {next_id}")
    next_id += 1

def search_equipment_by_id():
    """Searches for equipment by ID and displays its details if found."""
    search_id = input("Enter the equipment ID to search: ")
    if search_id.isdigit():
        search_id = int(search_id)
        found = False
        for equipment in inventory:
            if equipment['ID'] == search_id:
                print("Equipment Found:")
                print(f"ID: {equipment['ID']}, Name: {equipment['Name']}, Department: {equipment['Department']}, Status: {equipment['Status']}")
                found = True
                break

        if not found:
            print("No equipment found with that ID.")
    else:
        print("Invalid input; please enter a valid integer ID.")

def delete_equipment_by_id():
    """Deletes equipment by ID."""
    delete_id = input("Enter the equipment ID to delete: ")
    if delete_id.isdigit():
        delete_id = int(delete_id)
        index = 0  # Initialize the index variable
        found = False  # Flag to check if the equipment is found

        # Loop through the inventory until the item is found or the list ends
        while index < len(inventory):
            equipment = inventory[index]
            if equipment['ID'] == delete_id:
                inventory.pop(index)  # Remove the item without incrementing the index
                print(f"Equipment with ID {delete_id} has been deleted.")
                found = True
                break  # Exit the loop since the item is found and deleted
            index += 1  # Increment the index

        if not found:
            print("No equipment found with that ID.")
    else:
        print("Invalid input; please enter a valid integer ID.")

def list_all_equipment():
    """Lists all equipment in the inventory."""
    if not inventory:
        print("No equipment currently in inventory.")
    else:
        print("Listing All Equipment:")
        for equipment in inventory:
            print(f"ID: {equipment['ID']}, Name: {equipment['Name']}, Department: {equipment['Department']}, Status: {equipment['Status']}")


"""Main function to run the inventory management system."""
while True:
    print("\nBiomedical Equipment Inventory Management System")
    print("1. Add Equipment")
    print("2. Search Equipment by ID")
    print("3. Delete Equipment by ID")
    print("4. List All Equipment")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        add_equipment()
    elif choice == '2':
        search_equipment_by_id()
    elif choice == '3':
        delete_equipment_by_id()
    elif choice == '4':
        list_all_equipment()
    elif choice == '5':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")