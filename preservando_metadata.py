"""
Preservando meta wraps
Metadados -> são dados intrísecos em arquivos.
wraps -> São funcôes que envolvem elementos com diversas finalizados

modo de programação da Ia
import functools
import logging

# Configuração básica de logging (profissional em vez de print)
logging.basicConfig(level=logging.INFO, format="%(message)s")

def ver_log(func):
       Decorador para registrar chamadas de função e sua documentação.
    @functools.wraps(func)  # preserva metadados da função original
    def wrapper(*args, **kwargs):
        logging.info(f"Chamando função: {func.__name__}")
        logging.info(f"Docstring: {func.__doc__}")
        return func(*args, **kwargs)
    return wrapper


@ver_log
def soma(a: int, b: int) -> int:
      Soma dois números inteiros.
    return a + b


if __name__ == "__main__":
    resultado = soma(3, 4)
    print("Resultado:", resultado)

código do professor:

#Problema
def ver_log (funcao):
    def logar(*args, **kwargs):
        EU sou uma função dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação:{funcao.__doc__}')
        return funcao (*args, **kwargs)
    return logar


@ver_log
def soma (a,b):
    Soma dois numeros.
    return a+b


#print(soma(10,30))

print(soma.__name__)
print(soma.__doc__)

modo certo do professor:
Resolução do Problema
from functools import wraps

def ver_log (funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        EU sou uma função dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação:{funcao.__doc__}')
        return funcao (*args, **kwargs)
    return logar


@ver_log
def soma (a,b):
        soma dois numeros.
    return a+b


#print(soma(10,30))

print(soma.__name__)
print(soma.__doc__)

print(help(soma))

"""
