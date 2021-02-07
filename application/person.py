# [Person]:
class Person:
    def __init__(self, _f_name: str, _l_name: str, _address: str, _age: int):
        self.f_name = _f_name
        self.l_name = _l_name
        self.address = _address
        self.age = _age

    # Дава имета на човека
    def get_full_name(self):
        return f'{self.f_name} {self.l_name}'

    # Променя адреса на човека
    def change_address(self, _address):
        self.address = _address

    # Променя възрастта на човека
    def change_age(self, _age):
        self.age = _age
