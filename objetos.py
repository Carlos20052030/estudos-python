"""
POO - Objetos

Obejetos -> São instâncias de classe. Ou seja, após o mapeamentos do objeto do mundo real para sua
representaçaõ computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar
nos objetos/instâncias de uma classe como varíavel do tipo na classe.

# Instância/Objetos
lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 2000)

user1 = Usuario('Pato', 'Donald', 'patodonald@gmail.com', '123456')

from pandas.io.formats.info import series_see_also_sub

nome = 'Scooby'
sobrenome = 'Doo'
email = 'scooby@gmail.com'
senha = 123456

user = Usuario(nome, sobrenome, email, senha)

print(type('Geek'))

print(type(42))

print(type(user))



class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self._voltagem = voltagem
        self._luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente.__Cliente__nome}')


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


clil = Cliente('Scooby Doo', '123.456.789-99')

cc = ContaCorrente(5000, 10000,  clil)

cc.ContaCorrente__cliente.diz()

"""





