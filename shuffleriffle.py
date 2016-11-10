
def shuffle(mylist):
    length=len(mylist)
    newlength=length//2
    stack1=mylist[0:newlength]
    stack2=mylist[newlength:]
    stack=[]
    i=0
    for i in range(0,newlength):
        stack.append(stack1[i])
        stack.append(stack2[i])
        i=i+1   
    return stack

def howmany_shuffles(mylist):
    count=1
    global x
    x=mylist
    y=mylist
    while shuffle(y)!=x:
        y=shuffle(y)
        count+=1
    return count  
        
    

        
        
    



    
        
        
        
        
