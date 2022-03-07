def uclc(str):
    uc = 0
    lc = 0
    for i in str:
        if (i.upper()):
            uc = uc + 1
        elif (i.lower()):
            lc = lc + 1
    print("The number of uppercase characters is:")
    print(uc)
    print("The number of lowercase characters is:")
    print(lc)

str = input("Enter a string:")