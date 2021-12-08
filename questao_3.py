def verifica_meia_entrada(idade, carteira_estudante):
    meia_entrada = not (21 < idade < 65) or carteira_estudante == 'S'
    return meia_entrada
