"""
POO - Herança Mútipla

Herança Múltipla nada mais é do que a possibilidade de umma classe herdar de mútiplas
classes, fazendo com que a classe filha herde todos os atributos e métodos de todas
as classes herdadas.

OBS: A herança mútipla pode ser feita de duas maneiras:
    - Por Multiderivação direta:
    - Por Multiderivação indireta:

class Animal:
    def comer(self):
        print('O animal está comendo')

class Mamifero:
    def amamentar(self):
        print('O mamífero está amamentando')

class Cachorro(Animal, Mamifero):
    def latir(self):
        print('O cachorro está latindo')


🔍 O que aconteceu?

A classe Cachorro herdou:

comer() → de Animal
amamentar() → de Mamifero
e ainda tem seu próprio método latir()


2️⃣ Multiderivação Indireta

Aqui a herança acontece em cadeia.
Uma classe herda de outra que já herdou de outra.

📐 Estrutura mental
ClasseA
   ↓
ClasseB
   ↓
ClasseC


class SerVivo:
    def respirar(self):
        print('Respirando')

class Animal(SerVivo):
    def mover(self):
        print('Mover')

class Cachorro(Animal):
    def latir(self):
        print('Latindo')
🔍 O que Cachorro herda?
respirar() → de SerVivo
mover() → de Animal
latir() → próprio

📌 Mesmo sem herdar diretamente, a classe recebe tudo que veio antes na árvore.

🧠 Metáfora rápida (pra fixar)

Multiderivação direta →
Você aprende Português com um professor e Matemática com outro, ao mesmo tempo.

Multiderivação indireta →
Seu professor aprendeu com outro professor, que aprendeu com outro…
O conhecimento chega até você por herança.

"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Olá meu nome é {self.nome}, e tenho {self.idade} anos.'


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10


class LiderancaMixin:
    def liderar(self):
        return f'{self.nome} está liderando a equipe.'


class TecnicoMixin:
    def programar(self):
        return f'{self.nome} está escrevendo código.'


class Gerente(Funcionario, LiderancaMixin):
    def __init__(self, nome, idade, salario, setor):
        super().__init__(nome, idade, salario)
        self.__setor = setor

    def calcular_bonus(self):
        bonus_base = super().calcular_bonus()
        bonus_gerente = self.salario * 0.20
        return bonus_base + bonus_gerente


class Desenvolvedor(Funcionario, TecnicoMixin):
    def __init__(self, nome, idade, salario, linguagem):
        super().__init__(nome, idade, salario)
        self.__linguagem = linguagem

gerente = Gerente('Scooby', 30, 8000, 'TI')
dev = Desenvolvedor('Norville', 25, 6000, 'Python')

print(gerente.apresentar())
print(gerente.liderar())
print('Bônus do gerente:', gerente.calcular_bonus())

print('-'*30)

print(dev.apresentar())
print(dev.programar())
print('Bônus do dev:', dev.calcular_bonus())



