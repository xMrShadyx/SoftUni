def reverse_string(s):
    st = []
    for ch in s:
        st.append(ch)
    
    reversed_text = []
    
    while st:
        ch = st.pop()
        reversed_text.append(ch)
    
    return ''.join(reversed_text)


print(reverse_string(input()))


# def reverse_string(s):
#   return [::-1]
#
# print(reverse_string(input()))
