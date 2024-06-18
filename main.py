def main():

 try:
    # initialize books list
    booksList = []
    infile = open("theBooksLists.txt", "r")
    line = infile.readline()
    while line:
        booksList.append(line.rstrip("\n").split
        (","))
        line = infile.readline()
    infile.close()
 except FileNotFoundError :
    print("the <bookslist.txt> file is not found")

    print("Starting a new books lists!")
    booksList = []



    choice = 0 
    while choice !=4:
        print("***Books Manager ***")
        print ("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book>>>")

            nAuthor = input("Enter the name of theauthor>>>")
    
            nPages = input("Enter the number of pages >>>")

            booksList.append([nBook, nAuthor, nPages])

        elif choice == 2:
            print("Looking ip for a book ...")
            keyword = input("Enter search Term: ")
            for book in booksList:
                if keyword in book:
                   print(book)

        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(booksList)):
                print(booksList[i])
        
        elif choice == 4:
            print("Quiting Program")
    print("Program Terminatred!")
    

    #saving to external TXT file
    outfile = open("theBooksLists.txt","w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()

if __name__ == "__main__":
     main()