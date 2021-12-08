import math

def raiz_quadrada_mais_quadrado(x):
    f_imagem = math.sqrt(x) + math.pow(x, 2)

    print(f'f({x}) = {f_imagem}')
