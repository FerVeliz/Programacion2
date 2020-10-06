from flask import Flask, jsonify, request

app=Flask(__name__)

from Materias import Materias

@app.route("/Materias", methods=["GET"])
def getMaterias():
    return jsonify({"Materias":Materias})

@app.route("/Materias/<int:id_materia>", methods=["GET"])
def getMateria(id_materia):
    MateriaEncontrada=[materia for materia in Materias if materia["id"]==id_materia]
    if(len(MateriaEncontrada)>0):
        return jsonify({"Materia":MateriaEncontrada[0]})
    else:
        return jsonify({"message":"Materia no encontrada"})

@app.route("/Materias", methods=["POST"])
def addMateria():
    new_materia={
        "name": request.json["name"],
        "id": request.json["id"],
        "workload": request.json["workload"],
        "correlative": request.json["correlative"]
    }
    Materias.append(new_materia)
    return jsonify({"message": "Materia agregada correctamente", "Materia": new_materia})

@app.route("/Materias/<int:id_materia>", methods=["PUT"])
def editMateria(id_materia):
    materiaEncontrada=[materia for materia in Materias if materia["id"]==id_materia]
    if(len(materiaEncontrada)>0):
        materiaEncontrada[0]["name"] = request.json["name"]
        materiaEncontrada[0]["id"] = request.json["id"]
        materiaEncontrada[0]["workload"] = request.json["workload"]
        materiaEncontrada[0]["correlative"] = request.json["correlative"]
        return jsonify({
            "message":"Materia modificada",
            "Materia":materiaEncontrada[0]
        })
    else:
        return jsonify({"message":"Materia no encontrado"})

@app.route("/Materias/<int:id_materia>", methods=["DELETE"])
def deleteMateria(id_materia):
    materiaEncontrada=[materia for materia in Materias if materia["id"]==id_materia]
    if(len(materiaEncontrada)>0):
        Materias.remove(materiaEncontrada[0])
        return jsonify({
            "message":"Materia "+ materiaEncontrada[0]["name"]+ " eliminada.",
            "Materias":Materias
        })
    else:
        return jsonify({
            "message":"Materia no encontrada"
        })
if __name__=="__main__":
    app.run(debug=True, port=4000)