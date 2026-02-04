"""
POO - Polimorfismos

Poli -> Muitas
Morfismo -> Formas



Polimorfismo é um dos pilares da Programação Orientada a Objetos e representa a ideia
de “muitas formas”: objetos diferentes podem responder ao mesmo método, cada um com
seu próprio comportamento. Em Python, isso não depende necessariamente de herança;
basta que os objetos possuam o mesmo método, conceito conhecido como duck typing.


abc            → módulo
ABC            → classe
abstractmethod → função (decorador)


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def falar(self):
        pass

    def comer(self):
        print(f'{self.nome} está comendo...')


class Cachorro(Animal):
    def falar(self):
        return f'{self.nome} fala Au Au'


class Gato(Animal):
    def falar(self):
        return f'{self.nome} fala Miau Miau'


class Rato(Animal):
    def falar(self):
        return f'{self.nome} fala Squeak'


Neste código, as classes Carro, Pessoa e Robo implementam o método mover(), cada uma
com uma lógica própria. Ao iterar sobre a lista de objetos e chamar obj.mover(), o
Python executa automaticamente a implementação correta de acordo com o objeto em
questão, sem uso de condicionais. Isso demonstra o polimorfismo em ação: o mesmo
método, chamado da mesma forma, resultando em comportamentos diferentes definidos
pelo próprio objeto.

class Carro:
    def mover(self):
        return 'Carro andando'

class Pessoa:
    def mover(self):
        return 'Pessoa andando'

class Robo:
    def mover(self):
        return 'Robô se locomovendo'


objetos = [Carro(), Pessoa(), Robo()]

for obj in objetos:
    print(obj.mover())


class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return 'Au Au'

class Gato(Animal):
    def falar(self):
        return 'Miau Miau'


animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())

#sem herança
for animal in animais:
    if isinstance(animal, Cachorro):
        print(animal.falar())
    elif isinstance(animal, Gato):
        print(animal.falar())


class Carro:
    def mover(self):
        return 'Carro andando'

class Pessoa:
    def mover(self):
        return 'Pessoa andando'

def fazer_mover(objeto):
    print(objeto.mover())

fazer_mover(Carro())
fazer_mover(Pessoa())


--------------------------
class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Au Au')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Miau Miau')

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

------------------------------


🦆 Metáfora clássica (duck typing)
hasattr

“Se anda como pato e faz quack, eu trato como pato.”

Não importa o que ele é, importa o que ele faz.

isinstance

“Só quem tem carteira de motorista pode dirigir.”

Importa quem você é, não só o que você consegue fazer.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f'{self.nome} está comendo...')

class AnimalFalante(Animal):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(AnimalFalante):
    def falar(self):
        return f'{self.nome} fala Au Au'


class Gato(AnimalFalante):
    def falar(self):
        return f'{self.nome} fala Miau Miau'


class Rato(Animal):
    pass


animais = [
    Cachorro('Rex'),
    Gato('Felix'),
    Rato('Mickey')
]

for animal in animais:
    if isinstance (animal, AnimalFalante):
        print(animal.falar())
    animal.comer()
