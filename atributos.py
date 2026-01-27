"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos
representar computacionalmente os estados de um objeto.


Em Python, dividimos os atributos em 3 grupos:
    -Atributos de Instância;
    -Atributos de classes;
    -Atributos Dinâmicos

#Atributos de instância: Sâo atributos declarados dentro do método construtor.

#OBS:Método construtor: É um método especial utilizado para a construção do objeto.

#Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor;
    }
}

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é public.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da prápria classe onde está declarado,
utiliza-se __duplo underscore no inicio de seu nome.

Isso é conhecido também como Name Mangling.

#OBS: Lembre-se que iso é apenas uma convencao, ou seja, a linguagem Python não
#vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

#Exemplo:
user = Acesso("user@gmail.com", "11235")
print(user.email)

#print(user.__senha) #AtributeError

print(user._Acesso__senha) # Temos acesso. Mas não deveríamos fazer esse acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()

# O que significa atributos de instancia?

# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instancias
# Terao estes atributos.

user1 = Acesso("user1@gmail.com", "123456")
user2 = Acesso("useer2@gmail.com", "654321")

user1.mostra_email()
user2.mostra_email()

# Atributos de Classes

# Atributos de classe, são atributos, claros, que sao declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da clsse. Ou seja, ao invés de cada instancia de class ter seus proprios
# valores como é o caso dos atributos de instancia, com os atributos de classe todas as instancias

p1 = Produto('Playstation', 'Video game', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

print(p1.valor)    # Acesso possivel, mas incorreto de um atributo de clssse.
print(p2.valor)    # Acesso possivel, mas incorreto de um atributo de clssse.

#OBS: Nao precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como Java, os atributos conhecidos como atributos de classe aqui em Python
#sao chamados de atributos estáticos;

class Lampadas:

    def __int__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrent:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Publicos e Atributos Privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Retornara a classe Produto

class Produto:
    # Atriibuto de classe'
    imposto = 1.05 #0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributos Dinamicos -> Um atributo de instancia que pode ser criado em tempo de execuçao.

# OBS: O atributo dinamico sera exclusivo da instancia que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Marcenaria', 5.99)

# Criando um atributo deinamico em  tempo de execução

p2.peso = '5kg' # Note que na classe Produto nao existe o atributo peso

print(f'Produto: {p2.nome}, Descricao: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

#print(f'Produto: {p1.nome}, Descricao: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')  #AttributeError: 'Produto' object has no attribute 'peso'

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)

"""

