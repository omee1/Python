
#to display books = display_book
#to lend book = lend_book
#to add book = add_book
#to return book = return_book

class library():

    def __init__(self,name_of_library,list_of_books):
        self.name_of_library = name_of_library
        self.list_of_books = list_of_books
        self.lender_dict = {}
        print(f"welcome to {self.name_of_library}")

    def display_books(self):
        """ display books """
        #print(display_books.__doc__)
        return print(f"books avilable in library {list(self.list_of_books)}  ")

    def add_books(self):
        """ add books """

        print(lib_1.add_books.__doc__)
        while(1):
            book_name = input("enter the name of book which you want to add \n ")
            if book_name in self.list_of_books:
                print("the book which you wanted to add is already exist in library\n"
                      "try something new \n")
                continue
            else:
                 self.list_of_books.append(book_name)
                 print("book added successfully\n")
                 print(self.list_of_books)
            break
        return print(" thank you \n")

    def lend_book(self):
        """ book lenders """
        print(lib_1.lend_book.__doc__)
        self.lender_name = input("enter lenders name \n")
        while(1):
            self.lname_of_book = input("enter the name of the book which you want to lend \n")
            if self.lname_of_book in self.list_of_books:
               self.book_dict = {self.lname_of_book:self.lender_name}
               self.lender_dict.update(self.book_dict)
               print("you hane issued book successfully\n")
               print(self.lender_dict)
               print(self.lender_dict.keys())
               self.list_of_books.remove(self.lname_of_book)
               print(f"books for lending { self.list_of_books } \n")

               self.another_book = input("do you want lend another book ? \n ")
               if self.another_book == "yes":
                   self.newbook = input("mention the name of book which you want to lend \n")
                   if self.newbook in self.list_of_books:
                       self.book_dict = {self.lname_of_book and self.newbook:self.lender_name}
                       self.lender_dict.update(self.book_dict)
                       self.list_of_books.remove(self.newbook)
                       print(self.lender_dict)
                       print(self.lender_dict.keys())
                       print("you have issued both the books sucessfully \n")
                   else:
                       print(" no problem")
               break
            else:
                print(f"{self.lname_of_book } book is not available \n"
                      "try again following are the books currently available in library \n")
                print(self.list_of_books)
                continue

    def submit(self):
        """ submit book back to library """
        print(lib_1.submit.__doc__)
        while (1):

           self.return_book = input(f"please enter name of book \n")
           if self.return_book in self.lender_dict.keys():

              del self.lender_dict[self.return_book]
              self.list_of_books.append(self.return_book)
              print("you have submitted the book successfully \n")
              print(self.list_of_books)

              break
           else:
              print(f"their is no book issued with name {self.return_book} \n "
                    f"please try again \n")
              continue

lib_1 = library("lib_1",['ramayan','mahabharat','wings of fire'])

print(lib_1.display_books())
print(lib_1.add_books())
print(lib_1.lend_book())
print(lib_1.submit())