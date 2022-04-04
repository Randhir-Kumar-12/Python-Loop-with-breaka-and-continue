m=int(input("Enter frist number:"))
n=int(input("Enter second number:"))


list1=[]
a=m
while a>1:
    for i in range(2,a+1):
        if a%i==0:
            list1.append(i)
            break
    a//=i    
print(f"Prime factors of {m}=",list1)

list2=[]
b=n
while b>1:
    for i in range(2,b+1):
        if b%i==0:
            list2.append(i)
            break
    b//=i    
print(f"Prime factors of {n}=",list2)

for i in range(len(list1)):
    print(list1[i], end=' ')
print()
for j in range(len(list2)):
    print(list2[j], end=' ')
    

lcm=1
for j in range(len(list1)):
    for k in range(len(list2)):
        if list1[j]==list2[k]:
            lcm=lcm*list1[k]
            list1.remove(list1[k])
            list2.remove(list2[j])


print("list1=",list1)
print("list2=",list2)

print(f"HCM of {m} and {n}= {lcm}")

for item in list1:
    lcm=lcm*item

for items in list2:
    lcm=lcm*items

print(f"LCM of {m} and {n}= {lcm}")
