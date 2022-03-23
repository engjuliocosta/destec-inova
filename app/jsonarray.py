# Lógica das Rotas
"""from flask import Flask, Blueprint, current_app, request, jsonify, request
from .model import Json_PlaceHold
from .serealizer import Json_Placehold_Schema

# Nomenaodo Blueprint
bp_jsonph = Blueprint('arrays_id', __name__)

@bp_jsonph.route('/mostrar', methods=['GET'])
def mostrar():
    bs = Json_Placehold_Schema(many=True)
    id_array = get(request.json('https://jsonplaceholder.typicode.com/todos'))
    result = Json_PlaceHold.query.all()
    return bs.jsonify(result), 200

@bp_jsonph.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    '''id_array.query.filter(id_array.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado.')'''
    ...



@app.route('/validate-json', methods=['POST'])
def validate_json():
    if request.post(json('https://jsonplaceholder.typicode.com/todos')):
    return {
        "id": 0,
        "title": '<nome do registro>',
          }, 200
    return
        '''bs = Json_Placehold_Schema()
        query = id_array.query.filter(id_array.id == identificador)
        query.update(request.json)
        current_app.db.session.commit()
        crud_init = bs.jsonify(query.first())
        return jsonify({}), 200'''
    ...

@bp_jsonph.route('/cadastrar', methods=['POST'])
def cadastrar(identificador):
    '''bs = Json_Placehold_Schema()
    id_array, title, error = bs.load(request.json)
    current_app.db.session.add(id)
    current_app.db.session.commit()
    return bs.jsonify(id_array), 200'''
    ...

"""
