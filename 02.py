'''
2) Escreva um programa que verifique, em uma string, a existência da letra 'a', 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
'''


def verificar_letra_a(texto):
    texto_padrao = texto.lower()
    contador_a = texto_padrao.count('a')
    return contador_a
    

texto = input('Digite uma string: ')

contador_a = verificar_letra_a(texto)

if contador_a > 0:
    print(f"A letra 'a' aparece {contador_a} vezez na string '{texto}'.")
else:
    print("A letra 'a' não foi encontrada na string.")
