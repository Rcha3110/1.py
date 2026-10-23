print("Welcome to FLAMES game!!!")
print("Check your relationship status between you and your crush right now!!❤")
user=input("Type 'play' to play FLAMES, 'end' to exit: ")
is_on=True
while is_on:
    if user =='play':
        boy=input("What's your name?")
        girl=input("What's your crush's name?")
        dict={}
        for i in boy:
            if i not in dict:           #check these lines of code
                dict[i]=1
            elif i in dict:
                if dict[i]==1:
                    dict[i]-=1
                else:
                    dict[i]+=1
        for j in girl:
            if j not in dict:
                dict[j]=1
            elif j in dict:
                if dict[j]==1:
                    dict[j]-=1
                else:
                    dict[j]+=1
        num=0
        for letter in dict:
            if dict[letter] ==1:
                num +=1
        res= ["It's F...you are born to be friends","It's L...You are made for each other❤","It's A...affection is holding you together...Enahnce it","It's M...!!! Time to think of family plans","It's E...omg you are enemies!","It's S...I guess this is even worse than enemies lol bro and sis"]
        while len(res)>1:
            split_index=(num % len(res) -1)
            if split_index>=0:
                right=res[split_index + 1:]
                left=res[: split_index]
                res= right+ left
            else:
                res=res[:len(res)-1]
        print(res[0])
        is_on=False
    elif user =="end":
        print("Thank you, Hope you had a good time playing FLAMES using python")
        is_on=False
    else:
        print("Invalid input!!!")
        is_on=False
