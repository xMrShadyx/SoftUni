n = int(input())

new_value = 0
new_snow = 0
new_time = 0
new_quality = 0

for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = int(snowball_snow / snowball_time)
    snowball_value1 = snowball_value ** snowball_quality

    if snowball_value1 > new_value:
        new_value = snowball_value1
        new_snow = snowball_snow
        new_time = snowball_time
        new_quality = snowball_quality


print(f"{new_snow} : {new_time} = {new_value} ({new_quality})")
