# def potencia_de_pi(expoente):
#    import math
#    return math.pi ** expoente


# pi_ao_quadrado = potencia_de_pi(2)
# pi_mais_um = math.pi + 1

"""
    O módulo 'math' não está definido na variável 'pi_mais_um', 
    pois foi importado dentro da função 'potencia_de_pi'
"""

# A solução seria importar o módulo 'math' antes da função 'potencia_de_pi':

import math

def potencia_de_pi(expoente):
   return math.pi ** expoente


pi_ao_quadrado = potencia_de_pi(2)
pi_mais_um = math.pi + 1
