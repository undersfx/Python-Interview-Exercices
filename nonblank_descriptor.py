# Descriptor Definition
class Nonblank:
    def __init__(self, storage):
        self.storage = storage

    def __set__(self, instance, value):
        # Set Validation
        if not isinstance(value, str):
            raise TypeError(f"{self.storage} must be a 'str'")
        elif len(value) == 0:
            raise ValueError(f"{self.storage} must not be empty")
        instance.__dict__[self.storage] = value # Dict insertion in class to avoid infinite calls of __set__

class Person:
    # Descriptors class fields
    name = Nonblank('name') # Duplication Problem !!!
    email = Nonblank('email') # Duplication Problem !!!

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def full_email(self):
        return f'{self.name} <{self.email}>'

print(Person.__dict__, end='\n\n') # name and email are instances of Nonblank

thiago = Person('Thiago', 'thiago@rodrigues.com.br')
print(thiago.full_email(), end='\n\n')


thiago.name = 'Thiago Rodrigues'
# thiago.name = '' resolve to ValueError: email must not be empty
thiago.email = 'thiago@sfx.com.br'
# thiago.email = [] resolve to TypeError: name must be a 'str'
print(thiago.full_email())