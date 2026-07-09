# List Manipulation:
# Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.
ka_foods = ["dosa", "idli", "obattu", "mudde", "neer dose", "mysuru pak", "chicken"]
new_ka_foods = [i.upper() for i in ka_foods]
print(new_ka_foods)
# Sum of Prices:
# Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.
foody = {"Dosa": 45, "Idli": 26, "Obattu": 80, "Mudde": 20, "Neer Dose": 50, "Mysuru Pak": 100, "Chicken": 123}
tot_cost =0
for cost in foody.values():
    tot_cost+=cost
print(tot_cost)
# List of Squares:
# Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.
liss = [m for m in range(1,11)]
lisssq = [sq**2 for sq in liss]
print(lisssq)
# Student Data Task:
# Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.
student_data = [
    {"name": "Aarcha", "age": 21, "marks": 23},
    {"name": "Hemanth", "age": 22, "marks": 83},
    {"name": "Rhea", "age": 18, "marks": 98},
]
for stu in student_data:
    print(f"Student name:{stu["name"]}")
    print(f"Student age:{stu["age"]}")
    print(f"Student marks:{stu["marks"]}")
    print("-"*20)

# Dictionary Comprehension:


# Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.
# Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

# Prints the entire matrix row by row.
# Prints the sum of each row in the matrix.