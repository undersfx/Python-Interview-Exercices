# Descriptor Definition
class Nonblank:
    field_count = 0

    def __init__(self):
        # Gets Nonblank class attrs
        cls = self.__class__ 
        self.storage = f'{cls.__name__}_{cls.field_count}'
        # The incremental counter needs to change de class 'field_count' value, not the instances
        cls.field_count += 1 

    def __set__(self, instance, value):
        # Set Validation
        if not isinstance(value, str):
            raise TypeError(f"'Nonblank' must be a 'str'") # Non-named fields problem !!!
        elif len(value) == 0:
            raise ValueError(f"'Nonblank' must not be empty")
        instance.__dict__[self.storage] = value # Dict insertion in class to avoid infinite calls of __set__

    def __get__(self, instance, owner):
        if instance is None:
            # Direct access to the class attrs couse 'instance' to be None
            # That way we just return the descriptor itself
            return self
        else:
            return getattr(instance, self.storage)

class Person:
    # Descriptors class fields
    name = Nonblank() # Can't see the name of the attr (left side executed first)
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