from flask import Flask, jsonify, request

app = Flask(__name__)


productos = [
    {
        "id": 1,
        "nombre": "Teclado",
        "precio": 250
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "precio": 150
    }
]


# Ruta principal
@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API de productos funcionando"
    })


# GET: mostrar todos los productos
@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)


# POST: agregar un producto
@app.route("/productos", methods=["POST"])
def agregar_producto():

    datos = request.get_json()

    nuevo_producto = {
        "id": len(productos) + 1,
        "nombre": datos["nombre"],
        "precio": datos["precio"]
    }

    productos.append(nuevo_producto)

    return jsonify({
        "mensaje": "Producto agregado",
        "producto": nuevo_producto
    })


# PUT: modificar un producto
@app.route("/productos/<int:id>", methods=["PUT"])
def modificar_producto(id):

    datos = request.get_json()

    for producto in productos:

        if producto["id"] == id:

            producto["nombre"] = datos["nombre"]
            producto["precio"] = datos["precio"]

            return jsonify({
                "mensaje": "Producto modificado",
                "producto": producto
            })

    return jsonify({
        "mensaje": "Producto no encontrado"
    })


# DELETE: eliminar un producto
@app.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):

    for producto in productos:

        if producto["id"] == id:

            productos.remove(producto)

            return jsonify({
                "mensaje": "Producto eliminado",
                "producto": producto
            })

    return jsonify({
        "mensaje": "Producto no encontrado"
    })


if __name__ == "__main__":
    app.run(debug=True)
