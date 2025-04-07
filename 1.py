# for loop - for iterating over a sequence and execute a block of code repeatedly 
# Range - (1,10) -- Here final number's not included (start, stop, step) 
# range (4, 25, 2)- by default step is 1, but if it's 2 then it would come like 4,6,8,...
#string is also a collection of every character. So we can iterate over the string bb="aarcha"
#when we use enumerate function the output comes like this : (0, 'a')
# (1, 'a')
# (2, 'r')
# (3, 'c')
# (4, 'h')
# (5, 'a')
city=["Bengaluru","Mysuru","Hubli","Hassan","Manguluru"]
for i in city:
    print(i)      
j=1
while j<=10:
    print(j, end=" ")
    j+=1
bb="aarcha"
for k in enumerate(bb):
    print(k)