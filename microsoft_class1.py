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