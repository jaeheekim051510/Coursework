#! /usr/bin/env python3
import shelve
class Contact():
    def __init__(self, name, number):
        self.name = name
        self.number = number
phone_book = []
def main_menu():
    storage = shelve.open("phonebookC")
    if "phone_book" not in storage:
        storage["phone_book"] = {}
    phone_book = storage["phone_book"]
    """
    The primary menu of the phonebook accepts user input to select what other
    function to call.
    """
    running = True
    while running:
        user_choice = input("""
        Electronic Phone Book
        =====================
        1. Look up an entry
        2. Set an entry
        3. Delete an entry
        4. List all entries
        5. Quit
        What do you want to do (1-5)? """)
        if user_choice == "1":
            search_term = input("Name?: ")
            lookup_entry(search_term)

        elif user_choice == "2":
            new_name = input("Name?: ")
            new_number = input("Phone number?: ")
            create_entry(new_name, new_number)

        elif user_choice == "3":
            remove_target = input("Name?: ")
            remove_entry(remove_target)

        elif user_choice == "4":
            list_all_entries()

        elif user_choice == "5":
            print("Thank you for using our phonebook.")
            storage["phone_book"] = phone_book
            running = False
            storage.close()
        else:
            print(f"Invaild input: {user_choice}")
            print("Please enter a number one through five.")

def lookup_entry(search_term):
    entry_found = False
    for i in phone_book:
        if i.name == search_term:
            print(f"\tEntry found for {search_term} \n\tNumber: {i.number}")
            entry_found = True
    if not entry_found:
        print(f"{search_term} was not found in the phonebook.\nTry using their full name.")

def create_entry(new_name, new_number):
    person = Contact(new_name, new_number)
    phone_book.append(person)

def remove_entry(remove_target):
    for i in range(len(phone_book)):
        target_found = False
        if phone_book[i].name == remove_target:
            del phone_book[i]
            target_found = True
            break
    if not target_found:
            print(f"{remove_target} not found in phone_book")

def list_all_entries():
    for i in phone_book:
        print(f"\tName: {i.name} Number: {i.number}\n")

main_menu()
