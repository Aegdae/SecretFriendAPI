from flask import Flask, jsonify, request
from flask_cors import CORS
from dao import GrupoDAO, ParticipanteDAO
from entidade import Grupo, Participante
import random

app = Flask(__name__)
CORS(app)

GrupDAO = GrupoDAO()
PartDAO = ParticipanteDAO()

@app.route('/grupo')
def get_grupos():
    grupos = []
    for g in GrupDAO.obterTodos():
        grupos.append({"grupo_id": g.grupo_id,
                       "grupo_name": g.grupo_name})
    return jsonify(grupos)

@app.route("/grupo/<grupo_id>")
def get_grupo(grupo_id):
    g = GrupDAO.obter(grupo_id)
    if g is None:
        return jsonify({"Error": "Grupo não encontrado"}), 404
    return jsonify({"grupo_id": g.grupo_id,
                    "grupo_name": g.grupo_name})

@app.route("/grupo", methods=["POST"])
def add_grupo():
    grupo_json = request.get_json()
    if 'grupo_id' not in grupo_json or 'grupo_name' not in grupo_json:
        return jsonify({"Error": "Campos 'grupo_id' e 'grupo_name' são obrigatorios."}), 400
    grupo = Grupo(grupo_id=grupo_json['grupo_id'],
                  grupo_name=grupo_json['grupo_name'])
    GrupDAO.incluir(grupo)
    return '', 204

@app.route('/grupo/<grupo_id>', methods=['DELETE'])
def del_grupo(grupo_id):
    GrupDAO.excluir(grupo_id)
    return '', 204





@app.route('/participante/<grupo_id>')
def get_participante(grupo_id):
    participantes = [];
    for p in PartDAO.obterTodosGrupo(grupo_id):
        participantes.append({"part_id": p.part_id,
                              "part_name": p.part_name,
                              "grupo_id": p.grupo_id})
    return jsonify(participantes)

@app.route("/participante/<grupo_id>", methods=['POST'])
def add_participante(grupo_id):
    part_json = request.get_json()
    if 'part_id' not in part_json or 'part_name' not in part_json or 'grupo_id' not in part_json:
        return jsonify({"Error": "Campos 'part_id', 'part_name' e 'grupo_id' são obrigatorios."}), 400
    if part_json['grupo_id'] != int(grupo_id):
        return({"Error": "URL inconsistente com o novo participante"}), 400
    participante = Participante(part_id=part_json['part_id'],
                                part_name=part_json['part_name'],
                                grupo_id=part_json['grupo_id'])
    try:
        PartDAO.incluir(participante)
    except Exception as e:
        return jsonify({"Error": str(e)})
    return '', 204

@app.route('/participante/<participante_id>', methods=['DELETE'])
def del_participante(participante_id):
    PartDAO.excluir(participante_id)
    return '', 204

@app.route('/sorteio/<grupo_id>', methods=['GET'])
def sorteio(grupo_id):
    participantes = PartDAO.obterTodosGrupo(grupo_id)
    lista_part = [{"part_id": p.part_id, "part_name": p.part_name}for p in participantes]
    if len(lista_part) < 2:
        return jsonify({"Error": "Numero insuficiente de participantes para o sorteio."}), 400
    if len(lista_part) % 2 != 0:
        return jsonify({"Error": "Numero impar de participantes. Não é possivel formar todas as duplas"}), 400
    random.shuffle(lista_part)
    secretfriend = [
            {"parceiro_1": lista_part[i], "parceiro_2": lista_part[i+1]}
            for i in range(0, len(lista_part), 2)
    ]
    return jsonify({"grupo_id": grupo_id, "Amigo secreto": secretfriend})
    
if __name__ == "__main__":
    app.run(debug=True)