#!/usr/bin/env python3.8

from unicodedata import normalize

def retirar_vazio(lista: list) -> list:
    for chave, valor in enumerate(lista):
        if valor == '' or valor == ' ':
            del(lista[chave])
    return lista


def removendo_traco(frase):
    for letra in frase:
        frase = frase.replace('.', '')
        frase = frase.replace(',', '')
        frase = frase.replace('/', '')
        frase = frase.replace('\\', '')
        frase = frase.replace('_', ' ')
        frase = frase.replace('&', '')
        frase = frase.replace('  ', ' ')
        frase = frase.replace('-', ' ')
        frase = frase.replace('(', '')
        frase = frase.replace(')', '')
    return frase

def removendo_acentos(string: str) -> str:
    nova = normalize('NFD', string)
    return nova.encode('ascii', 'ignore').decode('utf8').casefold()


if __name__ == '__main__':
    frase = input('digite sua frase: ')

    frase = removendo_acentos(frase)
    frase = removendo_traco(frase)
    #formando lista de strings a cada espaço
    lista_palavras = frase.split(' ')
    lista_palavras = retirar_vazio(lista_palavras)
    ultima = '-'.join(lista_palavras)
    print('\n\n')
    print(ultima)
    print('\n\n')
