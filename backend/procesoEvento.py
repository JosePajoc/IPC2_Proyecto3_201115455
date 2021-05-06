import re

listaDatos = []
def recibirDatos(lista):
    listaDatos = lista
    print('Se recibio')
    #Mostrando los datos en consola
    for eve in listaDatos:
        fechas = re.findall('Guatemala.+Reportado', eve)                     #Extraer todo lo que se encuente entre
        fecha = fechas[0].replace('Reportado','')
        print('Fecha:           ', fecha)

        correos = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', eve)
        reportadoPor = correos[0].replace('Usuarios','')
        correos.pop(0)
        print('Reportado por:           ', reportadoPor)
        #correos[len(correos)-1].replace('Error','')
        print('Afectados:           ', correos)

        errores = re.findall('Error.+\S', eve)
        error1 = errores[0].replace('Error','')
        print('Error:           ', error1)
