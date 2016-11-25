# coding: utf8
import glob

arquivos = glob.glob("./entrada/*.xml")

def adiciona_tag(entidade, texto, inicio):
    sub_texto_inicial = texto[:inicio+len(entidade)]
    sub_texto_final = texto[inicio+len(entidade):]
    texto = sub_texto_inicial + '</EM>' + sub_texto_final
    sub_texto_inicial = texto[:inicio]
    sub_texto_final = texto[inicio:]
    texto = sub_texto_inicial + '<EM ID="' + arquivo[10:-4] + '" CATEG="granulometria">' + sub_texto_final

    return texto


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
            print entidade
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

for arquivo in arquivos:
    with open(arquivo) as texto:
        texto = texto.read()
        for i in granulometrias:
            print i
        texto = processa_categoria(texto, bacias, "Bacia ")
        texto = processa_categoria(texto, formacoes, "Formação ")
        texto = processa_categoria(texto, granulometrias)

        file = open("./saida/" + arquivo[10:], 'w')
        file.write(texto)
        file.close()