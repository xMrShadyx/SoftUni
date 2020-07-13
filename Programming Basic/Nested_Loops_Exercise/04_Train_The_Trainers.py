n = int(input())

name = input()
total_average = 0
count = 0
while name != "Finish":
    count += 1
    average_sum = 0
    for i in range(0, n):
        average_sum += float(input())
    average_sum /= n
    total_average += average_sum
    print(f"{name} - {average_sum:.2f}.")

    name = input()

print(f"Student's final assessment is {total_average / count:.2f}.")
