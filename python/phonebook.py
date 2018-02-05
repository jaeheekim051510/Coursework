def main_Menu():
    user_Choice =  int(input("""
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    What do you want to do (1-5)? """))
    if user_Choice == 1:
        lookup_Entry()
    elif user_Choice == 2:
        create_Entry()
    elif user_Choice == 3:
        remove_Entry()
    elif user_Choice == 4:
        listAll_Entries()
    elif user_Choice == 5:
        return "Thank you for using our phonebook."
    else:
        print("Please enter a number one through five.")
        main_Menu()
