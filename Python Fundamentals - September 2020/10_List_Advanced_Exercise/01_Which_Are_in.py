list_1 = input().split(", ")
list_2 = input().split(", ")


result = [subst for subst in list_1 for word in list_2 if subst in word]
print(sorted(set(result), key=result.index))
