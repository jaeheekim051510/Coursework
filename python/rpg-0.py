#! /usr/bin/env python3
import os
import time
"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    name = input("\tWhat is your name? ")
    enemy = input("\tWhich enemy do you want to fight?\n"
                  "\t0 for goblin, 1 for zombie.")
    if enemy == "0":
        enemy = Character(name="Goblin", power=2, health=6)
    elif enemy == "1":
        enemy = Undead(name="Zombie", power=2, health=6)
    player = Character(name=name, power=5, health=10)


    while enemy.health > 0 and player.health > 0:
        clear()
        player.status()
        enemy.status()
        print(f"\n\tWhat do you want to do?")
        print(f"\t1. attack {enemy.name}\n"
              "\t2. do nothing\n"
              "\t3. flee\n"
              "\t> ", end="")
        user_input = input()
        if user_input == "1":
            player.attack(enemy)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print(f"\t{enemy.name}: Why do you flee COWARD!")
            break
        else:
            print(f"Invalid input {user_input}")

        if enemy.is_alive():
            enemy.attack(player)
        time.sleep(3)
def clear():
    """
    Clears the screen in unix based or windows based systems.
    """
    os.system("cls||clear")

class Character():
    def __init__(self, name="Default", power=0, health=0):
        self.name = name
        self.power = power
        self.health = health
    def attack(self, target):
        target.attacked(self)

    def attacked(self, attacker=None):
        print(f"\t{attacker.name} does {attacker.power} damage to {self.name}.")
        self.health -= attacker.power
        if not self.is_alive():
            print(f"\t{self.name} is dead.")
    def is_alive(self):
        return self.health > 0
    def status(self):
        print(f"\t{self.name} has {self.health} health and {self.power} power.")
class Undead(Character):
    def attacked(self, attacker=None):
        print(f"\t{attacker.name} hits {self.name}.\n"
              "\tIt has no effect.")


main()
