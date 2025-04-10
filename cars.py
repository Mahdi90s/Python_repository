cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the orginal list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
# it reversed my list from assending to decessending before sort it first

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# Exercise 3.8 Seeing the world

favourite_place = ['UK', 'US', 'UAE','Ankara', 'Londn'] 
favourite_place.sort()
print(favourite_place)

favourite_place = ['UK', 'US', 'UAE','Ankara', 'Londn']
favourite_place.sort(reverse=True)
print(favourite_place)


favourite_place = ['UK', 'US', 'UAE','Ankara', 'Londn']
favourite_place.reverse()
print(favourite_place)

# Exercise 3.9 Dinner Guests

guest_list = ['arta', 'mahdi', 'micheal']
insert_guest = guest_list.insert(0,'jim')
insert_guest = guest_list.insert(2,'jack')
insert_guest = guest_list.insert(4,'suzan')
del guest_list[2]
print(len(guest_list))