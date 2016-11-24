# coding: utf8
import glob

arquivos = glob.glob("./entrada/*.xml")

def adiciona_tag(entidade, texto, inicio):
    sub_texto_inicial = texto[:inicio+len(entidade)]
    sub_texto_final = texto[inicio+len(entidade):]
    texto = sub_texto_inicial + '</EM>' + sub_texto_final
    sub_texto_inicial = texto[:inicio]
    sub_texto_final = texto[inicio:]
    texto = sub_texto_inicial + '<EM ID="' + arquivo[10:-4] + '" CATEG="baciaSEDIMENTAR">' + sub_texto_final
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
        inicio = texto.find("Bacia")
        for bacia in bacias:    
            if bacia in texto[inicio:(inicio+len(bacia))]:
                print bacia
                texto = adiciona_tag(bacia, texto, inicio)
        

        file = open("./saida/" + arquivo[10:], 'w')
        file.write(texto)
        file.close()