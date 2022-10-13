from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

urls = ["https://en.wikipedia.org/wiki/Natural_language_processing", 
        "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP",  
        "https://www.ibm.com/cloud/learn/natural-language-processing",
        "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/", 
        "https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html"]

listasTexto = []
for url in urls:
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
    for token in re.split("[.,?!]", text):
        if token != "":
            buffer.append(token)
    listasTexto.append(buffer)

    print("---------------------------------------------------------------------------------------------------------------------")
    # verificando o tamanho de cada site
    print(str(len(buffer)) + " sentenças no site -- " + url + "\n")
    # printando o texto de cada site
    print(str(buffer) + "\n")
    print("---------------------------------------------------------------------------------------------------------------------")