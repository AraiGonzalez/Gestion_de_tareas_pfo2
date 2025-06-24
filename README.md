# Gestión de Tareas
Practica Formativa Nº2 . programación sobre redes, Tecnicatura superior en desarrollo de software.Arai Gonzalez,comisión B
Este proyecto es una aplicación web desarrollada en Python utilizando Flask. Permite registrar usuarios, iniciar sesión y muestra una vista de gestion de tareas(sin funcionalidad). Las contraseñas de los usuarios se almacenan de forma segura utilizando hashing.
## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/AraiGonzalez/Gestion_de_tareas_pfo2.git
  
## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes requisitos:

- Python 3.10 o superior
- `pip` actualizado

# PARA WINDOWS
# Crear un entorno virtual
python -m venv .venv

# Activar el entorno virtual
.venv\Scripts\activate

# Instalar las dependencias desde requirements.txt
pip install -r requirements.txt
pip install Flask==2.3.2 Werkzeug==2.3.7

# PARA LINUX
# Crear un entorno virtual
python3 -m venv .venv

# Activar el entorno virtual
source .venv/bin/activate

# Instalar las dependencias desde requirements.txt
pip install -r requirements.txt
pip install Flask==2.3.2 Werkzeug==2.3.7

# Ejecución
Inicia el servidor Flask:
python servidor.py
# IMPORTANTE
Asegúrate de que el archivo tareas.db se genere correctamente al iniciar el servidor. Este archivo se utiliza para almacenar los datos de los usuarios.
# Prubas en Postman (opcional, para probar las rutas)
Página principal: http://127.0.0.1:5000/
Registro de usuarios
Método: POST
URL: http://127.0.0.1:5000/registro
Cuerpo (JSON):
{
  "usuario": "nombre",
  "contraseña": "1234"
}
-la contraseña y usuario puede ser cualquiera
Inicio de sesión
Método: POST
URL: http://127.0.0.1:5000/login
Cuerpo (JSON):
{
  "usuario": "testuser",
  "contraseña": "testpassword"
}
Visualización de tareas
Método: GET
URL: http://127.0.0.1:5000/tareas

# ¿Por qué hashear contraseñas?
Para protegerlas en caso de que la base de datos sea comprometida. El hashing es unidireccional, lo que dificulta revertirlo y mejora la seguridad.

# Ventajas de usar SQLite:
Fácil de configurar, porque no necesita servidor.
todo se guarda en un archivo, eso lo hace portable
