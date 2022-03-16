import json
from statistics import mean
import time

def readData():
    fData = open('data.json')
    data = json.load(fData)
    fData.close()
    return data

data = readData()

apnd = {}

estados = data["estados"].split(" ")
for estado in estados:
    apnd[estado] = {}

simbolos = data["simbolos"].split(" ")
simbPilha = data["simbPilha"].split(" ")
nTransicoes = int(data["nTransicoes"])

for i in range(0,nTransicoes):
    o, cA, cP, d, iP = data["quintuplas"][i].split(" ")
    if cA not in apnd[o]:
        apnd[o][cA] = []
    apnd[o][cA].append([cP, d, iP])

estadoInicial = data["estadoInicial"]
estadosFinais = data["estadosFinais"].split(" ")
palavras = data["palavras"].split(" ")

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
    tempo = []
    for t in range(0, 10000):
        inicio = time.time()
        resultado = testaPalavra(palavra)
        fim = time.time()
        tempo.append((fim - inicio))

    if  resultado:
        print('S')
    else:
        print('N') 
    print(sum(tempo)/len(tempo))
