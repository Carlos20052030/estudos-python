"""


📚 Grimório essencial (pra decorar aos poucos)
Método	O que controla
__init__	nascimento
__str__	fala
__repr__	identidade técnica
__len__	tamanho
__add__	soma
__eq__	igualdade
__getitem__	acesso tipo lista
__call__	objeto como função

class Mago:
    def __init__(self, nome):
        self.nome = nome

m = Mago('Gandalf')

->

class Mago:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'Mago supremo: {self.nome}'

print(Mago('Merlin'))

->

class Grimorio:
    def __init__(self, feiticos):
        self.feiticos = feiticos

    def __len__(self):
        return len(self.feiticos)

g = Grimorio(["fogo", "gelo", "raio"])
print(len(g))

->

class Mana:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        return Mana(self.valor + outro.valor)

m1 = Mana(10)
m2 = Mana(20)

m3 = m1 + m2
print(m3.valor)

class Pergaminho:
    def __init__(self, nome):
        self.nome = nome

    def __eq__(self, outro):
        return self.nome == outro.nome

p1 = Pergaminho('Fogo')
p2 = Pergaminho('Gelo')

print(p1 == p2)

->

class Mago:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f'Mago(nome="{self.nome}")'

m = Mago(nome='Merlin')

print(m)

print(repr(Mago))

->

class Cofre:
    def __init__(self, itens):
        self.itens = itens

    def __getitem__(self, chave):
        return self.itens[chave]


c = Cofre(['Ouro', 'Prata', 'Diamante'])

print(c[0])
print(c[1])

-------

class Grimorio:
    def __init__(self):
        self.feiticos = {
            'Fogo': 10,
            'gelo': 20
        }

    def __getitem__(self, nome):
        return self.feiticos[nome]

g = Grimorio()
print(g['Fogo'])

--------

class Pergaminho:
    def __init__(self, texto):
        self.texto = texto

    def __getitem__(self, chave):
        return self.texto[chave]

p = Pergaminho('Abracadabra')

print(p[0])
print(p[0 : 4])

print(p[::2]) # [início : fim : passo]

--------

class Mapa:
    def __init__(self):
        self.locais = {
            'norte': 'Montanhas',
            'sul': 'Deserto',
            'leste': 'Flosresta',
            'oeste': 'Mar'
        }
    def __getitem__(self, direcao):
        return self.locais[direcao]

m = Mapa()

print(m['norte'])

----------

Aqui:

slice vira instrução

__getitem__ executa a lógica

📌 Significado:
👉 slice como comando, não como dado

class Livro:
    def __init__(self, paginas):
        self.paginas = paginas

    def __getitem__(self, pagina):
        return f'Pagina {pagina}: {self.paginas[pagina]}'

livro = Livro([
    'Era uma vez',
    'Um mago poderoso',
    'Que dominava slices'
])

print(livro[1])



class Estoque:
    def __init__(self):
        self.itens = {
            "pocao": 5,
            "elixir": 2
        }

    def __getitem__(self, item):
        if item not in self.itens:
            return "Item inexistente"
        return f"{item}: {self.itens[item]} unidades"


e = Estoque()
print(e["pocao"])
"""


class Pergaminho:
    def __init__(self, texto):
        self.texto = texto

    def __getitem__(self, chave):
        if isinstance(chave, int):
            return f'Letra -> {self.texto[chave]}'
        elif isinstance(chave, slice):
            return f'Trecho -> "{self.texto[chave]}"'




p = Pergaminho('Abracadabra')

print(p[0])
print(p[1:8:3])

