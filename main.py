import sqlite3

def main():
    def display_books(cursor):
        # Function to display books in a table format
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        if books:
            print("{:<30} {:<30} {:<10}".format("Book Name", "Author", "Pages"))
            print("-" * 70)
            for book in books:
                print("{:<30} {:<30} {:<10}".format(book[0], book[1], book[2]))
        else:
            print("No books available to display.")

    # Connect to SQLite database
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    # Create the books table if it does not exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                      (name TEXT, author TEXT, pages INTEGER)''')

    choice = 0
    while choice != 4:
        print("\n***Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Adding a book...")
            n_book = input("Enter the name of the book: ")
            n_author = input("Enter the name of the author: ")
            n_pages = input("Enter the number of pages: ")
            cursor.execute("INSERT INTO books (name, author, pages) VALUES (?, ?, ?)", (n_book, n_author, n_pages))
            conn.commit()
            print("Book added successfully!")
        elif choice == 2:
            print("Looking up a book...")
            keyword = input("Enter search term: ")
            cursor.execute("SELECT * FROM books WHERE name LIKE ? OR author LIKE ? OR pages LIKE ?", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
            books = cursor.fetchall()
            if books:
                for book in books:
                    print("{:<30} {:<30} {:<10}".format(book[0], book[1], book[2]))
            else:
                print("No book found with the given keyword.")
        elif choice == 3:
            print("Displaying all books...")
            display_books(cursor)
        elif choice == 4:
            print("Quitting Program")
        else:
            print("Invalid choice. Please try again.")

    print("Program Terminated!")
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
