
n=int(input("Enter first N prime number:"))
m=2
count=0 
while m>=2:  # m is globle variable
    for j in range(2,m+1): # j is aslo global variale
        if m%j==0:
            break
    
    if j==m:
        count=count+1
        print(m, end=' ')   
    elif count==n:
        break    
    
    m=m+1 
