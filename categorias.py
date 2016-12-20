# coding: utf8
import glob

arquivos = glob.glob("./entrada/*.xml")


def adiciona_tag(entidade, texto, inicio):
    nome_arquivo = busca_nome_arquivo(texto, inicio)
    if "Formação" in entidade:
        nome_categoria = "formacao"
    elif "Bacia" in entidade:
        nome_categoria = "baciaSEDIMENTAR"
    else:
        nome_categoria = "granulometria"

    texto = ''.join([texto[:inicio+len(entidade)], '</EM>', texto[inicio+len(entidade):]])
    texto = ''.join([texto[:inicio], '<EM ID="', nome_arquivo, '" CATEG="', nome_categoria, '">', texto[inicio:]])

    return texto


def busca_nome_arquivo(texto, inicio):
    ini = texto.rfind('<DOC DOCID="', 0, inicio) + 12
    fim = texto.find('">', ini)
    nome_arquivo = texto[ini:fim]
    return nome_arquivo


def encontra_todos(texto, categoria):
    inicio = 0
    while True:
        inicio = texto.find(categoria, inicio)
        if inicio == -1: return
        yield inicio
        inicio += len(categoria)


def processa_categoria(texto, entidades, categoria=None):
    if categoria is None:
        for entidade in entidades:
            lista = list(encontra_todos(texto, entidade))
            while len(lista) > 0:
                texto = adiciona_tag(entidade, texto, lista.pop())
                # print len(lista)
    else:
        lista = list(encontra_todos(texto, categoria))
        while len(lista) > 0:
            inicio = lista.pop()
            # print len(lista)
            for entidade in entidades:
                if entidade in texto[inicio:(inicio+len(entidade))]:
                    texto = adiciona_tag(entidade, texto, inicio)
                    break
    return texto


with open("Bacias.txt") as bacias_arquivo:
    bacias = bacias_arquivo.read()[:-1].split("\n")

with open("Formacoes.txt") as formacoes_arquivo:
    formacoes = formacoes_arquivo.read()[:-1].split("\n")

with open("Granulometrias.txt") as granulometrias_arquivo:
    granulometrias = granulometrias_arquivo.read()[:-1].split("\n")

print ("Dicionários criados")

for arquivo in arquivos:
    with open(arquivo) as texto:
        texto = texto.read()

        print ("Aciononando Tags de Bacia...")
        texto = processa_categoria(texto, bacias, "Bacia ")
        print ("Aciononando Tags de Formação...")
        texto = processa_categoria(texto, formacoes, "Formação ")
        print ("Aciononando Tags de Granulometria...")
        texto = processa_categoria(texto, granulometrias)

        file = open("./saida/" + arquivo[10:], 'w')
        file.write(texto)
        file.close()
