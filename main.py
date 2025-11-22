donors = []

def add_donor():
    name = input("Enter donor name: ")
    age = int(input("Enter age: "))
    blood_group = input("Enter blood group: ")
    phone = input("Enter phone number: ")

    donor = {
        "name": name,
        "age": age,
        "blood_group": blood_group,
        "phone": phone
    }

    donors.append(donor)
    print("Donor added successfully.\n")


def view_donors():
    if not donors:
        print("No donors in the database.\n")
        return

    print("\n--- Donor List ---")
    for i, d in enumerate(donors):
        print(f"{i+1}. Name: {d['name']}, Age: {d['age']}, Blood Group: {d['blood_group']}, Phone: {d['phone']}")
    print()


def update_donor():
    view_donors()
    num = int(input("Enter donor number to update: ")) - 1

    if 0 <= num < len(donors):
        donors[num]["name"] = input("Enter new name: ")
        donors[num]["age"] = int(input("Enter new age: "))
        donors[num]["blood_group"] = input("Enter new blood group: ")
        donors[num]["phone"] = input("Enter new phone number: ")
        print("Donor details updated.\n")
    else:
        print("Invalid number.\n")


def delete_donor():
    view_donors()
    num = int(input("Enter donor number to delete: ")) - 1

    if 0 <= num < len(donors):
        donors.pop(num)
        print("Donor removed.\n")
    else:
        print("Invalid number.\n")
      
while True:
    print("----- Blood Donor Database System -----")
    print("1. Add Donor")
    print("2. View Donors")
    print("3. Update Donor")
    print("4. Delete Donor")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_donor()
    elif choice == "2":
        view_donors()
    elif choice == "3":
        update_donor()
    elif choice == "4":
        delete_donor()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.\n")
