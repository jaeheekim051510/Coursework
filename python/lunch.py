#! /usr/bin/env python3
"""
Allow the user to track where they went to lunch.
"""
import shelve
import os

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

week = storage["Week"]

if "Weeks" not in storage:
    storage["Weeks"] = {week:{}}

weeks = storage["Weeks"]

if "Sort Type" not in storage:
    storage["Sort Type"] = 0

sort_type = storage["Sort Type"]

if "sorted_restaurants" not in storage:
    storage["sorted_restaurants"] = sorted(restaurants.keys())

sorted_restaurants = storage["sorted_restaurants"]

print(" Defining functions")
def clear():
    os.system("cls||clear")

print("    Building menus")
def main_menu():
    global week
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
        for i in range(len(restaurants)):
            name = sorted_restaurants[i]
            print(f"\t{i+2}: {name} visited {restaurants[name]}")

        user_input = input(f"\tI would like to: ")
        if vaildate_input(user_input, 0, len(restaurants)+1):
            user_choice = int(user_input)

        else:
            print(f"\tInvaild input:{user_choice}\n"
                   "\tPlease choose only 0 through {i+2}.\n"
                   "\tHit enter to return to the main menu")
            input()
            continue

        if user_choice <= len(restaurants) + 1 and user_choice >= 2:
            user_choice -= 2
            restaurant = sorted_restaurants[user_choice]
            if restaurant in weeks[week]:

                if weeks[week][restaurant] < 3:
                    restaurants[restaurant] += 1
                    weeks[week][restaurant] += 1

                else:
                    print(f"\tI am sorry you have been to {restaurant} {weeks[week][restaurant]} times in a week.\n"
                           "\tPlease pick another restaurant")
                    input(f"\tHit enter to return to selection menu")
                    continue

            else:
                weeks[week][restaurant] = 1
                restaurants[restaurant] += 1

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
            storage["Week"] = week
            storage["Weeks"] = weeks
            storage["Sort Type"] = sort_type
            storage["sorted_restaurants"] = sorted_restaurants
            print("Closing storage.")
            storage.close()
            print("Have a wonderful day.")
            running = False
            continue
        if sum(weeks[week].values()) == 5:
            week += 1
            weeks[week] = {}
            day = 0
def managment_menu():
    managing = True
    global restaurants
    while managing:
        clear()
        print(f"\tWhat would you like to do?\n"
               "\t==========================================\n"
               "\t0: changing sorting to sort by name.\n"
               "\t1: change sorting to sort by most visited.\n"
               "\t2: change sorting to sort by least visited.\n"
               "\t3: delete a restaurant.\n"
               "\t4: add a restaurant.")
        user_input = input("I would like to: ")
        if not vaildate_input(user_input, 0, 4):
                print(f"\tPlease select either 0 it delete a restaurant or\n"
                        "\t1 to add a restaurant. Hit enter to continue")
                input()
                continue
        else:
            user_choice = int(user_input)
        if user_choice == 3:
            remove_restaurant()
def sort():
    global sorted_restaurants
    if sort_type == 0:
        sorted_restaurants = sorted(restaurants.keys())
    if sort_type == 1:
        reverse_restaurants = reverse_dict(restaurants)
        sorted_revrse_restaurants = sorted(reverse_restaurants.keys())
        sorted_restaurants = []
        for key in sorted_revrse_restaurants:
            sorted_restaurants.append(reverse_restaurants[key])
    if sort_type == 2:
        reverse_restaurants = reverse_dict(restaurants)
        sorted_revrse_restaurants = sorted(reverse_restaurants.keys(),)
        sorted_restaurants = []
        for key in sorted_revrse_restaurants:
            sorted_restaurants.append(reverse_restaurants[key], reverse=True)
def reverse_dict(dictionary):
    reversed_dict = {}
    for item in dictionary:
        reversed_dict[dictionary[item]] = item

    return reversed_dict

def vaildate_input(target, min_value, max_value):
    return target.isnumeric() and (min_value < int(target) < max_value)

def remove_restaurant():
    clear()
    print("\tWhich restaurant would you like to delete?\n"
          "\t==========================================")
    for i in range(len(restaurants)):
        name = sorted_restaurants[i]
        print(f"\t{i}: {name} visited {restaurants[name]}")
    user_input = input("I would like to delete: ")
    if vaildate_input(user_input,0,len(restaurants)-1):
        user_choice = user_input()
    else 
main_menu()
