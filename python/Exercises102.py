#First part
name = input("What is your name? ")
print(f"Hello, {name}!")

#Second Part
name = input("WHAT IS YOUR NAME? ")
print(f"Hello, {name}!".upper())
print(f"YOUR NAME HAS {len(name)} IN IT! AWESOME!")

#Third part
print("""Please fill in the blanks below:
___(name)___'s favorite breed of guinea pig is ___(breed)___
""")
name=input("What is your name? ")
breed=input("What is your favorite breed? ")
print(f"{name}'s favorite breed of Guinea pig is {breed}.")