n=int(input("Enter number:"))
print("All prime factors of given number-")

count=1
while n>1:
    i=2
    while n>=i:
        if n%i==0:
            break
        i=i+1
    for j in range(2,i+1):
        count=count+1
        if i%j==0:
            break
    if count==i:
        print(i, end=' ')    

    n//=i
    i=2 

while n>1:
    i=2
    while n>=i:
        if n%i==0:
            break
        i=i+1
    print(i,end=' ')       
    n//=i
    i=2     