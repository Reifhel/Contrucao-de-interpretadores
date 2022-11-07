from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

urls = ["https://en.wikipedia.org/wiki/Natural_language_processing", 
        "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP",  
        "https://www.ibm.com/cloud/learn/natural-language-processing",
        "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/", 
        "https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html"]

# função para pegar apenas os textos das paginas
def getWebSentence(url):
    html = requests.get(url).content
    bfsoup = BeautifulSoup(html, features="html.parser")

    # retirando todo o javascript e css da pagina para deixar só o texto
    for script in bfsoup(["script", "style"]):
        script.extract()    

    # pegando o texto da pagina
    texto = bfsoup.get_text()

    # quebrando o texto em linhas
    linhas = (line.strip() for line in texto.splitlines())
    # quebrando cada linha em sentenças
    sentenças = (frase.strip() for line in linhas for frase in line.split("  "))
    # removendo espacos em branco
    text = "".join(trecho for trecho in sentenças if trecho)
    buffer = []

    # regex para separar as sentenças
    for token in re.split("[.,?!;:()\"]", text):
        if token != "":
            buffer.append(token)

    return buffer

# função que transforma o texto em um vocabulário
def transforma_em_vocabulario(arrayTexto):
    vocabulario = set()

    # para cada lista de texto
    for lista in arrayTexto:
        # para cada sentença
        for sentenca in lista:
            # para cada palavra
            for palavra in sentenca.split():
                # adiciona a palavra no vocabulario
                vocabulario.add(palavra)

    # retorna o vocabulario ordenado por ordem alfabetica pois o set 
    # não é ordenado e sempre da um resultado diferente
    return sorted(vocabulario)

# função que cria a matriz de frequencia
def matriz_frequencia(arrayTexto):
    vocabulario = transforma_em_vocabulario(arrayTexto)
    bagOfWords = []

    # para cada lista de texto
    for lista in arrayTexto:
        # para cada sentença
        for sentenca in lista:
            # cria um vetor de zeros
            vetor = [0] * len(vocabulario)
            # para cada palavra
            for palavra in sentenca.split():
                # incrementa a contagem da palavra no vetor
                vetor[vocabulario.index(palavra)] += 1
            # adiciona o vetor na bag of words
            bagOfWords.append(vetor)

    return bagOfWords

texto = []

for url in urls:
    texto.append(getWebSentence(url))

print(texto)

vocabulario = transforma_em_vocabulario(texto)
print(vocabulario)

# cria uma matriz para cada documento mostrando a frequencia de cada palavra
matriz = matriz_frequencia(texto)

# imprime a matriz
for linha in matriz:
    print(linha)



