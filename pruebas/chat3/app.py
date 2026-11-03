import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import ollama

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/evaluar', methods=['POST'])
def evaluar():
    try:
        data = request.get_json()
        requerimiento = data.get("state", "")
        questions = data.get("questions", {})

        # Petición a Ollama
        response = ollama.systemone(
            model="d1-omni:600m",
            state=requerimiento,
            questions=questions
        )

        condicion = response.answers["condicion"].noul
        condicion_1 = response.answers["condicion_1"].noul
        condicion_2 = response.answers["condicion_2"].noul
        condicion_3 = response.answers["condicion_3"].noul
        condicion_4 = response.answers["condicion_4"].noul
        condicion_5 = response.answers["condicion_5"].noul

        # Imprimir en consola de Python
        if condicion >= 0.05:
            print(f"1. Cumple con la condición: {condicion}")
        else:
            print(f"1. No cumple con la condición: {condicion}")

        if condicion_1 >= 0.05:
            print(f"2. Cumple con la condición: {condicion_1}")
        else:
            print(f"2. No cumple con la condición: {condicion_1}")

        if condicion_2 >= 0.05:
            print(f"3. Cumple con la condición: {condicion_2}")
        else:
            print(f"3. No cumple con la condición: {condicion_2}")

        if condicion_3 >= 0.05:
            print(f"4. Cumple con la condición: {condicion_3}")
        else:
            print(f"4. No cumple con la condición: {condicion_3}")

        if condicion_4 >= 0.05:
            print(f"5. Cumple con la condición: {condicion_4}")
        else:
            print(f"5. No cumple con la condición: {condicion_4}")

        if condicion_5 >= 0.05:
            print(f"6. Cumple con la condición: {condicion_5}")
        else:
            print(f"6. No cumple con la condición: {condicion_5}")

        print(response.answers["condicion"])

        # SOLUCIÓN AL ERROR 500: Construir un diccionario serializable para jsonify
        respuesta_json = {
            "answers": {
                "condicion": {"noul": condicion},
                "condicion_1": {"noul": condicion_1},
                "condicion_2": {"noul": condicion_2},
                "condicion_3": {"noul": condicion_3},
                "condicion_4": {"noul": condicion_4},
                "condicion_5": {"noul": condicion_5}
            }
        }

        return jsonify(respuesta_json)

    except Exception as error:
        print(f"Error procesando la solicitud: {error}")
        return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)