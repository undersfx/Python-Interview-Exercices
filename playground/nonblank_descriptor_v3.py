# Descriptor Definition
class Nonblank:
    def __set__(self, instance, value):
        # Set Validation
        if not isinstance(value, str):
            raise TypeError(f"{self.storage} must be a 'str'")
        elif len(value) == 0:
            raise ValueError(f"{self.storage} must not be empty")
        instance.__dict__[self.storage] = value # Dict insertion in class to avoid infinite calls of __set__

def named_fields(cls):
    """
    Decorator that change the names of a given class if any instances of Nonblank where find and return it
    """
    for name, attr in cls.__dict__.items():
        if isinstance(attr, Nonblank):
            attr.storage = name
    return cls

# Class decorator rename the fields after the name bindings happens
# Django replace this with a metaclass that the Person needs to inherit
@named_fields
class Person:
    # Descriptors class fields
    name = Nonblank()
    email = Nonblank()

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def full_email(self):
        return f'{self.name} <{self.email}>'


# name and email are instances of Nonblank
print(Person.__dict__, end='\n\n')

thiago = Person('Thiago', 'thiago@rodrigues.com.br')
print(thiago.full_email(), end='\n\n')

# Resolve to ValueError: email must not be empty
# thiago.name = ''

# Resolve to TypeError: name must be a 'str'
# thiago.email = []