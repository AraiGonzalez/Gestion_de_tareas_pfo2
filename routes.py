# routes.py
from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection
import sqlite3

routes = Blueprint('routes', __name__)
@routes.route('/', methods=['GET'])
def home():
    return render_template('tarea.html')
@routes.route('/registro', methods=['POST'])
def registro():
    data = request.json
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({'error': 'Usuario y contraseña son requeridos'}), 400

    contraseña_hash = generate_password_hash(contraseña)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (usuario, contraseña_hash))
        conn.commit()
        conn.close()
        return jsonify({'mensaje': 'Usuario registrado exitosamente'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El usuario ya existe'}), 400

@routes.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({'error': 'Usuario y contraseña son requeridos'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
    result = cursor.fetchone()
    conn.close()

    if result and check_password_hash(result[0], contraseña):
        return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401

@routes.route('/tareas', methods=['GET'])
def tareas():
    return render_template('tarea.html')