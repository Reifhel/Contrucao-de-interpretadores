import re

# --------------------- Gramatica ---------------------
constantes = ["T", "F"]
operadorUnario = "\lneg"
operadoresBinario = ["\lor", "\land", "\Rightarrow", "\Leftrightarrow"]
abreParen = "("
fechaParen = ")"

# --------------------- Verificação de fórmulas ---------------------
# Verifica se a fórmula é válida
def Formula(indiceAtual, status):

    # indice igual a parenteses inicial
    if expressao[indiceAtual] == abreParen:
        status = AbreParen(indiceAtual)

    # indice igual a parenteses final
    elif expressao[indiceAtual] == fechaParen:
        status = FechaParen(indiceAtual)

    # indice igual a operador de negação
    elif expressao[indiceAtual] == operadorUnario:
        status = FormulaUnaria(indiceAtual)

    # indice igual a um operador binario
    elif expressao[indiceAtual] in operadoresBinario:
        status = FormulaBinaria(indiceAtual)

    # indice diferente de constante
    elif expressao[indiceAtual] not in constantes:
        status = Proposicao(indiceAtual)


    # verificando cada caracter da fórmula
    if status and (indiceAtual != indiceFinal):
        status = Formula(indiceAtual + 1, status)

    return status

# verificando as preposições
def Proposicao(indiceAtual):
    result = re.search("[a-z]|[a-z]+[0-9]", expressao[indiceAtual])

    # caso o valor nao bata cm o regex, retorna falso
    if not result:
        return False

    return True

# função para verificar quando um parenteses abre
def AbreParen(indiceAtual):
    global contaParen
    contaParen = contaParen + 1

    if ((indiceAtual > indiceFinal - 1) or (expressao[indiceAtual + 1] == operadorUnario) or
        (expressao[indiceAtual + 1] in operadoresBinario) or (expressao[indiceAtual + 1] == fechaParen) ):
        return False

    return True

# verficação de fechaa parenteses
def FechaParen(indiceAtual):
    global contaParen
    contaParen = contaParen - 1

    if (contaParen < 0):
        return False

    return True

# formula unaria
def FormulaUnaria(indiceAtual):
    # caso indice atual seja o ultimo OU o proximo caracter seja um parenteses final OU um operador binario, retorna falso
    if ((indiceAtual == indiceFinal) or (expressao[indiceAtual + 1] == fechaParen) or 
                (expressao[indiceAtual + 1] in operadoresBinario)):
        return False

     # caso seja uma constante ou preposição (casos restantes), retorna true
    return True


def FormulaBinaria(indiceAtual):
    # caso indice atual seja o ultimo OU o proximo caracter seja um parenteses final OU um operador binario, retorna falso
    if ( (indiceAtual == indiceFinal) or (expressao[indiceAtual + 1] == fechaParen) or
            (expressao[indiceAtual + 1] in operadoresBinario)
    ):
        return False

    # caso indice atual seja o primeiro OU o penultimo caracter seja um parenteses inicial OU um operador unario
    # OU um operador binario, retorna falso
    if (
            (indiceAtual == 0) or (expressao[indiceAtual - 1] == abreParen) or (expressao[indiceAtual - 1] == operadorUnario) or
                                        (expressao[indiceAtual - 1] in operadoresBinario)
    ):
        return False

    # caso seja uma constante ou preposição (casos restantes), retorna true
    return True

# --------------------- Análise de fórmulas ---------------------
def main():
    # variaveis globais
    global expressao
    global indiceFinal
    global contaParen

    while True:
        # entrada de dados
        print('\n-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-')
        arq = input('Digite o nome do arquivo, e seu diretorio caso necessário (Ex: arquivos/1.txt): ')

        try:
            arquivo = open(arq, 'r')
            break
        except:
            print('Arquivo inválido, tente novamente!')
            continue


    # printando dados do arquivo
    print('-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-')
    print('Arquivo lido: ' + arq)

    quantidade = arquivo.readline()
    print('Formulas a serem lidas: ' + quantidade)

     # lendo cada linha do arquivo segundo a quantidade dada pela linha 1
    for i in range(int(quantidade)):
        # pegando a primeira linha do arquivo e armazenando em uma variavel
        expressao = arquivo.readline().rstrip('\n').replace('neg', 'lneg').split()
        # pegando a quantidade de caracteres da primeira linha
        indiceFinal = len(expressao) - 1
        # contador de parenteses
        contaParen = 0
        # verifica se a fórmula é válida
        status = Formula(0, True)
        # apos verificar a formula, imprime a fórmula + validade
        if status and contaParen == 0:
            print(" ".join(expressao) + ' ==> Válido')
        else:
            print(" ".join(expressao) + ' ==> Inválido')




    arquivo.close()

# --------------------- Execução ---------------------
main()