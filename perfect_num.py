num: int = int(input("enter the number: "))
print("the given number is: ", num)
sum: int = 0
for i in range(1, num):
    if num %i ==0:
        sum = sum+i
if sum == num:
    print("the given number is perfect number")
else:
    print("the given number is not  perfect number")



