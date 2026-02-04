"""
POO - O método super()

super() é utilizado para chamar métodos das classes pai de forma cooperativa,
respeitando a hierarquia de herança e a ordem de resolução de métodos (MRO).
Isso garante que todas as classes envolvidas na herança sejam corretamente
inicializadas, especialmente em cenários de herança múltipla.

Neste código, super() permite que Animal e Mamifero participem da construção
do objeto Gato, cada um inicializando seus próprios atributos. O uso de
**kwargs garante que os parâmetros sejam encaminhados corretamente entre
as classes, mantendo o código desacoplado, reutilizável e seguro para
extensões futuras.


class Animal:
    def __init__(self, nome, **kwargs):
        super().__init__(**kwargs)
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class Mamifero:
    def __init__(self, gestacao, **kwargs):
        super().__init__(**kwargs)
        self.__gestacao = gestacao

    @property
    def gestacao(self):
        return self.__gestacao

class Gato(Animal, Mamifero):
    def __init__(self, nome, gestacao, raca):
        super().__init__(nome=nome, gestacao=gestacao)
        self.__raca = raca

    @property
    def raca(self):
        return self.__raca


    def __str__(self):
        return(
            f'{self.__class__.__name__}('
            f'nome={self.nome},'
            f'gestacao={self.gestacao},'
            f'raca={self.raca})'
        )

"""


class Animal:
    def __init__(self, nome, **kwargs):
        super().__init__(**kwargs)
        self.__nome = nome
        self.__nomes_anteriores = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError('Nome não pode ser vazio')
        self.__nomes_anteriores.append(self.__nome)
        self.__nome = novo_nome

    @property
    def nomes_anteriores(self):
        return tuple(self.__nomes_anteriores)

class Mamifero:
    def __init__(self, gestacao, **kwargs):
        super().__init__(**kwargs)
        self.__gestacao = gestacao

    @property
    def gestacao(self):
        return self.__gestacao

class Gato(Animal, Mamifero):
    def __init__(self, nome, gestacao, raca):
        super().__init__(nome=nome, gestacao=gestacao)
        self.__raca = raca

    @property
    def raca(self):
        return self.__raca

    def __str__(self):
        return(
            f'{self.__class__.__name__}('
            f'nome={self.nome},'
            f'gestacao={self.gestacao},'
            f'raca={self.raca})'
        )

espec = Gato('Mingau', 65, 'Persa')

print(espec)

print(espec.nome)
print(espec.gestacao)
print(espec.raca)

espec.nome = 'Ronaldo'
print(espec.nome)

espec.nome = 'Garfield'
print(espec.nome)

print(espec.nomes_anteriores)


