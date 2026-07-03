# Basic Counting with while Loop:
# Write a program that counts from 1 to 10 using a while loop.

# Odd Numbers Printer:
# Create a program that prints all odd numbers between 1 and 20 using a while loop.
# Ticket Booking Simulation:

# Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked."
# Countdown Timer:

# Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.
i=1   #prgm 1
while i<=10:
    print(i, end=" ")
    i +=1 
#prgm 2
i = 1
while True:
    if i % 2 != 0:
        print(i, end=" ")
        i +=2   
    if i>20:
        break
i = 1
while True:
    if i % 2 != 0:
        print(i, end=" ")
        i +=1
        continue
    i+=1  
    if i>20:
        break

seats = 8
is_booked = True
while is_booked:
    print(f"Seat number {seats} booked")
    seats -=1
    if seats == 0:
        print("Sorry, all seats booked!")
        break
  
count = 10
while True:
    print(count)
    count -=1
    if count ==0:
        print("Happy New Year")
        break