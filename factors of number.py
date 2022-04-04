n=int(input("Enter number:"))
print("All factors of given number-")
for i in range(1,n+1):
    if n%i==0:
        print(i, end=' ')