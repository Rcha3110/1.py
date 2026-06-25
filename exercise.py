# Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:

# "You are an adult" if the age is greater than or equal to 18.
# "You are a minor" if the age is less than 18.
# Use >= and < comparison operators.
age = int(input("What's your age?? Tell me your age: "))
if age >= 18:
    print("You are an adult, oh I never knew that lol so yeah you can access this site")
else:
    print("This website is only for adults. You are a minor. Immediately leave the website for your better mental health")
# Membership Operator Exercise: Write a Python program that:

# Takes a string as input from the user.
# Checks if the letter 'a' is in the string (using in).
# Checks if the string doesn't contain the word "Python" (using not in).
strr = input("Write something: ")
print("a" in strr)
print("Python" not in strr)
# Bitwise Operator Task: Given two integers, write a Python program that:

# Prints the result of a & b, a | b, and a ^ b.
# Shifts the bits of a two positions to the left (a << 2).
# Shifts the bits of b one position to the right (b >> 1).
bh = 45
ch = 54
print(bh & ch) 
print(bh | ch) 
print(bh ^ ch) 
print(bh << 2) 
print(ch >> 1) 