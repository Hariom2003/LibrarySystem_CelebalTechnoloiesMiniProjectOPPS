class Library:
    def __init__(self,list,name):
        self.BookList=list
        self.name=name
        self.LendDict={}

    def DisplayBook(self):
        print(f"we have following Book are avlable :{self.name} ")
        for book in self.BookList:
            print(book)

    def LendBook(self,user,book):
        if book not in self.LendDict.keys():
            self.LendDict.update({book:user})
            print("lender Book database Has been Updated. You Can Take Book")
        else:
            print(f"This  Book is already being used by {self.LendDict[book]}")

    def addBook(self,book):
        self.bookList.append(book)
        print("Book has been added to the bookList")
    def returnBook(self,book):
        self.LendDict.pop(book)
if __name__=='__main__':
    HariomLib=Library(["java","python","c","c++","HTML","CSS"],"Welcome To Jiet Library")

    while(True):
        print(f"\t\t{HariomLib.name}   \nPlease Choose The Option which Is Given Blow:- ")
        print("1.Dispaly The Books")
        print("2.Lend a Book")
        print("3.AddBooK into the  BookList")
        print("4.return Book into the  Library")
        user_choice=int(input("Enter the number:"))
        if user_choice==1:
            HariomLib.DisplayBook()
        elif user_choice==2:
            book=input("Enter the name of the book . you want to lend:")
            user=input("Enter your name :")
            HariomLib.LendBook(user,book)
        elif user_choice==3:
            book=input("Enter the name of the Book .you want to add.")

            HariomLib.addBook(book)
        elif user_choice==4:
            book = input("Enter the name of the Book .you want to return.")

            HariomLib.returnBook(book)
        else:
            print("Plese Enter the valid input")
        print("Press q for quit and c for continue")
        User_decision=""
        while(User_decision!="c" and User_decision!="q"):
            User_decision=input()
            if User_decision == "q":
                exit()
            elif User_decision == "c":
                continue
