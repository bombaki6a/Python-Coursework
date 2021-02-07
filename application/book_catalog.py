from account import Account
from book import Book


# [Catalog]:
class Catalog:
    def __init__(self, _books=None):
        self.book_list = _books

    # Добавяне на книга към католога
    def add_book(self, _book: Book):
        if self.book_check() is True:
            self.book_list.append(_book)
        else:
            self.book_list = [_book]

    # Премахване на книга от каталога
    def remove_book(self, _index: int):
        if self.book_check() is True:
            self.book_list.pop(_index - 1)
            if len(self.book_list) == 0:
                self.book_list = None
        else:
            print('Каталога е празен!')

    # Копуване на книга от каталога
    def buy_book(self, _account: Account, _name_or_n):
        if self.book_check() is True:
            if type(_name_or_n) is int:
                _account.list_books.append(self.book_list[_name_or_n - 1])
                self.remove_book(_name_or_n - 1)
            else:
                _account.list_books.remove(_name_or_n - 1)
                self.remove_book(_name_or_n - 1)
        else:
            print('Каталога е празен!')

    # Извежда имената на всички налични книги в каталога
    def get_all_book(self):
        if self.book_check() is True:
            for index, book in enumerate(self.book_list):
                print(f'№{index + 1}: {book.name}')
        else:
            print('Каталога е празен!')

    # Проверка за налични книги
    def book_check(self):
        return True if self.book_list is not None else False
