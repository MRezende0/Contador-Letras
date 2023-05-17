# Atividade de Arquitetura Cloud - Matheus Rezende
## Contador de palavras

Na atividade, foi pedido o seguinte: 

Crie um programa em Python que receba um texto (proveniente de um arquivo TXT) e realize as seguintes atividades:

1. Carregue o arquivo
2. Retire os acentos e exiba o texto reescrito.
3. Realize a contagem das palavras (que deverão ser ranqueadas em forma decrescente).
4. Permita ao usuário saber qual(is) palavra(s) que ele deseja e quantas aparições de cada uma.
5. Exibir a com mais aparição e a com menos aparição.
6. Mostre um menu para as escolhas acima e use o 0 para encerrar a aplicação.

-----

Em primeiro lugar, utilizei as bibliotecas string para utilizar a constante 'string.punctuation', que é uma string pré-definida contendo todos os caracteres de pontuação. Essa constante é utilizada na função 'remover_acentos' para remover a pontuação do texto antes de remover os acentos.
Também foi utilizado a biblioteca 'tkinter' importando o módulo 'filedialog' para abrir uma janela para selecionar um arquivo em um sistema de arquivos.
```
import string
import tkinter as tk
from tkinter import filedialog
```

----

### Atividade 01 - Carregar arquivo

Este trecho de código cria uma janela "invisível" (`root.withdraw()`) usando a biblioteca `tkinter`, permitindo que o usuário selecione um arquivo usando uma caixa de diálogo padrão do sistema operacional (`filedialog.askopenfilename()`). O caminho completo do arquivo selecionado é armazenado na variável `file_path`.
Ao executar o programa, essa sequência de comandos permite que o usuário selecione um arquivo a partir de uma caixa de diálogo padrão do sistema operacional e, em seguida, o conteúdo do arquivo selecionado é carregado e processado.
```
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)
```

----

### Atividade 02 - Retire os acentos e exiba o texto reescrito

A função 'remover_acentos' tem como objetivo remover os acentos e a pontuação de uma string de entrada (txt) e retornar a string resultante.
```
def remover_acentos(txt):
    return ''.join(c for c in txt if c not in string.punctuation).translate(str.maketrans('', '', 'áàãâéêíóôõúüçÁÀÃÂÉÊÍÓÔÕÚÜÇ'))
```

----

### Atividade 03 - Realize a contagem das palavras (que deverão ser ranqueadas em forma decrescente)

A função 'contar_palavras' recebe uma string texto como entrada e retorna um dicionário que contém as palavras no texto e o número de vezes que cada palavra aparece.
A função 'exibir_ranking' recebe o dicionário contagem retornado pela função contar_palavras() e exibe um ranking das palavras em ordem decrescente de frequência.
```
def contar_palavras(texto):
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

def exibir_ranking(contagem):
    ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    for palavra, cont in ranking:
        print(f'{palavra}: {cont}')
```

----

### Atividade 04 - Permita ao usuário saber qual palavra que ele deseja e quantas aparições

A função 'escolher_palavras' recebe uma string texto como entrada. Em seguida, o usuário é solicitado a inserir uma palavra que deseja procurar no texto. Depois disso, exibe o número de ocorrências para cada palavra encontrada no texto.
```
def escolher_palavras(texto):
    palavras = input("Insira a palavra que deseja saber quantas vezes aparece no texto: ")
    palavras = palavras.split(",")
    ocorrencias = {}

    for palavra in palavras:
        ocorrencias[palavra.strip()] = texto.count(palavra.strip())

    for palavra, num_ocorrencias in ocorrencias.items():
        print(f"A palavra '{palavra}' aparece {num_ocorrencias} vezes no texto.")
```

----

### Atividade 06 - Mostre um menu para as escolhas acima e use o 0 para encerrar a aplicação

A função 'exibir_menu' mostra um menu para o usuário escolher qual opção deseja realizar.
```
def exibir_menu():
    print('-----------------------------------------------')
    print('MENU DE OPÇÕES:')
    print('-----------------------------------------------')
    print('1 - Remover acentos e exibir texto sem acentos')
    print('2 - Contar palavras e exibir ranking')
    print('3 - Escolher palavras para contar')
    print('4 - Exibir a palavra com mais aparições')
    print('5 - Exibir a palavra com menos aparições')
    print('0 - Encerrar aplicação')
    print('-----------------------------------------------')
```

----

Essa construção 'if __name__ == '__main__':' verifica se o módulo está sendo executado como um programa autônomo, ou se está sendo importado por outro módulo. Se o módulo estiver sendo executado como um programa autônomo, o bloco de código dentro do if será executado. Caso contrário, o bloco de código dentro do if será ignorado.
Dentro do bloco de código, o arquivo de texto Atividade-Cloud-Texto.txt é aberto em modo de leitura ('r') usando a instrução with open(). Em seguida, o conteúdo do arquivo é lido usando o método read() e armazenado na variável texto. Esse conteúdo será usado nas funções definidas para realizar as operações descritas no enunciado.
```
if __name__ == '__main__':
    with open('Atividade-Cloud-Texto.txt', 'r') as f:
        texto = f.read()
```

----

Essa parte do código está realizando a parte do loop e é responsável por mostrar o menu, até que o usuário deseje sair. O programa pede ao usuário digitar a opção desejada.
```
while True:
    exibir_menu()
    opcao = input('Digite a opção desejada: ')
```

----

Se a variável opcao for igual a string '1', a função 'remover_acentos()' é chamada com o parâmetro texto para remover os acentos do texto e armazenar o resultado na variável 'texto_sem_acentos'.
```
if opcao == '1':
    texto_sem_acentos = remover_acentos(texto)
    print(texto_sem_acentos)
```

----

Se a variável `opcao` for igual a string `'2'`, a função `contar_palavras()` é chamada com o parâmetro `texto` para contar as palavras do texto e armazenar o resultado na variável `contagem`. Em seguida, a função `exibir_ranking()` é chamada com o parâmetro `contagem` para exibir o ranking das palavras na tela, em ordem decrescente de ocorrências.
```
elif opcao == '2':
    contagem = contar_palavras(texto)
    exibir_ranking(contagem)
```

----

Se a variável 'opcao' for igual a string '3', a função 'escolher_palavras()' é chamada com o parâmetro 'texto' para permitir ao usuário inserir uma ou mais palavras e, em seguida, exibir o número de ocorrências dessas palavras no texto.
```
elif opcao == '3':
    escolher_palavras(texto)
```

----

### Atvidade 05 - Exibir a palavra com mais aparição e a palavra com menos aparição

Quando a opção 4 é selecionada, ele calcula a contagem de palavras no texto e classifica as palavras em ordem decrescente de aparição. Em seguida, exibe a palavra com mais aparições e o número de vezes que ela aparece.
Quando a opção 5 é selecionada, ele faz a mesma coisa, mas classifica as palavras em ordem crescente de aparição e exibe a palavra com menos aparições e o número de vezes que ela aparece.
```
    elif opcao == '4':
        contagem = contar_palavras(texto)
        ranking = sorted(contagem.items(),
                        key=lambda x: x[1], reverse=True)
        print(
            f'A palavra com mais aparições é "{ranking[0][0]}" com {ranking[0][1]} aparições.')
            
            
    elif opcao == '5':
        contagem = contar_palavras(texto)
        ranking = sorted(contagem.items(), key=lambda x: x[1])
        print(
            f'A palavra com menos aparições é "{ranking[0][0]}" com {ranking[0][1]} aparições.')
```

----

Essa parte do código é uma cláusula 'elif' que testa se a opção escolhida pelo usuário é igual a '0'. Se essa condição for verdadeira, a execução do loop é interrompida usando o comando 'break', o que finaliza o programa.
```
elif opcao == '0':
    break
```

----

Essa parte do código é responsável por tratar casos em que o usuário insere uma opção inválida no programa. Se o valor digitado pelo usuário não corresponde a nenhuma das opções disponíveis no programa, a mensagem "Opção inválida. Tente novamente." é exibida na tela para alertar o usuário sobre o erro.
```
else:
    print('Opção inválida. Tente novamente.')
```

----

# Obrigado!
