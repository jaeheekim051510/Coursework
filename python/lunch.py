#! /usr/bin/env python3
"""
Allow the user to track where they went to lunch.
"""
import shelve
import os
from operator import itemgetter
print(" Starting lunch traker")
"""
Opening Save File
"""
print(" Opening storage")
days = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday"}

storage = shelve.open("lunch")

if "Restaurants" not in storage:
    storage["Restaurants"] = {"Farm Burger":0,
                              "Chipotle":0,
                              "ru san's":0}

restaurants = storage["Restaurants"]

if "Day" not in storage:
    storage["Day"] = 0
day = storage["Day"]

if "Week" not in storage:
    storage["Week"] = 0

current_week = storage["Week"]

if "Weeks" not in storage:
    storage["Weeks"] = {current_week:{}}

weeks = storage["Weeks"]

if "Sort Type" not in storage:
    storage["Sort Type"] = 0

sort_type = storage["Sort Type"]

if "sorted_restaurants" not in storage:
    storage["sorted_restaurants"] = sorted(restaurants.keys())

sorted_restaurants = storage["sorted_restaurants"]

print(" Defining functions")
def clear():
    """
    Clears the screen in unix based or windows based systems.
    """
    os.system("cls||clear")

print("    Building menus")

def main_menu():
    """
    The main menu of the program. Contians all the nessary loops for all menus.
    """
    global current_week
    global day
    running = True
    """
    Primary Loop
    """
    while running:
        clear()
        print(f"\tPlease select a Restaurant for {days[day]}:\n"
              "\t==========================================\n"
              "\t0: to quit.\n"
              "\t1: to manage restaurants.")
        menu_offset = 2
        display_resuarants(menu_offset)
        user_input = input(f"\tI would like to: ")

        if vaildate_input(user_input, min_value=0, max_value=len(restaurants)+1):
            user_choice = int(user_input)

        else:
            print(f"\tInvaild input:{user_input}")
            print(f"\tPlease choose only 0 through {len(restaurants)+menu_offset}.\n"
                  "\tHit enter to return to the main menu")
            #Holding for user to hit return
            input()
            continue

        if (len(restaurants) + 1) >= user_choice >= menu_offset:
            user_choice -= menu_offset
            restaurant = sorted_restaurants[user_choice]
            if restaurant in weeks[current_week]:

                if weeks[current_week][restaurant] < 3:
                    restaurants[restaurant] += 1
                    weeks[current_week][restaurant] += 1
                    next_day()
                    sort()

                else:
                    print(f"\tI am sorry you have been to {restaurant}")
                    print("\t{weeks[current_week][restaurant]} times in a week.\n"
                          "\tPlease pick another restaurant")
                    #Holding for user to hit return
                    input(f"\tHit enter to return to selection menu")
                    continue

            else:
                weeks[current_week][restaurant] = 1
                restaurants[restaurant] += 1
                next_day()
                sort()

        elif user_choice == 1:
            clear()
            managment_menu()
            continue

        elif user_choice == 0:
            clear()
            print("Thank you for using the lunch traker.")
            print("Packing up variables")
            storage["Restaurants"] = restaurants
            storage["Day"] = day
            storage["Week"] = current_week
            storage["Weeks"] = weeks
            storage["Sort Type"] = sort_type
            storage["sorted_restaurants"] = sorted_restaurants
            print("Closing storage.")
            storage.close()
            print("Have a wonderful day.")
            running = False
            continue

def managment_menu():
    """
    Menu that allows the user to configure the program.
    """
    managing = True
    global restaurants
    global sort_type
    while managing:
        clear()
        print(f"\tWhat would you like to do?\n"
              "\t==========================================\n"
              "\t0: changing sorting to sort by name.\n"
              "\t1: change sorting to sort by most visited.\n"
              "\t2: change sorting to sort by least visited.\n"
              "\t3: delete a restaurant.\n"
              "\t4: add a restaurant.\n"
              "\t5: go back.")
        user_input = input(f"\tI would like to: ")

        if not vaildate_input(user_input, min_value=0, max_value=5):
            print(f"\tPlease select either 0 through 2 it change sorting,\n"
                  "\t3 to delete a restaurant, or 4 to add a restaurant.\n"
                  "\t Hit enter to continue.")
                #Holding for user to hit return
            input()
            continue

        else:
            user_choice = int(user_input)

        if user_choice == 0:
            sort_type = 0
            sort()
            clear()
            display_resuarants()
            #Holding for user to hit return
            input(f"\tSort done. Hit enter to continue.")

        elif user_choice == 1:
            sort_type = 1
            sort()
            clear()
            display_resuarants()
            input(f"\tSort done. Hit enter to continue.")

        elif user_choice == 2:
            sort_type = 2
            sort()
            clear()
            display_resuarants()
            print(f"\tSort done. Hit enter to continue.")
            input()

        elif user_choice == 3:
            remove_restaurant()

        elif user_choice == 4:
            add_restuarant()

        elif user_choice == 5:
            managing = False

def sort():
    """
    Updates the sorted_restaurants list base on current restuarnts and sort type.
    """
    global sorted_restaurants
    sorted_restaurants = []
    if sort_type == 0:
        sorted_restaurants = sorted(restaurants.keys())

    elif sort_type == 1:
        sorted_restaurants_tuples = sorted(restaurants.items(),
                                           key=itemgetter(1))

        for item in sorted_restaurants_tuples:
            sorted_restaurants.append(item[0])

    elif sort_type == 2:
        sorted_restaurants_tuples = sorted(restaurants.items(), key=itemgetter(1), reverse=True)

        for item in sorted_restaurants_tuples:
            sorted_restaurants.append(item[0])

def vaildate_input(target, min_value=None, max_value=None):
    """
    vaildates user input to check if it is an
    integer inclusively bewteen the min and max value.
    """
    return target.isnumeric() and (min_value <= int(target) <= max_value)

def remove_restaurant():
    """
    The menu that removal of restuarnts from the restaurant list.
    """
    choosing = True
    while choosing:
        clear()
        print("\tWhich restaurant would you like to delete?\n"
              "\t==========================================\n"
              "\t0: Go back to previous menu")
        menu_offset = 1
        display_resuarants(offset=menu_offset)
        user_input = input(f"\tI would like to delete: ")
        if vaildate_input(user_input, min_value=0, max_value=len(restaurants)):
            user_choice = int(user_input)

        else:
            print(f"\t{user_input} is invaild please select again.")
            print(f"\tVaild range is 0 through {len(restaurants)}\n"
                  "\tHit enter to return to the selection menu")
            #Holding for user to hit return
            input()
            continue

        if user_choice == 0:
            choosing = False
            continue

        else:
            user_choice -= menu_offset
            del restaurants[sorted_restaurants[user_choice]]
            sort()
            clear()
            display_resuarants()
            input(f"\tRestaurant deleted hit enter to return to the previous menu")
            choosing = False

def add_restuarant():
    """
    Menu for the user to add Restaurants
    """
    clear()
    print(f"\tThe current list is:")
    display_resuarants()
    user_input = input(f"\tWhat is the name of the new restaurant? ")
    restaurants[user_input] = 0
    sort()
    clear()
    print(f"\t{user_input} added to restaurant list.")
    display_resuarants()
    input(f"\tHit enter to return to the previous menu.")

def display_resuarants(offset=0):
    """
    Displays the restuarnts list.
    Takes an integer to set how far the starting number if offset
    """
    for i in range(len(restaurants)):
        name = sorted_restaurants[i]
        print(f"\t{i+offset}: {name} visited {restaurants[name]}")

def next_day():
    """
    Handles all the nessary variable transtion to move the day forward.
    """
    global day
    global current_week
    global weeks
    if day < 4:
        day += 1

    elif day == 4:
        day = 0
        current_week += 1
        weeks[current_week] = {}

    else:
        print("Whoops I have had an error {day} is an invaild value.\n"
              "Please contact the developer.")


main_menu()
