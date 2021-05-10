from flask import Flask, jsonify, request
from flask_cors import CORS
import procesoEvento

app = Flask(__name__)
CORS(app)


@app.route('/')
def inicio():
    return jsonify({'mensaje': 'Servidor en ejecucion'})

@app.route('/recibirXML', methods=['POST'])
def recibirXML():
    datosXML = request.json['datos']
    print(request.json['datos'])                            #Mostrar datos recibidos del XML en la consola
    print('-----------------------------------------------------------------------------')
    eventos = datosXML.split("</EVENTO>")                   #Arreglo con split
    eventos.pop(len(eventos) - 1)                           #Quitando elemento extra que se crea
    
    #print(eventos)
    procesoEvento.recibirDatos(eventos)                     #Llamar evento para expresiones regulares
    eventos.clear()
    return jsonify({'mensaje': 'datos recibidos en el servidor'})   #Respuesta para el frontend

@app.route('/verDocumentacion', methods=['GET'])
def verDocumentacion():
    print('Si entro a documentación')
    return jsonify({'mensaje': 'mostrando documentación, espere un momento'})

@app.route('/reiniciarApp', methods=['GET'])
def reiniciarApp():
    print('Se ha reiniciado la App')
    procesoEvento.reiniciar()
    return jsonify({'mensaje': 'Aplicación reiniciada...'})

if __name__=='__main__':
    app.run(debug=True, port=5000)