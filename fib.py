limit = int (input("enter a limit:  "))

num1 = 0
num2 = 1

next = num1 + num2

while next < limit :
    print (next)

    num1 = num2
    num2 = next
    next = num1 + num2

