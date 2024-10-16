import os
import json
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from nxo_omega_prime import Neurocore, Picrypt, Echoplex, Auroranode, Spectraos, NexarionDB, NexarionAI
from nxo_omega_prime.utils import logger, error_handler
from nxo_omega_prime.config import config

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

# Initialize Nexarion Omega Prime components
neurocore = Neurocore()
picrypt = Picrypt()
echoplex = Echoplex()
auroranode = Auroranode()
spectraos = Spectraos()
nexarion_db = NexarionDB()
nexarion_ai = NexarionAI()

# API Endpoints

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    language_from = data['language_from']
    language_to = data['language_to']
    text = data['text']
    translated_text = neurocore.translate(text, language_from, language_to)
    return jsonify({'translated_text': translated_text})

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    text = data['text']
    encrypted_text = picrypt.encrypt(text)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    encrypted_text = data['encrypted_text']
    decrypted_text = picrypt.decrypt(encrypted_text)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data['message']
    recipient = data['recipient']
    echoplex.send_message(message, recipient)
    return jsonify({'message': 'Message sent successfully'})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    messages = echoplex.get_messages()
    return jsonify({'messages': messages})

@app.route('/node_management', methods=['POST'])
def node_management():
    data = request.get_json()
    action = data['action']
    node_id = data['node_id']
    auroranode.manage_node(action, node_id)
    return jsonify({'message': 'Node management successful'})

@app.route('/os_management', methods=['POST'])
def os_management():
    data = request.get_json()
    action = data['action']
    os_id = data['os_id']
    spectraos.manage_os(action, os_id)
    return jsonify({'message': 'OS management successful'})

@app.route('/ai_assistant', methods=['POST'])
def ai_assistant():
    data = request.get_json()
    query = data['query']
    response = nexarion_ai.process_query(query)
    return jsonify({'response': response})

@app.route('/db_query', methods=['POST'])
def db_query():
    data = request.get_json()
    query = data['query']
    results = nexarion_db.execute_query(query)
    return jsonify({'results': results})

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    file_path = os.path.join(config.UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return jsonify({'message': 'File uploaded successfully'})

@app.route('/file_download', methods=['GET'])
def file_download():
    file_name = request.args.get('file_name')
    file_path = os.path.join(config.UPLOAD_FOLDER, file_name)
    return send_file(file_path, as_attachment=True)

# SocketIO Events

@socketio.on('connect')
def connect():
    logger.info('Client connected')

@socketio.on('disconnect')
def disconnect():
    logger.info('Client disconnected')

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

@socketio.on('error')
def error_handler(error):
    logger.error(error)

if __name__ == '__main__':
    socketio.run(app, debug=True)
