from re import A


list1=[]
list2=[]
n=int(input("Enter first number:"))
m=int(input("Enter first number:"))
hcm=1
a=n
b=m
while n>1:
    i=2
    while n>=i:
        if n%i==0:
            list1.append(i)
            break
        i=i+1
    n//=i
    i=2       
print("list1=",list1)

while m>1:
    j=2
    while m>=j:
        if m%j==0:
            list2.append(j)
            break
        j=j+1
    m//=j
    j=2
print("list2=",list2)
'''
for k in range(0, len(list1)):
    for l in range(0, len(list2)):
        if list1[k]==list2[l]:
            hcm=hcm*list1[k]
            list1.remove(list1[k])
            list2.remove(list2[l])
            break
print("list1=",list1)
print("list2=",list2)'''

for k in range(0, len(list1)):
    for l in range(1, len(list1)-1):
        if list1[k]==list1[l]:
            hcm=hcm*list1[k]
            list1.remove(list1[k])
            list1.remove(list1[l])
            break
print("list1=",list1)

for x in range(0, len(list2)):
    for y in range(1, len(list2)-1):
        if list2[x]==list2[y]:
            hcm=hcm*list2[x]
            list2.remove(list2[x])
            list2.remove(list2[y])
            break
print("list2=",list2)


print(f"HCM of {a} and {b}= {hcm}")
