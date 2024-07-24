lower_limit = int(input("entr the lower limit: "))
print("the lower limit is: ", lower_limit)
upper_limit = int(input("entr the upper limit: "))
print("the upper limit is: ", upper_limit)
sum_of_numbers = 0
for i in range(lower_limit, upper_limit + 1):
    print(i)
    sum_of_numbers = sum_of_numbers + i
print("the sum is: ", sum_of_numbers)
