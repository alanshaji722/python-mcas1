#Alan Shaji
#21MCA002

def repl(str):
    s=str[0]
    data=str.replace(s,'$')
    data=s+data[1:]
    return data
print(repl("onion"))
