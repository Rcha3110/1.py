def greet():
    print("Hello world")
greet()

def greet_user():
    name = input("Enter your name: ")
    print(f"Hello {name}! Ntmy")

greet_user()

def add_numbers(a,b):
    return a + b
r = add_numbers(5,78)
print(r)

#Difference between print and return
'''print() — shows something to a human

*It sends text to the screen (technically, standard output).
*It's a side effect — it doesn't hand any value back to the code that called it.
*The function's actual return value is still None unless you explicitly return something.

return — sends a value back to the caller

*It exits the function and hands a value back to wherever the function was called.
*That value can then be stored in a variable, used in a calculation, passed to another function, etc.
*It does not display anything on screen by itself.'''
def add_print(a, b):
    print(a + b)      # just displays it

def add_return(a, b):
    return a + b       # hands it back

x = add_print(5, 3)    # prints "8" to the screen
print(x)                # None  <-- because add_print never returned anything

y = add_return(5, 3)    # prints nothing on its own
print(y)                 # 8   <-- because y actually holds the value