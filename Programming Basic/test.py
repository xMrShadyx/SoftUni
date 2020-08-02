try:
    astr = 'Hello Bob'
    istr = int(astr)

except ValueError:
    print('Ebati Kavala')  # <- istr = int(astr)
else:
    print(istr)  # <- istr = astr
