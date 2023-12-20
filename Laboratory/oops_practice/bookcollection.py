class Book:
    def __init__(self,title,author,price):
        books=[]
        self.title=title
        self.author=author
        self.price=price
    def addbook(self):
        books.append(self)

    def removebook(self):
        if self in books:
            books.remove(self)
class BookClub:
    def __init(self,member):
        self.member=member
        members=[]
    def addmember(self):
        members.append(self)

    def removemember(self):
        if self in members:
            members.remove[self]

    def findbook(self,book):
        for self in members:
            if book in self.book:
                return f'book found: {book}'
            else:
                return f'no book found'
    # def change(self,person1,person2):
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10)
book2 = Book("The Catcher in the Rye", "J. D. Salinger", 8)
book3 = Book('The 4-Hour Workweek', 'Tim Ferriss', 15)
book4 = Book('The Lean Startup', 'Eric Ries', 10)
book5 = Book('The 7 Habits of Highly Effective People', 'Stephen Covey', 5)
book6 = Book('The Business School', 'Robert Kiyosaki', 25)

member1 = BookClub("David", [book2])
member2 = BookClub("Aaron", [book3, book4, book5])
member3 = BookClub("Emily", [book1, book6])

book_club = BookClub("IIITD Book Club", [])
book_club.add_member(member1)
book_club.add_member(member2)
book_club.add_member(member3)
    
