from flask import Flask, jsonify, request
from flask_cors import CORS
import procesoEvento

app = Flask(__name__)
CORS(app)

eventosXML = []                                             #Lista con eventos individuales

@app.route('/inicio')
def inicio():
    return jsonify({'mensaje': 'Servidor en ejecucion'})

@app.route('/recibirXML', methods=['POST'])
def recibirXML():
    global eventosXML
    datosXML = request.json['datos']
    print(request.json['datos'])                            #Mostrar datos del XML recibidos
    print('-----------------------------------------------------------------------------')
    datosXML = datosXML.replace('<EVENTOS>','')             #Quitar etiquetas
    datosXML = datosXML.replace('</EVENTOS>','')
    eventos = datosXML.split("</EVENTO")                    #Arreglo con split
    #Quitando datos innecesarios
    for eve in eventos:
        eve = eve.replace('<EVENTO>', '')                   
        eve = eve.replace('\n', '')
        eve = eve.replace('\t', '')
        eve = eve.replace('>', '')
        eventosXML.append(eve)                              #Asignando a la lista de eventos individuales
    eventosXML.pop(len(eventos) - 1)
    #Respuesta para el frontend
    procesoEvento.recibirDatos(eventosXML)
    eventosXML.clear()
    return jsonify({'datos recibidos en el backend': request.json['datos']})

if __name__=='__main__':
    app.run(debug=True, port=5000)