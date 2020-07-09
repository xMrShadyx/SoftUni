def chars_as_string(start, end):
    res = ''
    for i in range(ord(start) + 1, ord(end)):
        res += chr(i) + ' '

    return res


start = input()
end = input()

result = chars_as_string(start, end)
print(result)
