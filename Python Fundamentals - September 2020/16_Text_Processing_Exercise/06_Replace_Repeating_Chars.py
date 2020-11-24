def decrypt(index, arr):
    if index + 1 >= len(arr):
        return arr
    else:
        if arr[index] == arr[index + 1]:
            arr.pop(index + 1)
            return decrypt(index, arr)
        else:
            return decrypt(index + 1, arr)


line = input()
text = [line[i] for i in range(0, len(line))]
word = decrypt(0, text)
print(''.join(word))
