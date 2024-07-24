given_num=int(input("enter the number: "))
print(given_num)
flag=0
for i in range(2,given_num):
    if given_num%i == 0:
        flag = 1
        break
if flag == 1:
       print("the number is not prime")
else:
       print("the number is prime")
