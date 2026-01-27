"""
POO - Abstração e Encapsulamento

O grande objetivo de POO é encapsular nesse código dentro de um grupo lógico e hierárquico utilizando classe.

Encapsular -> capsula


                classe
-----------------------------------------
/                                       /
/        atributos de métodods          /
/_______________________________________/

# Relenbrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python nâo bloqueia este
acesso fora da classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteraçâo na forma
de se acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instância._Pessoa__nome

instância._Pessoa__falar()


Abstração, POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de um usuario.


print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)


conta1.numero = 42
conta1.titular = 'Scooby Doo'
conta1.saldo = 9999999999999999999
conta1.limite = 999999999999999999999999999999999999999


print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular)  # NAmae Manglling

conta1._Conta__titular = 'Scooby Doo'

print(conta1.__dict__)

print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(200)

print(conta1.__dict__)

"""



class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor <= 0:
            print('Valor de saque inválido')
        elif self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')

    def transferir(self, valor, conta_destino):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            conta_destino.depositar(valor)
        else:
            print('Transferência não realizada')


# Testando

conta1 = Conta('Scooby Doo', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Norville Rogers', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)


conta1.extrato()
conta2.extrato()

