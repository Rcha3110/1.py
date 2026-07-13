# Lambda Function: Write a lambda function that multiplies two numbers.
multiple = lambda a, b: a * b
print(multiple(5,6))

#Recursive Function: Write a recursive function that calculates the sum of the first n numbers.
def add(n):
    if n == 0:
        return n
    return n + add(n-1)
print(add(5))

# Variable-Length Arguments: Write a function that accepts any number of arguments and returns their average.
def avgg(*num):
    print(sum(num)/len(num))

avgg(1,2,3,4,5)
'''Two different operations are happening here.
avgg(3,5,6) — inside, num is the tuple (3, 5, 6). But you don't print num itself — you print sum(num)/3. sum(num) adds up the tuple to get 14, 
and then / is the true division operator in Python 3, which always returns a float, even when the result would be a whole number
 (e.g., 6/3 gives 2.0, not 2). So 14/3 gives you a float like 4.666....add(9) — inside, f is the tuple (9,) (a one-element tuple, 
 since *f collects all positional args into a tuple). You print f directly — you never sum it or divide it. 
 So Python just shows you the tuple as-is.'''