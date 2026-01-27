"""
Forçando tipos de dados com decoradores

#conserto IA
def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)
repete_msg('scooby', '3')

#Professor
def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))   #str('scooby'), int('3')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)

dividir("1", "5")

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(int(vezes)):
        print(msg)
repete_msg('scooby', '3')
"""


