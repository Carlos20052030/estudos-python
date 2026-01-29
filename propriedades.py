"""
POO - Propriedades - Properties


“self.__numero guarda o número exclusivo da conta no momento em que ela foi criada.”
"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return (
            f'Cliente {self.__titular},'
            f'Conta n° {self.__numero},'
            f'Saldo: {self.__saldo}.'
        )

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        if novo_limite < 0:
            raise ValueError("Limite não pode ser negativo")
        self.__limite = novo_limite

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.depositar(valor)


conta1 = Conta('Scooby', 2000, 5000)
conta2 = Conta('Norville', 3000, 6000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo

print(f'Soma dos saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 76515

conta1.depositar(500)
print(conta1.__dict__)
