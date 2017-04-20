from flask import Blueprint

usuarios = Blueprint('usuarios', __name__)

@usuarios.route("/usuarios/", methods=['GET'])
def usuarios_get():
    return "TODOS OS USUARIOS"

@usuarios.route("/usuarios/<id>/", methods=['GET'])
def usuario_get(id):
    return "UM USUARIO %s" % id

@usuarios.route("/usuarios/", methods=['POST'])
def usuario_post():
    return "CRIAR USUARIO"