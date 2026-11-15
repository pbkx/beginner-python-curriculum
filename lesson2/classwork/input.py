# Input prints a line, and then returns what the user types
name = input("What is your name? ")
print("Hi", name)

# input ALWAYS returns a string
year = input("What year is it? ")
print("It is currently", year)

year_num = int(year)  # casting to an integer
print("Next year is", year_num + 1)

# You can shorten this process:
user_number = int(input("Give me a number: "))
print(user_number + 1)