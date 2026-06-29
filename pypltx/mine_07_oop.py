
class library:

    def __init__(self):
        self.books = []

    def add_book(self,title,author,isbn):
        book ={
            "title":title,
            "author":author,
            "isbn":isbn,
            "available":1

        }
        self.books.append(book)
        return book

    def get_book(self,isbn):
        for book in self.books:
            if book["isbn"] == isbn:
                return book

/ז

    # def checkout_book(self,isbn):
    #     for book in self.books:
    #         if book["isbn"] == isbn:
    #             book["available"] = 0
    def checkout_book(self, isbn):
        for book in self.books:
            if book["isbn"] == isbn:
                # If found and available, checkout and return success
                if book["available"] == 1:
                    book["available"] = 0
                    return "success"
                # If found but already checked out
                return "unavailable"
        # If the loop finishes without finding the ISBN
        return "not_found"

    def return_books(self,isbn):
        for book in self.books:
            if book["isbn"] == isbn:
                book["available"] = 1
                return True  # Exits the function immediately

        return False  # Only triggers if the loop finishes without finding the ISBN
"""
ORRRRR

# If self.books was a dictionary keyed by ISBN:
def return_books(self, isbn):
    if isbn in self.books:
        self.books[isbn]["available"] = 1
        return True
    return False

"""
def exe_07_oop():

    daily = library()
    # Add some initial books
    daily.add_book("Python Basics", "John Smith", "1234567890")
    daily.add_book("Advanced Python", "Jane Doe", "0987654321")

    while True:
        print("\n1. Display books")
        print("2. add book")
        print("3. checkout book")
        print("4. return books")
        print("5. exit program")
        print("6: show specific book")

        choice = input("Choose option (1-6): ")

        if choice == '1':
            daily.show_books()
# Q1 (partial) 
        elif choice == '2':
            # daily.add_book(input("Title: "),input("Author: "),input("isbn: "))
            print(daily.add_book(input("Title: "), input("Author: "), input("isbn: ")))
        elif choice == '3':
            # daily.checkout_book(input("isbn: "))
            i = input("isbn: ")
            print(daily.checkout_book(i))
            print(daily.get_book(i))
        elif choice == '4':
            i = input("isbn: ")
            print(daily.return_books(i))
            print(daily.get_book(i))
        elif choice == '5':
            break
        elif choice == '6':
            i = daily.get_book(input("isbn: "))
            # print(daily.get_book(i))
            print(i)
        else:
            print("Invalid choice!")


def main():
    """Main function to run all chapter demonstrations"""
    exe_07_oop()

if __name__ == "__main__":
    main()
