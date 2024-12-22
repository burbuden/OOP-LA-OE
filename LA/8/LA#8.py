print ("OOP LA#8\nArdent Azrael Sayson\nBSIT-2B\n")
class Book: 
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def bookInfo(self):
        return f"The book is titled {self.title} written by {self.author}."
        
book1 = Book("Beauty and the Beast", "Gabrielle-Suzanne Barbot de Villeneuve")

print(book1.bookInfo())
del book1.author

book2 = Book("I am a hero", "Kengo Hanazawa")
print (book2.bookInfo())

print(book1.bookInfo())