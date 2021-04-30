from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/inicio')
def inicio():
    return jsonify({'mensaje': 'Servidor en ejecucion'})

@app.route('/recibirXML', methods=['POST'])
def recibirXML():
    print(request.json['datos'])
    return jsonify({'datos recibidos en el backend': request.json['datos']})


if __name__=='__main__':
    app.run(debug=True, port=5000)