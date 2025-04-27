#Q10) Using Various functions  :
newlist=list(input("make the desired list"))
user_choice=input("what would you like to do?: Append,insert,pop,copy,remove")
if user_choice=="append":
    newlist.append("kickboxing")
    print(newlist)
elif user_choice=="insert":
    ind=int(input("enter the index"))
    val=input("enter the desired value")
    newlist.insert(ind,val)
    print(newlist)
elif user_choice=="remove":
    rem=input("enter the element that you want to get rid of")
    newlist.remove(rem)
    print(newlist)
elif user_choice=="pop":
    no=int(input("enter the index"))
    newlist.pop(no)
    print(user_list)
elif user_choice=="copy":
    newlist.copy()
    print(newlist)


    
    
            




             
             
