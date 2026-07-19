pet = "cat"

def show_pet():
    print("The pet is", pet)

show_pet()

def adopt_parrot():
    global pet  # Correct way to change a global variable
    pet = "parrot"

adopt_parrot()
show_pet()