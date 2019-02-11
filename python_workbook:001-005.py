#1
name = "St.Robert CHS"
address = "8101 Leslie St."
city = "Thornhill"
province = "ON"
postal_code = "L3T 7P4"
telephone = "905-889-4982"
print(name)
print(address)
print("{}, {}" .format(city, province))
print(postal_code)
print(telephone)

#2
name = input("Enter your name")
print("Hello", name)
mood = input("How are you feeling")
if mood == "happy":
  print("THAT'S AWESOME!!")
elif mood == "sad":
  print("It's ok, it'll be better soon!")
else:
  print("cool, bye")

#3
length = float(input("Enter the length in meters"))
width = float(input("Enter the width in meters"))
area = length * width
print("The area of the room is:", area, "meters")

#4
farm_length = float(input("Enter the length in feet"))
farm_width = float(input("Enter the width in feet"))
farm_area = (farm_length * farm_width)/43560
print(farm_area, "acres")

#5
smaller_bottles = int(input("How many bottles of under 1L are recycled"))
bigger_bottles = int(input("How many large bottles of greater than 1L are recycled"))
refund = (smaller_bottles * 0.10) + (bigger_bottles * 0.25)
print("You earn back: $", refund)