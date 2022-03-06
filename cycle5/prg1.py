#Alan Shaji
#21MCA002

list =[]
f = open("demofile.txt" , 'r')
for x in f:
  print(x)
  list.append(x)
print("the list is ", list)