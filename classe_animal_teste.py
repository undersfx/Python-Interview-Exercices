class Animal: # Animal é um arquetipo para as classes abaixo herdarem
    _sound = None # _ por convenção diz que o atributo é privado.

    def __init__(self, name): # Nome e Fazer algum som é comum a todos, podem herdar sem alterações.
        self.name = name

    def make_sound(self):
        return self._sound

class Cat(Animal): # Gato herda tudo de Animal e também tem seu próprio atributo sound = 'meow'
    def __init__(self, name):
        super().__init__(name)

    _sound = "meow"

class Duck(Animal): # Gato herda tudo de Animal e também tem seu próprio atributo sound = 'quack'
    def __init__(self, name):
        super().__init__(name)

    _sound = "quack"

a = Animal('humano')
print('O {} faz {}'.format(a.name, a.make_sound()))

c = Cat('gato')
print('O {} faz {}'.format(c.name, c.make_sound()))

d = Duck('pato')
print('O {} faz {}'.format(d.name, d.make_sound()))
