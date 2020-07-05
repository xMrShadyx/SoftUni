fave_book = input()

is_found = False
count_books = 0

line = input()
while line != 'No More Books':
    current_book = line

    if current_book == fave_book:
        print(f"You checked {count_books} books and found it.")
        is_found = True
        break

    count_books += 1
    line = input()

if not is_found:
    print("The book you search is not here!")
    print(f"You checked {count_books} books.")