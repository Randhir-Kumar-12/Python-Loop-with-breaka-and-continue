m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))

print(f"Pime number from {m} to {n}:")
if m==0:
    m=m+2
elif m==1:
    m=m+1
        
for i in range(m,n+1): # outer loop
    count=1
    for j in range(2,i+1): # j variable can be used only inside this loop
        count=count+1      # Inner loop
        if i%j==0:
            break
    if i==count:
        print(i, end=' ') 
    count=1 