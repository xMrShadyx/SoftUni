num = int(input())
sum = 0
for x in range(1, num):
    if num % x == 0:
        sum += x
if sum == num:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")




# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     if sum == n:
#         print("We have a perfect number!")
#     else:
#         print("It's not so perfect.")
#
#
# num = int(input())
# perfect_number(num)