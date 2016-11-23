# coding: utf8
import glob

arquivos = glob.glob("./entrada/*.txt")

def adiciona_tag(bacia, texto, inicio, arquivo):
    sub_texto_inicial = texto[:inicio+len(bacia)]
    sub_texto_final = texto[inicio+len(bacia):]
    texto = sub_texto_inicial + '</EM>' + sub_texto_final
    sub_texto_inicial = texto[:inicio]
    sub_texto_final = texto[inicio:]
    texto = sub_texto_inicial + '<EM ID="' + arquivo + '" CATEG="baciaSEDIMENTAR">' + sub_texto_final
    return texto


bacias = ["Bacia do Paraná", "Bacia do Acre", "Bacia do Marajó", "Bacia do Jacaúnas"]
for arquivo in arquivos:
    with open(arquivo) as texto:
        texto = texto.read()
        inicio = texto.find("Bacia")
        for bacia in bacias:    
            if bacia in texto[inicio:(inicio+len(bacia))]:
                print bacia
                texto = adiciona_tag(bacia, texto, inicio, arquivo)
        

        file = open("./saida/" + arquivo[10:], 'w')
        file.write(texto)
        file.close()