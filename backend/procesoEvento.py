import re                                                              #Uso de expresiones regulares
from eventos import evento                                             #Importando la clase eventos
from io import open                                                    #Importando módulo para crear archivo plano
import webbrowser

listaEventos = []                                                      #Lista de objetos

def recibirDatos(lista):
    listaDatos = lista                                                 #Lista con eventos
    #Aplicando expresiones regulares a cada elemento
    for eve in listaDatos:
        fecha = re.findall('[0-9]+/[0-9]+/[0-9]+', eve)                #Extraer fecha
        print('Fecha:           ', fecha)

        correos = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', eve)         #extraer correos
        print('Reportado por:   ', correos[0])
        reportadoPor = correos[0]                                       #Seperara quién reporto
        correos.pop(0)                                                  #Quitar de la lista de correo quién reporto
        print('Afectados:       ', correos)

        errores = re.findall('Error.+\S', eve)                          #Extraer el error
        error1 = errores[0].replace('Error:','')                        #Eliminar la palabra Error
        print('Error:       ', error1)

        listaEventos.append(evento(fecha, reportadoPor, correos, error1))
        print('-----------------------------------------------------------------------------')

def reiniciar():
    if len(listaEventos)>0:
        print('Lista vacía')
        listaEventos.clear()

def crearXML():
    salidaXML = open('salida.xml', 'w')
    respuesta = '<ESTADISTICAS>\n'
    salidaXML.write('<ESTADISTICAS>\n')

    salidaXML.write('</ESTADISTICAS>')
    respuesta = respuesta + '</ESTADISTICAS>'
    salidaXML.close()
    return respuesta

def verDocumentacion():
    webbrowser.open_new_tab('documentacion.pdf')
