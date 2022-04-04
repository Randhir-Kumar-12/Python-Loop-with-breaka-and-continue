n=int(input("Enter number:"))
m=n+1

while m:  # m is globle variable
    for j in range(2,m+1): # j is aslo global variale
        if m%j==0:
            break
    if j==m:
        print("Next prime number:",m)
        break    
    m=m+1    