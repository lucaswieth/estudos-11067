import math
import funcoes

def funcao(x, y):
    f_imagem = 0

    if x > 0 and x % 2 == 0:
        f_imagem = math.log2(x)

    else:
        f_imagem = funcoes.magia(y)

    return f_imagem
