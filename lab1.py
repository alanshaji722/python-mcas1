def compound_rate(p, r, n):

    A = p * (pow((1 + r / 100), n))

    CI = A - p

    print("Amount: ", A)
    print("Compound Interest", CI)

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate: "))
n = float(input("Enter the time period: "))

compound_rate(p, r, n)