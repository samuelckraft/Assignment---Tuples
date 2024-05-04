#Task 1
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    title = input("Enter title of book: ")
    author = input(f"Enter author of '{title}': ")
    in_library = True
    for book in library:
        if title.lower() == book[0].lower():
            print("Book already in library")
            in_library = False
    if in_library == True:
        library.append((title, author))
        print(f"Book added: {title} by {author}")

    print("\nLibrary Catalog: ")
    for item in library:
        name, writer = item
        print(f"- {name} by {writer}")


add_book(library)