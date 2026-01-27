"""
POO - Metodos

- Metodos (funcoes) -> Representam os comportamentos do objeto, ou seja, as acoes
que este objeto pode realizar no seu sistema.

Em Python, dividimos os metodos, em 2 grupos: 'Metodos de instancia' e 'Metodos
de Classe'.

# Metodos de Instancia

# O metodo dunder init __init__ é um metododo especial chamado de construtor e sua
funcao é construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de
dunder (Double underline)

OBS: Os elementos em Python sao chamados de metodos magicos.

ATENCAO! Por mais que possamos criar nossas proprias funcoes utilizando dunder
(underline no inicio e no fim) não é aconselhado. Python possui vários metoddos
com esta forma de nomenclatura e pode ser que mudemos o comportamento dessas
funcoes magicas internas da linguagem. Entao evite ao maximo. De preferencia nunca
o faca.

# Metodos sao escritos em letra maiusculas. Se o nome for composto, o nome tera as
palavras separadas por underline.


user1 = Usuario('Bruno', 'Marrone', 'brunoemarrone@gmail.com', '112358')
user2 = Usuario('Ivete', 'Sangalo', 'ivetesangalo', '123321')

print(user1.nome_completo())

print(Usuario.nome_completo(user1))

print(user2.nome_completo())

print(f'senha user1: {user1._Usuario__senha}')

print(f'senha user2: {user2._Usuario__senha}')

FRASE-CHAVE (GUARDE ESSA)

Hash protege senhas.
Salt protege contra tabelas.
Rounds protegem contra força bruta.


----------------------------------------------------------------

nome = input('informe o nome: ')
sobrenome = input('informe o sobrenome: ')
email = input('informe o email:')
senha = input('informe a senha: ')
confirme_senha = input('confirme a senha: ')

if senha == confirme_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(42)

print('Usuario criadodo com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checar_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')


print(f'Sennha User Crypitografada: {user._Usuario__senha}')  #Acesso errado

 # Métodos de Classse em Python são conhecidos como Métodods Estáticos em outra linguagem.

 # Metodos de Classe

user = Usuario('Felicity', 'Jones', 'felicityjones@gmail.com', '123456')

Usuario.conta_usuarios() #Forma correta
user.conta_usuarios()    #Possível, mas incorreta

user = Usuario('Felicity', 'Jones', 'felicityjones@gmail.com', '123456')

print(user._Usuario__gera_usuario()) # Acesso de forma ruim


"""

from operator import truediv


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limete, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limete = limete
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero



class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100  #Exemplo: (2300 * 80) / 100 = 1840


p1 = Produto('PlayStation 4', 'Video Game', 2300)

#print(p1.desconto(20))  # #Exemplo: (2300 * 80) / 100 = 1840

#print(Produto.desconto(p1, 40))  #self, desconto



from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')


    @classmethod
    def ver(self):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'


    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]



# Método Estático


print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Felicity', 'Jones', 'felicityjones@gmail.com', '123456')

print(user.contador)

print(user.definicao())

