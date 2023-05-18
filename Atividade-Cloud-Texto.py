import string
import tkinter as tk
from tkinter import filedialog
from unidecode import unidecode

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)


def remover_acentos(txt):
    return ''.join(c for c in txt if c not in string.punctuation).translate(str.maketrans('', '', 'áàãâéêíóôõúüçÁÀÃÂÉÊÍÓÔÕÚÜÇ'))


def obtendo_letras(texto):
    texto = unidecode(texto)
    texto = texto.upper().split()
    palavras = []
    for i in texto:
        i = i.translate(str.maketrans('', '', string.punctuation))
        palavras.append(i)
    letras = []
    for i in palavras:
        for l in i:
            letras.append(l)
    return letras

def contar_letras(texto):
    texto = unidecode(texto)
    texto = texto.upper().split()

    palavras = []
    for i in texto:
        i = i.translate(str.maketrans('', '', string.punctuation))
        palavras.append(i)

    letras = []
    for i in palavras:
        for l in i:
            letras.append(l)
    return letras

def exibir_ranking(cont):
    ranking = sorted(cont.items(), key=lambda x: x[1], reverse=True)
    for l, cont in ranking:
        print(f'{l}: {cont}')


def escolher_letras(texto):
    letras = input("Insira a letra que deseja saber quantas vezes aparece no texto: ")
    letras = letras.split(",")
    ocorrencias = {}

    for letra in letras:
        ocorrencias[letra.strip()] = texto.count(letra.strip())

    for letra, num_ocorrencias in ocorrencias.items():
        print(f"A letra '{letra}' aparece {num_ocorrencias} vezes no texto.")


def exibir_menu():
    print('-----------------------------------------------')
    print('MENU DE OPÇÕES:')
    print('-----------------------------------------------')
    print('1 - Remover acentos e exibir texto sem acentos')
    print('2 - Contar letras e exibir ranking')
    print('3 - Escolher letra para contar')
    print('4 - Exibir a letra com mais aparições')
    print('5 - Exibir a letra com menos aparições')
    print('0 - Encerrar aplicação')
    print('-----------------------------------------------')



if __name__ == '__main__':
    with open('Atividade-Cloud-Texto.txt', 'r') as f:
        texto = f.read()

    while True:
        exibir_menu()
        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            texto_sem_acentos = remover_acentos(texto)
            print(texto_sem_acentos)

        elif opcao == '2':
            cont = contar_letras(texto)
            exibir_ranking(cont)

        elif opcao == '3':
            escolher_letras(texto)

        elif opcao == '4':
            cont = contar_letras(texto)
            ranking = sorted(cont.items(),
                             key=lambda x: x[1], reverse=True)
            print(
                f'A letra com mais aparições é "{ranking[0][0]}" com {ranking[0][1]} aparições.')
            
        elif opcao == '5':
            cont = contar_letras(texto)
            ranking = sorted(cont.items(), key=lambda x: x[1])
            print(
                f'A letra com menos aparições é "{ranking[0][0]}" com {ranking[0][1]} aparições.')

        elif opcao == '0':
            break

        else:
            print('Opção inválida. Tente novamente.')