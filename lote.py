import random
def adicionar():
    num = input(f'Digite a sequencia: [separados por espaço]')
    n = num.split()
    return n

def saber(listanum):
    listsorteados = list()
    sortnum = input('Digite a sequência a ser comparada: [separados por espaço] ')
    sortnumL = sortnum.split()
    if len(listanum) == len(sortnumL):
        for i in range(0, len(listanum)):
            if sortnumL[i] in listanum:
                listsorteados.append(sortnumL[i])
    else:
        print('Desculpe, seu jogo está incorreto!')
        return 'JOGO ERRADO!'
    return listsorteados

def imprimir_jogo(tabnum):
    matriz = [] #lista vazia
    n = 0
    if len(tabnum) >= 15:
        for i in range(5):
            #cria a linha i
            linha = []
            for j in range(3):
                linha.append(tabnum[n])
                n += 1
            matriz.append(linha)
    else:
        tabnum = matriz
    return matriz

def gerador_aleatorio():
    random.seed()
    listAlea = []
    cont = 0
    while cont != 15:
        numAlea = random.randrange(1, 25)
        if numAlea not in listAlea:
            listAlea.append(numAlea)
            cont += 1
    return listAlea


print('------------------- JOGO OFICIAL -------------------')
print('A seguir, digite o jogo oficial que será comparado\ncom os jogos que você fez')
print('----------------------------------------------------')
testA = gerador_aleatorio()


print( 'Teste aleatorio : ', testA)
numeros = adicionar()
while True:
    teste = saber(numeros)
    tabela = imprimir_jogo(numeros)
    #printar tabela
    print(f'Sequência original: ')
    if len(tabela) >= 15:
        for i in range(5):
            for j in range(3):
                print(f'{tabela[i][j]}   ')
            print('\n')
        print('=-='*15)
    else:print(f'   {numeros}   ', end='\n')


    print(f'ACERTOS     : {len(teste)}')
    print(f'Sequencia de acertos : {teste}')
    print('=-='*15)
    cond = str(input('Deseja verificar outro jogo? s / n : '))
    print('---'*15)
    if cond == 'n':
        break