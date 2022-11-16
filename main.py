
def FilterNum(num):
    x = ""
    for n in num:
        if n.isnumeric():
            x += n
    if x == "":
        x = 1
    return int(x)


def FilterOpp(op):
    x = ""
    for n in op:
        if n == "+" or n == "-" or n == "*" or n == "/":
            x = n
    if x == "":
        x = "+"
    return x


num_one = FilterNum(input("1st number: "))

op = FilterOpp(input("Operator: "))

num_two = FilterNum(input("2nd number: "))

if op == "+":
    print(num_one + num_two)
elif op == "-":
    print(num_one - num_two)
elif op == "*" or op == "x":
    print(num_one * num_two)
elif op == "/":
    if num_two == 0:
        print("Division by 0 is not possible")
    else:
        print(num_one / num_two)
else:
    print("Not a valid operation :(")


