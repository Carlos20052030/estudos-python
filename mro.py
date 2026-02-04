"""
POO - MRO -> Method Resolution Order


MRO (Method Resolution Order) é a ordem linear que o Python utiliza para decidir
qual método será executado quando existe herança múltipla.

Neste código, utilizamos herança múltipla com mixins e o método super() para criar
uma cadeia cooperativa de execução. Cada classe executa sua própria lógica e, ao
chamar super(), delega a execução para a próxima classe definida no MRO.

O método super() não chama o "pai direto", mas sim o próximo método na fila do MRO,
garantindo que todos os métodos sejam executados uma única vez, na ordem correta.

A classe BaseFinal existe para encerrar explicitamente a cadeia, já que a classe
object não possui o método executar(). Assim, o fluxo de execução percorre todas
as classes de forma previsível e controlada.



class A:
    def falar(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


class A:
    def acao(self):
        print("A")

class B(A):
    def acao(self):
        print('B')
        super().acao()

class C(A):
    def acao(self):
        print('C')
        super().acao()

class D(B, C):
    def acao(self):
        print('B')
        super().acao()
"""


class BaseFinal:
    def executar(self):
        print('Basefinal: fim real')


class Base(BaseFinal):
    def executar(self):
        print('Base: inicio da cadeia')
        super().executar()


class LogMixin:
    def executar(self):
        print('LogMixin: registrando log')
        super().executar()


class AuthMixin:
    def executar(self):
        print('AuthMixin: verificando autenticação')
        super().executar()


class Servico(AuthMixin, LogMixin, Base):
    def executar(self):
        print('Serviço: preparando execução')
        super().executar()


servico = Servico()
servico.executar()


print(Servico.mro())



