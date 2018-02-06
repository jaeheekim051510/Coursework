#! /usr/bin/env python3
"""
A phonebook command line tool. Entries are persistent.
"""
import shelve
import sys

storage = shelve.open("phonebook")
if "phone_book" not in storage:
    storage["phone_book"] = {}
phone_book = storage["phone_book"]
def main_menu():
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
            storage.close()
            running = False

        else:
            print("""
                Please enter a number one through five.
                =====================
                1. Look up an entry
                2. Set an entry
                3. Delete an entry
                4. List all entries
                5. Quit
                """)

def lookup_entry(search_term):
    """
    Searches the phonebook names for the search_term.
    """
    if search_term in phone_book:
        result = phone_book[search_term]
        print(f"Found entry for {search_term}: " + result)

    else:
        print(f"{search_term} not found in phonebook")

def create_entry(new_name, new_number):
    """
    Creates a new entry in the phonebook.
    """
    phone_book[new_name] = new_number

def remove_entry(remove_target):
    if remove_target in phone_book:
        del phone_book[remove_target]
    else:
        print(f"Error {remove_target} not found!")
def list_all_entries():
    sort_type = input("Do you want to sort by name(1) or number(2)? ")
    if sort_type == "1":
        sorted_phone_book = sorted(phone_book.keys())
        for i in sorted_phone_book:
            print(f"Name: {i} Number: {phone_book[i]}")
    elif sort_type == "2":
        sorted_phone_book = sorted(phone_book.items(), key=lambda number: number[1])
        for index, value in enumerate(sorted_phone_book):
            print(f"Name: {value[0]} Number: {value[1]}")
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test-sort":
        list_all_entries()
    else:
        main_menu()
