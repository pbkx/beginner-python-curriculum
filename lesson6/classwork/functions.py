# Function that returns a greeting message
def make_greeting():
    greeting = "Hello, world!"
    return greeting  # Sends the greeting variable back to where the function was called

message = make_greeting()  # Call the make_greeting() function
print(message)

# Function that returns a personalized greeting based on name
def build_face():
    face = ":)"
    return face

person = build_face()  # Call the build_face() function
print(person)

# Paramters are local variables that can only be accessed inside the function.

# Function that returns a personalized greeting based on name
def personalized_greeting(name):  # name is a parameter.
    greeting = "Hello, " + name + "!"
    return greeting

text = personalized_greeting("Alice")
print(text)

# Function that returns a rectangles area based on length and width.
def rectangle_area(length, width):  # length and width are parameters.
    area = length * width
    return area

print("The area of a 5x3 rectangle is:", rectangle_area(5, 3))