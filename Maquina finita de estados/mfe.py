
(
ALFABETO,
TRANSITION_FUNCTION,
ESTADO_INICIAL,
ESTADO_FINAL
) = range(4)

def validate_string(alfabeto, string):
    for letra in string:
        if letra not in alfabeto:
            return False
    return True

def processa_string(string, automato):

    if (not validate_string(automato[ALFABETO], string)):
        return None    # caso a string contenha letras nao contidas no alfabeto
        
    # inicializando o estado atual com o estado inicial
    estado_atual = automato[ESTADO_INICIAL]
    # percorrendo a string
    for letra in string:
        # transição para o estado seguinte
        estado_atual = automato[TRANSITION_FUNCTION][estado_atual][letra]
    # retornando o estado final
    return estado_atual in automato[ESTADO_FINAL]

def maquina_finita(arquivo):
    linhas = ""
    #lendo o arquivo
    with open(arquivo, 'r') as f:
        #lendo linha por linha
        for line in f.readlines():
            #adicionando a linha ao texto
            linhas += line
    #separando o texto em palavras
    a = linhas.split('\n')
    #debugando a lista
    print(a)
    #salvando a quantidade de strings
    numero = int(a[0])

    #testando a linguagem nas palavras
    for i in range(numero):
        x = processa_string(a[i+1], automato)
        if x == True:
            print("{}: pertence".format(a[i+1]))
        else:
            print("{}: nao pertence".format(a[i+1]))

if __name__ == '__main__':
    # definindo o automato
    alfabeto = set(['a', 'b', 'c'])
    trans_func = {'q1' : {'a' : 'q2', 'b' : 'q2'},
                  'q2' : {'a' : 'q5', 'b' : 'q3'},
                  'q3' : {'a' : 'q5', 'b' : 'q4'},
                  'q4' : {'a' : 'q2', 'b' : 'q4'},
                  'q5' : {'a' : 'q5', 'b' : 'q5'}
                  }
    estado_inicial = 'q1'
    estado_final = set(['q4'])
    automato = (alfabeto, trans_func, estado_inicial, estado_final)


# teste da maquina finita
arquivo = 'texto.txt'
maquina_finita(arquivo)




                    
