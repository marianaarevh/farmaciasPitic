from flask import Flask, render_template, request, redirect, flash
import controlador_productos

app = Flask(__name__)

@app.route("/agregar_producto")
def formulario_agregar_producto():
    return render_template("agregar_productos.html")

@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    idproducto = request.form["idproducto"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    disponible = request.form["disponible"]
    idproveedor = request.form["idproveedor"]
    controlador_productos.insertar_producto(idproducto, descripcion, precio, stock, disponible, idproveedor)
    # De cualquier modo, y si todo fue bien, redirecciona
    return redirect("/productos")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/productos")
def productos():
    productos = controlador_productos.obtener_producto()
    return render_template("productos.html", productos=productos)

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    controlador_productos.eliminar_productos(request.form["id"])
    return redirect("/productos")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/formulario_editar_producto/<int:id>")
def editar_producto(id):
    # obtener el producto por ID:
    producto = controlador_productos.obtener_producto_por_id(id)
    return render_template("editar_producto.html", producto=producto)

@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    idproducto = request.form["idproducto"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    disponible = request.form["disponible"]
    idproveedor = request.form["idproveedor"]
    controlador_productos.actualizar_producto(idproducto, descripcion, precio, stock, disponible, idproveedor)
    return redirect("/productos")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

