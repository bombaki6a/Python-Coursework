# [Book]:
class Book:
    def __init__(self, _name: str, _category: str, _author: str, _rating: float, _price: float):
        self.name = _name
        self.category = _category
        self.author = _author
        self.rating = _rating
        self.price = _price

    # Извежда инфорация за книгата
    def get_info(self):
        print(
            f'Име: {self.name}\n'
            f'Категория: {self.category}\n'
            f'Автор: {self.author}\n'
            f'Рейтинг: {self.rating}/10\n'
            f'Цена: {self.price:.2f}лв'
        )

    # Добавя рейтинг на книгата
    def add_rating(self, _rating: float):
        self.rating += _rating

    # Променя цената на книгата
    def change_price(self, _price: float):
        self.price = _price
