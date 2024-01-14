# -*- coding: utf-8 -*-

#Apresentação e descrição
print ("ARQUIVOS / FILES")

#Funcao OPEN
print ("Função OPEN: Responsável por abrir um arquivo de acordo com o modo setado, com a seguinte sintaxe:")
print ("variavel = open(nome, modo)\n\n*Obs.: Caso você imprima apenas o arquivo da seguinte forma:\narquivo = open(\"arquivo.txt\")\n\n*Neste caso será impresso apenas as informações de nome e encoding do arquivo, para realizar a leitura, será necessário utilizar um dos modos de leitura que serão descritos abaixo.\n")
print ("MODOS RESPECTIVAS FUNCOES:")
modo1 = "r"
modo11 = "somente leitura"
modo2 = "w"
modo21 = "escrita (caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)"
modo3 = "a"
modo31 = "leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)"
modo4 = "r+"
modo41= "leitura e escrita"
modo5 = "w+"
modo51 = "escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)"
modo6 = "a+"
modo61 = "leitura e escrita (abre o arquivo para atualização)"
def criarTabela():
    print ("________________________________")
    print ("Modo\t|\tFuncao")
    print ("--------------------------------")
    print ("%s\t|\t%s" % (modo1, modo11))
    print ("%s\t|\t%s" % (modo2, modo21))
    print ("%s\t|\t%s" % (modo3, modo31))
    print ("%s\t|\t%s" % (modo4, modo41))
    print ("%s\t|\t%s" % (modo5, modo51))
    print ("%s\t|\t%s" % (modo6, modo61))
    print ("________________________________")
criarTabela()
print ("\n---x---\n")

#LENDO ARQUIVOS
print ("\nLENDO ARQUIVOS")
print("read(): Lê arquivo inteiro\nreadline(): Lê uma linha\nreadlines(): Lê arquivo e armazena em uma lista.\n")
print ("Exemplo:\narq = open(\"arquivo.txt\")\nlinhas = arq.readlines()\nfor linha in linhas:\n\tprint(linha)")
print ("Explicação: Utilizamos a estrutura de repetição FOR neste exemplo para que fosse impresso linha por linha enquanto existissem leituras na lista criada do arquivo.")
print ("Obs.:Será necessário você criar o cenário localmente com um arquivo txt para simular o exemplo descrito ou criar um cenário semelhante.")
print ("\n---x---\n")

#CRIANDO E ESCREVENDO EM ARQUIVOS
print ("Exemplo1: Criação de arquivo com escrita:\n")
print ("w = open(\"teste2.txt\", \"w\")\nw.write(\"Esse é o meu arquivo criado e já com escrita\")")
print ("\n\nExemplo2: Leitura de arquivo já existente com escrita sem apagar o que já existe:\n")
print ("w = open(\"arquivo.txt\", \"a\")\nw.write(\"\\nNova escrita no arquivo\"\nw.close()\n")