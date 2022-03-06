#Alan Shaji
#21MCA002

limit=int(input("enter limit"))
print("enter intiger values")
list1=[]
for i in range(0,limit):
    data=int(input())
    list1.append(data)
for x in range(0,limit):
    if list1[x]>100:
        list1[x]="over"

print(list1)
