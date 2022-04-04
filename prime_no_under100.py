
print("Prime number under 100:")
for i in range(2,101):
    count=1
    for j in range(2,i+1):
        count=count+1
        if i%j==0:
            break
    if i==count:
        print(i, end=' ') 
    count=1       