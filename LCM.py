list1=[]
list2=[]
n=int(input("Enter first number:"))
m=int(input("Enter first number:"))
lcm=1

while n>1:
    i=2
    while n>=i:
        if n%i==0:
            list1.append(i)
            break
        i=i+1
    n//=i
    i=2       

while m>1:
    j=2
    while m>=j:
        if m%j==0:
            list2.append(j)
            break
        j=j+1
    m//=j
    j=2

for k in range(0, len(list1)):
    for l in range(1, len(list1)-1):
        if list1[k]==list1[l]:
            lcm=lcm*list1[k]
            list1.remove(list1[k])
            list1.remove(list1[l-1])
            break

for x in range(0, len(list2)):
    for y in range(1, len(list2)-1):
        if list2[x]==list2[y]:
            lcm=lcm*list2[x]
            list2.remove(list2[x])
            list2.remove(list2[y-1])
            break
print(f"lcm= {lcm}")

for item in list1:
    lcm=lcm*item

for items in list2:
    lcm=lcm*items

print(f"LCM of {n} and {m}= {lcm}")
