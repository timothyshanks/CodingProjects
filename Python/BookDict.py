# Create and initialize a list 'books' with some duplicated book titles of your choice
books = ['Robin Hood', 'Beowulf', 'Sir Gawain', 'Beowulf']

# Create an empty dictionary 'book_count' to store the count of each book
book_count = {}

for book in books:
    if book_count.get(book) is not None:
        book_count[book] += 1
    else:
        book_count[book] = 1
# Loop through each book in the 'books' list
# TODO: Check if the book is already in dictionary, if so increment its count, otherwise add it with count 1

# Finally, print the 'book_count' dictionary
print(book_count)
