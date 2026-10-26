#WHILE LOOP
#Print all the numbers from one to ten using while loop
# i = 1
# while (i<=10):
#     print(i)
#     i+=1
#Print numbers from 10 down to 1 in reverse order
# i=10
# while (i>=1):
#     print(i)
#     i-=1
#Print all even numbers between 1 and 100
even = 1
while True:
    if (even%2==0 and even<=100):
        print(even)
    even +=1
    if even ==101:
        break

#Print all even numbers between 1 and 100
odd = 1
while True:
    if (odd%2!=0 and odd<=100):
        print(odd)
    odd +=1
    if odd == 101:
        break