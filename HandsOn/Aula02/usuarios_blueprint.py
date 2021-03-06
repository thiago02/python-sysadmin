from flask import Blueprint, jsonify, request
from Model import Usuarios
import json 

usuarios = Blueprint('usuarios', __name__)

@usuarios.route("/usuarios/", methods=['GET'])
def usuarios_get():
	usuarios = json.loads(Usuarios.objects.to_json())
	return jsonify({"usuarios": usuarios})



	return "TODOS OS USUARIOS"

@usuarios.route("/usuarios/<id>/", methods=['GET'])
def usuario_get(id):
	user = json.loads(Usuarios.objects(id=id).to_json())
	return jsonify({"usuario": user})




    #return "UM USUARIO %s" % id

@usuarios.route("/usuarios/", methods=['POST'])
def usuario_post():
	user = request.get_json()

	userModel = Usuarios()

	for usr in user.keys():

		setattr(userModel, usr, user[usr])

	userModel.save()
	return jsonify({'message': "usuario cadastrado com sucesso!"})


@usuarios.route("/usuarios/<id>/", methods=['DELETE'])
def usuario_delete(id):
	userModel = Usuarios.objects(id=id)
	userModel.delete()

	return jsonify({"message": "Usuario removido com sucesso"})