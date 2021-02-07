from person import Person


# [Account]:
class Account(Person):
    def __init__(
            self,
            _f_name: str,
            _l_name: str,
            _address: str,
            _age: int,
            _user_name: str,
            _password: str,
            _email: str
    ):
        super(Account, self).__init__(_f_name, _l_name, _address, _age)
        self.user_name = _user_name
        self.password = _password
        self.email = _email

        self.list_books = []

    # Извеждане на информация за потребителя
    def get_info(self):
        print(
            f'Потребителско име: {self.user_name}\n'
            f'Имена: {self.get_full_name()}\n'
            f'Години: {self.age}\n'
            f'Емай: {self.email}\n'
            f'Брой книги: {len(self.list_books)}'
        )

    # Изваждане на имената на книгите в списъка на потребителя
    def get_list_of_books(self):
        if len(self.list_books) > 0:
            for index, book in enumerate(self.list_books):
                print(f'#{index + 1}: {book.name}')
        else:
            print('Няма налични книги!\n')

    # Извеждане на информация за определена книга
    def get_book_info(self, _n: int):
        self.list_books[_n - 1].get_info()

    # Промяна на потребителското име на потребителя
    def change_user_name(self, _name: str):
        self.user_name = _name
        print(f'Потребителското име беше сменено!')

    # Промяна на паролата на потребителя
    def change_password(self, _password: str):
        self.password = _password
        print(f'Паролата на [{self.user_name}] беше променена!')

    # Промяна на емайла на потребителя
    def change_email(self, _email: str):
        self.email = _email
        print(f'Емайла на [{self.user_name}] беше сменен!')
