from tkinter import *
from tkinter import simpledialog, messagebox

class Node:
    def __init__(self,title,author,year,genre) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.next = None

class BookList:
    def __init__(self) -> None:
        self.head = None
    
    def add_book(self,title,author,year,genre):
        new_book = Node(title,author,year,genre)
        if self.head is None:
            self.head = new_book
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_book

class Library:
    def __init__(self,root) -> None:
        self.root = root
        self.root.title("Library application")
        self.book_list = BookList()
        self.root.geometry('350x300')

        self.label = Label(root,text="Library application", font = ('Times new romans',16))
        self.label.pack()

        self.add_button = Button(root,text = "Add button", command=self.add_book)
        self.add_button.pack()


    def add_book(self):
        title = simpledialog.askstring("Input", "Enter book title")
        author = simpledialog.askstring("input", "Enter book's author")
        year = simpledialog.askstring("input", "Enter book's release date")
        genre = simpledialog.askstring("Input", "Enter genre")
        if title and author and year and genre:
            self.book_list.add_book(title,author,year,genre)
            messagebox.showinfo("Success", f'book {title} added.')

if __name__ == "__main__":
    root = Tk()
    app = Library(root)
    root.mainloop()