food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.

food = food.split(',')
food.sort()
equipment = equipment.split(',')
equipment.sort()
pets = pets.split(',')
pets.sort()
sleep_aids = sleep_aids.split(',')
sleep_aids.sort()

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = []
cargo_hold.append(food)
cargo_hold.append(equipment)
cargo_hold.append(pets)
cargo_hold.append(sleep_aids)
print('Cargo hold items: ',cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

cabinet_choice = int(input('Please enter a cabinet 0 - 3: '))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.

if 0 <= cabinet_choice < len(cargo_hold):
    selected_cabinet = cargo_hold[cabinet_choice]
    print(f"Contents of cabinet {cabinet_choice}: {selected_cabinet}")
else:
    print("Error: Please enter a number between 0 and 3.")


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

selected_item = input('Please enter the item you are looking for: ')

if selected_item in selected_cabinet:
    print(f'Cabinet {cabinet_choice} DOES contain {selected_item}')
else:
    print(f'Cabinet {cabinet_choice} DOES NOT contain {selected_item}')