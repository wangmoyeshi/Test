_# initiating empty lists, sets, and dictionary
books_list = []
authors_set = set()
books_dict = {}

# add books
books_list.append("python progamming")
authors_set.add("John Smith")
books_dict["python progamming"] = "John Smith"

books_list.append("Data Structures and Algorithms")
authors_set.add("Jane Doe")
books_dict["Data Structures and Algorithms"] = "Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

#search for book
search_title = input("Enter the title of book the search:")
if search_title in books_list:
    print(f"Book Found! Author:{books_dict[search_title]}")
else:
    print("Book Not Found!")

# display all books
print("List of Books:")
for book in books_list:
    print(book)

# remove a book
remove_title = input ("Enter the title of the book to remove or else enter the skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed successfully!")
    print("Books available: ", books_list)

else:
 print("Book not found!")