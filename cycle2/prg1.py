#Alan Shaji
#21MCA002

n=int(input("enter a limit"))
temp=1
for i in range(1,n+1):
    temp=i*temp
print(temp)
if n<0:
    print("no factorial for negative number")
