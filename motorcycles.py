motorcycles = ['honda' , 'yamaha' , 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles =[]

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda' , 'yamaha' , 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles = ['honda' , 'yamaha' , 'suzuki']

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda' , 'yamaha' , 'suzuki']
print(motorcycles)

popped_motocycle = motorcycles.pop()
print(motorcycles)
print(popped_motocycle)

last_owned = motorcycles.pop()
print (f"The last motorcycle I owned was a {last_owned.title()}.")


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Exercise 3.4 : Guest List

guest_list = ['arta', 'mahdi', 'micheal']
print (f"""
        \nDear {guest_list[0].title()} this is an invetaion to my Firday party.
        \nDear {guest_list[1].title()} this is an invetaion to my Firday party.
        \nDear {guest_list[2].title()} this is an invetaion to my Firday party.""")

# Exercise 3.5 Changing Guest List

guest_list = ['arta', 'mahdi', 'micheal']
print(guest_list[-1])



guest_list = ['arta', 'mahdi', 'micheal']
popped_guest = guest_list.pop()
print(guest_list)
print(popped_guest)

guest_list = ['arta', 'mahdi', 'micheal']
insert_guest = guest_list.insert(0,'jim')
insert_guest = guest_list.insert(2,'jack')
insert_guest = guest_list.insert(4,'suzan')
popped_geust = guest_list.pop()
print (f"""
        \nDear {guest_list[0].title()} this is an invetaion to my Firday party.
        \nDear {guest_list[1].title()} this is an invetaion to my Firday party.
        \nDear {guest_list[2].title()} this is an invetaion to my Firday party.
        \nDear {guest_list[3].title()} this is an invetaion to my Firday party.
        \nDear {guest_list[4].title()} this is an invetaion to my Firday party.""")

guest_list = ['arta', 'mahdi', 'micheal']
insert_guest = guest_list.insert(0,'jim')
insert_guest = guest_list.insert(2,'jack')
insert_guest = guest_list.insert(4,'suzan')
del guest_list[2]
print(guest_list)
