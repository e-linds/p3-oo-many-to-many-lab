class Author:
    all = []

    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [each for each in Contract.all if each.author == self]
    
    def books(self):
        return [each.book for each in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        newcontract = Contract(self, book, date, royalties)
        return newcontract

    def total_royalties(self):
        royalties_list = []
        for each in self.contracts():
            royalties_list.append(each.royalties)
        return sum(royalties_list)
        
        
    

class Book:
    all = []
    
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [each for each in Contract.all if each.book == self]
    
    def authors(self):
        return [each.author for each in self.contracts()]

   

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    def get_author(self):
        return self._author

    def set_author(self, value):
        if type(value) is Author:
            self._author = value
        else:
            raise Exception("input not valid Author type")
        
    author = property(get_author, set_author)

    def get_book(self):
        return self._book

    def set_book(self, value):
        if type(value) is Book:
            self._book = value
        else:
            raise Exception("input not valid Book type")
        
    book = property(get_book, set_book)

    def get_date(self):
        return self._date

    def set_date(self, value):
        if type(value) is str:
            self._date = value
        else:
            raise Exception("input not valid string")
        
    date = property(get_date, set_date)

    def get_royalties(self):
        return self._royalties

    def set_royalties(self, value):
        if type(value) is int:
            self._royalties = value
        else:
            raise Exception("input not valid integer")
        
    royalties = property(get_royalties, set_royalties)


    @classmethod
    def contracts_by_date(cls, input):
        date_contracts = []
        for each in cls.all:
            if each.date == input:
                date_contracts.append(each)
        return date_contracts
      

  
    


# LH = Author("Laura Hillenbrand")
# LH.book = "Unbroken"

# print(Author.contracts())

   