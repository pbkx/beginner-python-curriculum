fruit = ["banana", "apple", "cherry", "orange"]

flag = False  # assume there is no apple in our list
for i in range(len(fruit)):  # Go through each item in the list
    if fruit[i] == "apple":  # If the current item is apple
        flag = True  # Update our guess to true
        break  # Exit the loop after finding
print(flag)

if "apple" in fruit:
    print("found apple")
else:
    print("no apples found")