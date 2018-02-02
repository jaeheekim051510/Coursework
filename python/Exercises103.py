#Part 1
dayDict = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursady",5:"Friday",6:"Saturday"}
day = int(input( "Day (0-6)? "))
print(dayDict[day])

#Part 2
day = int(input("Day (0-6)? "))
#Output
if day == 0 or day == 6:
    print("Sleep in!😀")
else:
    print("Go to work.☹️")
#Part 3
C = input("Temperature in C? ")
F = float(C) * 1.8 +32
print(f"{F} F")

#Part 4
serviceDict = {"GOOD":0.2,"FAIR":0.15,"BAD":0.1}

subtotal = int(input("The total is? "))
serviceQuality = input("The level of service was?(Good,Fair, Bad) ").upper()
tip = subtotal*serviceDict[serviceQuality]
total = tip + subtotal
print(f"Tip amount: ${tip}")
print(f"Total amount: ${total}")

#Part 5
serviceDict = {"GOOD":0.2,"FAIR":0.15,"BAD":0.1}

subtotal = int(input("The total is? "))
serviceQuality = input("The level of service was?(Good,Fair, Bad) ").upper()
numberOfPeople = int(input("Split how many ways? "))
tip = subtotal*serviceDict[serviceQuality]
total = tip + subtotal
print(f"Tip amount: ${tip}")
print(f"Total amount: ${total}")
print(f"Amount per person: ${total/numberOfPeople}")