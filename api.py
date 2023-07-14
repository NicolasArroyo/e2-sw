from classes import Operacion, Cuenta
from flask import Flask, request, jsonify

app = Flask(__name__)

bd = [Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
      Cuenta("123", "Luisa", 400, ["456"]),
      Cuenta("456", "Andrea", 300, ["21345"])]


@app.route("/billetera/contactos", methods=["GET"])
def get_contactos():

    numero = request.args.get("minumero")
    for cuenta in bd:
        if cuenta.numero == numero:
            return jsonify(cuenta.get_lista_contactos()), 200

    return jsonify({"error": "cuenta no encontrada"}), 404


@app.route("/billetera/pagar", methods=["GET"])
def post_operacion():

    numero = request.args.get("minumero")
    numero_destino = request.args.get("numerodestino")
    valor = request.args.get("valor")

    nueva_operacion = Operacion(numero, numero_destino, valor)

    flag_error = False
    for cuenta in bd:
        if numero == cuenta.numero:
            if cuenta.enviar_operacion(nueva_operacion):
                flag_error = True

    if flag_error:
        for cuenta in bd:
            if numero_destino == cuenta.numero:
                cuenta.recibir_operacion(nueva_operacion)

    if flag_error:
        return jsonify({"success": "operacion enviada"}), 200

    if not flag_error:
        return jsonify({"error": "no se pudo realizar la operacion"}), 404


@app.route("/billetera/enviadas", methods=["GET"])
def get_enviadas():

    numero = request.args.get("minumero")

    for cuenta in bd:
        if cuenta.numero == numero:
            return jsonify(cuenta.get_operaciones_enviadas()), 200

    return jsonify({"error": "cuenta no encontrada"}), 404


@app.route("/billetera/recibidas", methods=["GET"])
def get_recibidas():

    numero = request.args.get("minumero")

    for cuenta in bd:
        if cuenta.numero == numero:
            return jsonify(cuenta.get_operaciones_recibidas()), 200

    return jsonify({"error": "cuenta no encontrada"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=8000)
