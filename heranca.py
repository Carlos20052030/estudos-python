"""
POO - Herança (Inheritance)

A ideia de Herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra
classe que passa a herdar atributos e métodos da classe herdada.


Cliente
    - nome;
    - sobremenome;
    - cpf;
    - renda;

Funcionário
    - nome;
    - sobremenome;
    - cpf;
    - matrícula;

Perguntar: Existe alguma entidade genérica o suficiente para encapsular os
atributos e métodos comuns e outrans entidades?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Scooby', 'Doo', '004.336.668-75', 2500)
func1 = Funcionario('Norville', 'Rogers', '995.615.754-74', 'D656')


print(cliente1.nome_completo())
print(func1.nome_completo())


OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e
métodods da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:

    [Pessoa]
    - Super Classe:
    - Classe Mãe:
    - Classe Pai:
    - Classe base:
    - Classe Genérica:

Quando uma classe herda de outra classe, ela é chamada:

    [Cliente, Funcionario}
    - Sub Classe:
    - Classe Filha:
    - Classe Específica:


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    -> Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    -> Funcionario herda de pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Scooby', 'Doo', '004.336.668-75', 2500)
func1 = Funcionario('Norville', 'Rogers', '995.615.754-74', 'D656')


print(cliente1.nome_completo())
print(func1.nome_completo())


print(cliente1.__dict__)

print(func1.__dict__)

# Sobrescrita de Métodods (Overriding)

Sobrescrita de de métodos, ocorre quando reescrevemos/reimplementamos um
método presente na super classe em classes filhas.

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    @property
    def nome(self):
        return self.__nome

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário: {self.__matricula} Nome: {self.nome}'


cliente1 = Cliente('Scooby', 'Doo', '004.336.668-75', 2500)
func1 = Funcionario('Norville', 'Rogers', '995.615.754-74', 'D656')


print(cliente1.nome_completo())
print(func1.nome_completo())
