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
        print(testando_linguagem(a[i+1]))

def testando_linguagem(palavra):
    #alfabeto da linguagem
    alfabeto = ['a','b','c']
    #separando a palavra em letras
    palavra_cortada = list(palavra)

    try:
        #testando se a palavra é válida
        for i in range(len(palavra_cortada)):
            #testando se a letra está no alfabeto
            if palavra_cortada[i] not in alfabeto:
                #se não estiver, a palavra não é válida e isso é retornado
                return palavra + ": nao pertence"
            #caso a letra seja a é veroficado caso as proximas letras são 'b'
            elif palavra_cortada[i] == 'a':
                if palavra_cortada[i+1] == 'b' and palavra_cortada[i+2] == 'b':
                    #caso seja, nada ocorre
                    pass
                # se não for, a palavra não é válida e isso é retornado
                else:
                    return palavra + ": nao pertence"
        # caso a palavra passe por toda a validação sem erro, a palavra é válida e isso é retornado
        return palavra + ": pertence"
    #caso ocorra erro de index
    except IndexError:
        return palavra + ": nao pertence" 

# teste da maquina finita
arquivo = 'texto.txt'
maquina_finita(arquivo)




                    
