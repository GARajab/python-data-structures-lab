# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.


# def example_list_function():
#     example_list = ["element1", "element2", "element3"]
#     for element in example_list:
#         print(element)


# # Call the function and print each element
# example_list_function()
# *******************************************************************
# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.


def manage_students():
    # your code here
    students = ["Mohamed", "Mohsen", "Salman", "Loay"]
    first_student = students[1]
    last_student = students[-1]
    return f"First student: {first_student}, Last student: {last_student}"


# Call the function and print the result
print("Exercise 1:", manage_students())


# *******************************************************************

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.


def combine_foods():
    foods = ("Burger", "Pizza", "Twister", "Brosted")
    meal = ""
    for food in foods:
        meal += food + " "
    return f"Meals are: {meal}"


print("Exercise 2:", combine_foods())


# *******************************************************************

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.


def slice_foods():
    # your code here
    foods = ("Burger", "Pizza", "Twister", "Brosted")
    last_two_foods = slice(2, 4)
    return foods[last_two_foods]


# Call the function and print the result
print("Exercise 3:", slice_foods())

# *******************************************************************


def hometown_info():
    # Create the dictionary with proper syntax
    home_town = {
        "city": "Hidd",
        "state": "Muharraq",
        "population": 10000,
    }

    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"

    return home_town_message


print("Exercise 4:", hometown_info())


# *******************************************************************


def list_home_town_items():
    home_town = {
        "city": "Hidd",
        "state": "Muharraq",
        "population": 10000,
    }
    home_town_items = []  # Define an empty list

    # Iterate over the key-value pairs
    for key, value in home_town.items():
        # Append formatted string to the list
        home_town_items.append(f"{key} = {value}")

    return home_town_items  # Return the list


# Call the function and print the result
print("Exercise 5:", list_home_town_items())

# *******************************************************************
