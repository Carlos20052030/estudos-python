"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    def nome_completo(self):
        return f'{self._nome} {self._sobrenome}'


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Marlon', 'Brando', '245.845.659-45', 5000)
func1 = Funcionario('Ana', 'Viera', '523.458.946-52', 'F561')

print(cliente1.nome_completo())
print(func1.nome_completo())
"""



class Pessoa2:

    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f'Olá meu nome é {self.nome}'


# Sobre (Overriding) nas filhas:

# Cliente sobrescrevendo
class Cliente2(Pessoa2):
    def apresentar(self):
        return f"Olá sou o cliente {self.nome}"


# Funcionário sobrescrevendo
class Funcionario2(Pessoa2):
    def apresentar(self):
        return f"Olá sou o funcionário {self.nome}"


pessoa = Pessoa2("Bob Esponja")

cliente = Cliente2("Patrick Estrela")

func = Funcionario2("Lula Molusco")

print(pessoa.apresentar())

print(cliente.apresentar())

print(func.apresentar())



