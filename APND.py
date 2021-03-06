apnd = {}

estados = input().split(" ")
for estado in estados:
    apnd[estado] = {}

simbolos = input().split(" ")
simbPilha = input().split(" ")
nTransicoes = int(input())

for i in range(0,nTransicoes):
    o, cA, cP, d, iP = input().split(" ")
    if cA not in apnd[o]:
        apnd[o][cA] = []
    apnd[o][cA].append([cP, d, iP])

estadoInicial = input()
estadosFinais = input().split(" ")
palavras = input().split(" ")

def testaPalavra(palavra):
    transicao = [(estadoInicial, palavra, [])]
    pValida = False

    while ((not pValida) and (not (len(palavra)==0)) and (not (len(transicao)==0))):
        aux = transicao.pop()
        aux_estado = aux[0]
        aux_palavra = aux[1]
        aux_pilha = aux[2]

        if ((apnd[aux_estado].get('*')) and (aux_palavra != '*')):
            estadoAuxiliar = apnd[aux_estado]['*']
            aux2 = 1
            for estado in estadoAuxiliar: 
                novo_aux_pilha = aux_pilha.copy() 

                if(estado[0] != '*'): 
                    if (len(novo_aux_pilha) == 0):
                        aux2 = 0
                        break
                    else:
                        top = novo_aux_pilha.pop()
                        if top != estado[0]:
                            aux2 = 0
                            
                if((estado[2] != '*') and (aux2 == 1)):
                    for estadoPilha in estado[2]:
                        novo_aux_pilha.append(estadoPilha)
                
                if(aux2 == 1):
                    transicao.append((estado[1], aux_palavra, novo_aux_pilha))

                aux2 = 1

        if (len(aux_palavra) == 0):
            if ((aux_estado in estadosFinais) and (len(aux_pilha) == 0)):
                return not pValida
            else:
                continue

        if(apnd[aux_estado].get(aux_palavra[0])):
            estadoAuxiliar = apnd[aux_estado][aux_palavra[0]] 
            aux2 = 1
            for estado in estadoAuxiliar: 
                novo_aux_pilha = aux_pilha.copy() 
                if(estado[0] != '*'): 
                    if len(novo_aux_pilha) == 0:
                        aux2 = 0
                        break
                    else:
                        top = novo_aux_pilha.pop()
                        if top != estado[0]:
                            aux2 = 0

                if(estado[2] != '*' and aux2 == 1): 
                    for estadoPilha in estado[2]:
                        novo_aux_pilha.append(estadoPilha)
                
                if(aux2 == 1): 
                    transicao.append((estado[1], aux_palavra[1:], novo_aux_pilha))

for palavra in palavras: 
    if  testaPalavra(palavra):
        print('S')
    else:
        print('N')