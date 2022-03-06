#Alan Shaji
#21MCA002

string = input("enter word:")
if len(string) < 3:
  print(string)
elif string[-3:] == 'ing':
  print(string + 'ly')
else:
  print(string + 'ing')
