archivo = open("convert.txt", "r", encoding='utf-8') 
convertido = open("convertido.txt", "w", encoding='utf-8') 
capitulos = ['I','II','III','IV','V','VI','VII','VIII']
subcapitulos = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h']
capitulo_final = ['ACKNOWLEDGMENT', 'ACKNOWLEDGMENTS']
for linea in archivo.readlines(): 
    if linea[-1]=='\n':
        linea_convertida=linea[:-1]
        try:
            if linea_convertida in capitulo_final  or linea_convertida[-1]=='.':
                linea_convertida += '\n'
            elif linea_convertida[-1]=='-':
                linea_convertida = linea_convertida[:-1]
            else:
                linea_split=linea_convertida.split('.')
                if linea_split[0] in capitulos + subcapitulos :
                    linea_convertida += '\n'
        except IndexError:
            print('linea_convertida es vacia')
        print(linea_convertida)
        convertido.write(linea_convertida)
archivo.close()
convertido.close()

import goslate
import urllib.error as error

gs = goslate.Goslate()
archivo_para_traducir = open('convertido.txt',encoding='utf-8')
archivo_traducido = open("traducido.txt", "w", encoding='utf-8') 
try:
    for linea in archivo_para_traducir.readlines():
        linea_traducida=gs.translate(linea,'es')
        archivo_traducido.write(linea_traducida+'\n')
except error.HTTPError:
    print('NO SE PUDO TRADUCIR , EL API DE GOOGLE NO LO SOPORTO :c')
archivo_traducido.close()
