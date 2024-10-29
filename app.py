from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Ruta para mostrar la página de solicitud de ubicación
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para recibir la ubicación del usuario
@app.route('/save_location', methods=['POST'])
def save_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Aquí podrías guardar la ubicación en una base de datos o archivo
    print(f"Ubicación recibida: Latitud={latitude}, Longitud={longitude}")

    return jsonify({'message': 'Ubicación guardada correctamente'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 80)))
