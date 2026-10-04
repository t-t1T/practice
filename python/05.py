class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def show_info(self):
        print(f"{self.title} : {self.author} : {self.category}")


class User:
    def __init__(self, name, interest):
        self.name = name
        self.interest = interest

    def show_info(self):
        print(f"利用者名: {self.name}, 興味分野: {self.interest}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.show_info()

    def recommend(self, user):
        match_found = False
        for book in self.books:
            if book.category == user.interest:
                book.show_info()
                match_found = True
        
        if not match_found:
            print("おすすめの書籍はありません。")


# 実行部分の例
if __name__ == "__main__":
    library = Library()
    
    book1 = Book("AIのしくみ", "AI先生", "AI")
    library.add_book(book1)
    
    user1 = User("米子", "AI")
    
    user1.show_info()
    library.show_books()
    library.recommend(user1)