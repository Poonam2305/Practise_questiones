num = int(input("enter the number: "))
print(num)
fact = 1
if num < 0:
    print("Not Possible")
else:
    for i in range(1, num+1):
        fact = fact * i
    print("the factorial of given number is: ",fact)