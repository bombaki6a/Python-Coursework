import os
from book import Book
from account import Account
from book_catalog import Catalog

# Помощни функции
clear = (lambda: os.system('cls' if os.name == 'nt' else 'clear'))
line = (lambda: print('========================================'))

# Добавяне на книги
books = [
    Book('A Children’s Bible', 'fiction', 'Lydia Millet', 4.50, 50.95),
    Book('Deacon King Kong', 'historical', 'James McBride', 6.21, 56.0),
    Book('Hamnet', 'prose', 'Maggie O’Farrell', 3.20, 53.20),
    Book('Homeland Elegies', 'fiction', 'Ayad Akhtar', 7.50, 56.0),
    Book('The Vanishing Half', 'mystery', 'Brit Bennett', 8.30, 54.0),
    Book('Hidden Valley Road', 'biography', 'Robert Kolker', 2.10, 59.10),
    Book('A Promised Land', 'biography', 'Barack Obama', 4.90, 90.0),
    Book('Shakespeare in a Divided America', 'drama', 'James Shapiro', 1.50, 54.0),
    Book('Uncanny Valley', 'biography', 'Anna Wiener', 2.50, 43.0),
    Book('War', 'historical', 'Margaret MacMillan', 6.66, 60.0),
]

# Добавяне на профили
accounts = [
    Account('Николай', 'Минчев', 'Laurel Drive', 23, 'Niki65', 'pass123', 'niki65@gmail.com'),
    Account('Иван', 'Христов', 'Fairway Drive', 19, 'ivan66', 'pass891', 'ivan.biqcha66@gmail.com'),
    Account('Мария', 'Николова', 'Court Street', 20, 'mimi_b', 'min9011', 'mimi.n2000@gmail.com'),
    Account('Красимир', 'Маринов', 'Essex Court', 34, 'krasi99', 'krasras90', 'kras90@gmail.com'),
    Account('Станислава', 'Иванова', 'Orchard Avenue', 21, 'stas19', 'staskat99', 'stas99@gmail.com'),
]

# Създавне на каталог с книги
catalog = Catalog(books)
account: Account


# Меню на каталога
def catalog_menu():
    # Изкарване на опциите на монюто
    clear()
    print(
        '--Меню на каталога--\n'
        '1) [Списък с всички книги]\n'
        '2) [Купи книга]\n'
        '3) [Добави книга]\n'
        '4) [Премахни книга]\n'
        '5) [Назад]\n'
    )

    # Избор на опция
    option = int()
    try:
        option = int(input('> '))
    except ValueError:
        clear()
        print('Изисква се единствено номера на дадена опция!\n')
        input('Натиснете ENTER, за да опитате отново!')
        catalog_menu()

    # Проверка на опциията
    if option == 1:
        clear()
        catalog.get_all_book()
        input('Натиснете ENTER, за да опитате отново!')
        catalog_menu()
    elif option == 2:
        name_or_number = input('Въведи името или номера на книгата: ')
        name_or_number = int(name_or_number) if name_or_number.isnumeric() else name_or_number
        catalog.buy_book(account, name_or_number)
        input('Натиснете ENTER за да се върнете!\n')
        catalog_menu()
    elif option == 3:
        clear()
        name = input('Заглавие: ')
        category = input('Категория: ')
        author = input('Автор: ')
        rating = float(input('Рейтинг: '))
        price = float(input('Цена: '))
        catalog.add_book(Book(name, category, author, rating, price))
        input('Натиснете ENTER за да се върнете!\n')
        catalog_menu()
    elif option == 4:
        catalog.remove_book(int(input('Номера на книгата: ')))
        input('Натиснете ENTER за да се върнете!\n')
        catalog_menu()
    elif option == 5:
        main_menu()
    elif option > 5:
        clear()
        print('Опцията, която се опитвате да достъпите не е налична!\n')
        input('Натиснете ENTER, за да опитате отново!')
        catalog_menu()


# Потребителско име
def user_menu():
    # Изкраване на опциите на менюто
    clear()
    print(
        '--Потребителско меню--\n'
        '1) [Информация за протебителя]\n'
        '2) [Списък с книгите]\n'
        '3) [Информация за книга]\n'
        '4) [Смени потребителското име]\n'
        '5) [Смени потребителската парола]\n'
        '6) [Смени потребителският емай]\n'
        '7) [Назад]\n'
    )

    # Избор на опция
    option = int()
    try:
        option = int(input('> '))
    except ValueError:
        clear()
        print('Изисква се единствено номера на дадена опция!\n')
        input('Натиснете ENTER, за да опитате отново!')
        user_menu()

    # Проверка на опцията
    if option == 1:
        clear()
        account.get_info()
        input('Натиснете ENTER за да се върнете!\n')
        user_menu()
    elif option == 2:
        clear()
        account.get_list_of_books()
        input('Натиснете ENTER за да се върнете!\n')
        user_menu()
    elif option == 3:
        account.get_book_info(int(input('Въведи номера на книгата: ')))
        input('Натиснете ENTER за да се върнете!\n')
        user_menu()
    elif option == 4:
        clear()
        account.change_user_name(input('Ново потребителско име: '))
        input('Натиснете ENTER за да се върнете!\n')
        user_menu()
    elif option == 5:
        clear()
        account.change_password(input('Нова потребитерска парола: '))
        input('Натиснете ENTER за да се върнете!\n')
        user_menu()
    elif option == 6:
        clear()
        account.change_email(input('Нов емай: '))
        input('Натиснете ENTER за да се върнете!\n')
        user_menu()
    elif option == 7:
        main_menu()
    elif option > 7:
        clear()
        print('Опцията, която се опитвате да достъпите не е налична!\n')
        input('Натиснете ENTER, за да опитате отново!')
        user_menu()


# Главно меню
def main_menu():
    # Изкарване на опциите на менюто
    clear()
    print(
        '--Меню--\n'
        '1) [Каталог с книги]\n'
        '2) [Потребител]\n'
        '3) [Изход]\n'
    )

    # Избор на опция
    option = int()
    try:
        option = int(input('> '))
    except ValueError:
        clear()
        print('Изисква се единствено номера на дадена опция!\n')
        input('Натиснете ENTER, за да опитате отново!')
        main_menu()

    # проверка на оцията
    if option == 1:
        catalog_menu()
    elif option == 2:
        user_menu()
    elif option == 3:
        clear()
        print('Успешно излязохте!')
    elif option > 3:
        clear()
        print('Опцията, която се опитвате да достъпите не е налична!\n')
        input('Натиснете ENTER, за да опитате отново!')
        main_menu()


# Модове на програмата:
def mode_v_1():

    # Информация за всички регистрирани потребители
    print('[ВСИЧКИ ПОТРЕБИТЕЛИ]')
    line()
    for n, acc in enumerate(accounts):
        print(f'ПОТРЕБИТЕЛ {n + 1}')
        line()
        acc.get_info()
        line()

    # Извеждане на списака с книги от каталога
    print('\n[КНИГИТЕ В КАТАЛОГА]')
    line()
    catalog.get_all_book()
    line()

    # Потребител [1(0)] си харесва книгите 3 и 6 и ги копува
    catalog.buy_book(accounts[0], 3)
    catalog.buy_book(accounts[0], 6)

    # Извеждане на информация за акаунта след покупката
    print('\n[ПОТРЕБИТЕЛ 1]')
    line()
    accounts[0].get_info()
    line()

    # Извеждане на списъка с книги след покупката на 1-я потребител
    print('\n[КНИГИТЕ В КАТАЛОГА]')
    line()
    catalog.get_all_book()
    line()

    # Потебител [5(4)] си харесва книгите 8 5 2 и 1
    catalog.buy_book(accounts[4], 8)
    catalog.buy_book(accounts[4], 5)
    catalog.buy_book(accounts[4], 2)
    catalog.buy_book(accounts[4], 1)

    # Извеждане на информация за акаунта след покупката
    print('\n[ПОТРЕБИТЕЛ 5]')
    line()
    accounts[4].get_info()
    line()

    # Извеждане на списъка с книги след покупката на 5-я потребител
    print('\n[КНИГИТЕ В КАТАЛОГА]')
    line()
    catalog.get_all_book()
    line()


def mode_v_2():
    global account

    # Създаване на профил
    print('--Създай си акаунт--')

    name = input('Име: ')
    f_name = input('Файмилия: ')
    address = input('Адрес: ')
    age = int(input('Възраст: '))
    nickname = input('Потребителско име: ')
    password = input('Парола: ')
    email = input('Емайл: ')

    account = Account(name, f_name, address, age, nickname, password, email)
    main_menu()


# От тука се избира кой мод да ползва програмата
if __name__ == '__main__':
    # Този режим работи с списък от потребители
    # mode_v_1()

    # Този режим работи с потребител, който се създава при пускане на програмата
    # !!! Работи само в конзолата !!!
    mode_v_2()
