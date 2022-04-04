list1=[]
n=int(input("Enter number:"))
b=n
while b>1:
    for i in range(2,b+1):
        if b%i==0:
            list1.append(i)
            break
    b//=i    
print(f"Prime factors of {n}=",list1)
