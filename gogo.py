# List Manipulation Exercise:

# Create a list of 5 items (strings or numbers).
# Add a new item to the end of the list and another at the second position.
# Remove the third item from the list.
# Print the list after each operation.
hyy = [45,76,34,86,45,87,56,7356,57,25,34]
hyy.append(444)
hyy.insert(1,16)
print(hyy)
hyy.remove(hyy[2])
print(hyy)

hyy.sort(reverse=True)
print(hyy)
hyy.reverse()
print(hyy)
# Tuple Operations:

# Create a tuple with 5 elements.
# Try to modify one of the elements. What happens?
# Perform slicing on the tuple to extract the second and third elements.
# Concatenate the tuple with another tuple.
# Set Operations:

# Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
# Find the union, intersection, and difference between the two sets.
# Add a new fruit to your set.
# Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?
# Tuple and Set Comparison:

# Create a list of elements and convert it into both a tuple and a set.
# Print both the tuple and the set.
# Try to add new elements to the tuple and set. What differences do you observe?
tpu = (34, 54,5657,767,3426,8687,266)
print(tpu[1:3])
tpu2 = (45,65,789)
tpu4 = tpu + tpu2
print(tpu4)

syy1 = {"apple", "banana", "mango"}
syy2 = {"guava", "tomato", "jamun", "apple"}
syy1.add("Ornge")
print(syy1)
syy3 = syy1 | syy2
print(syy3)
syy4 = syy1 & syy2
print(syy4)
syy5 = syy1 - syy2
print(syy5)

syy1.discard("ple")
print(syy1)