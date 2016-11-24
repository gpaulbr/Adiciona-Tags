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
    inicio = len(sub_texto_inicial + '<EM ID="' + arquivo[10:-4] + '" CATEG="baciaSEDIMENTAR">')
    return texto, inicio


with open("Bacias.txt") as bacias_arquivo:
    bacias = bacias_arquivo.read()[:-1].split("\n")

with open("Formacoes.txt") as formacoes_arquivo:
    formacoes = formacoes_arquivo.read()[:-1].split("\n")

with open("Granulometrias.txt") as granulometrias_arquivo:
    granulometrias = granulometrias_arquivo.read()[:-1].split("\n")

inicio = 0
for arquivo in arquivos:
    with open(arquivo) as texto:
        texto = texto.read()
        print texto[:1000]
        while inicio != -1:
            inicio = texto.find("Bacia", inicio)
            print inicio
            for bacia in bacias:    
                if bacia in texto[inicio:(inicio+len(bacia))]:
                    print bacia
                    texto, inicio = adiciona_tag(bacia, texto, inicio)
        

        file = open("./saida/" + arquivo[10:], 'w')
        file.write(texto)
        file.close()