from flask import Flask, render_template, request, redirect, flash
import controlador_productos

app = Flask(__name__)

@app.route("/")
@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/agregar_proveedor")
def formulario_agregar_proveedor():
    return render_template("agregar_proveedor.html")

@app.route("/agregar_producto")
def formulario_agregar_producto():
    return render_template("agregar_productos.html")

@app.route("/agregar_pedido")
def formulario_agregar_pedido():
    return render_template("agregar_pedidos.html")

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

@app.route("/guardar_proveedor", methods=["POST"])
def guardar_proveedor():
    idproveedor = request.form["idproveedor"]
    proveedor = request.form["proveedor"]
    controlador_productos.insertar_proveedor(idproveedor, proveedor)
    # De cualquier modo, y si todo fue bien, redirecciona
    return redirect("/proveedor")

@app.route("/guardar_pedido", methods=["POST"])
def guardar_pedido():
    idpedido = request.form["idpedido"]
    fechapedido = request.form["fechapedido"]
    estadopedido = request.form["estadopedido"]
    idproducto = request.form["idproducto"]
    controlador_productos.insertar_pedido(idpedido, fechapedido, estadopedido, idproducto)
    # De cualquier modo, y si todo fue bien, redirecciona
    return redirect("/pedidos")

#@app.route("/")
@app.route("/productos")
def productos():
    productos = controlador_productos.obtener_producto()
    return render_template("productos.html", productos=productos)

@app.route("/proveedor")
def proveedor():
    proveedor = controlador_productos.obtener_proveedor()
    print(proveedor)
    return render_template("proveedor.html", proveedor=proveedor)

@app.route("/pedidos")
def pedidos():
    pedidos = controlador_productos.obtener_pedido()
    return render_template("pedidos.html", pedidos=pedidos)

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    controlador_productos.eliminar_productos(request.form["id"])
    return redirect("/productos")

@app.route("/eliminar_proveedor", methods=["POST"])
def eliminar_proveedor():
    idproveedor = request.form.get("idproveedor")
    if idproveedor is not None:
        controlador_productos.eliminar_proveedor(idproveedor)
    return redirect("/proveedor")

@app.route("/eliminar_pedido", methods=["POST"])
def eliminar_pedido():
    controlador_productos.eliminar_pedido(request.form["id"])
    return redirect("/pedidos")

@app.route("/formulario_editar_producto/<int:id>")
def editar_producto(id):
    # obtener el producto por ID:
    producto = controlador_productos.obtener_producto_por_id(id)
    return render_template("editar_producto.html", producto=producto)

@app.route("/formulario_editar_proveedor/<int:id>")
def editar_proveedor(id):
    # obtener el producto por ID:
    proveedor = controlador_productos.obtener_proveedor_por_id(id)
    return render_template("editar_proveedor.html", proveedor=proveedor)

@app.route("/formulario_editar_pedido/<int:id>")
def editar_pedido(id):
    # obtener el producto por ID:
    pedido = controlador_productos.obtener_pedido_por_id(id)
    return render_template("editar_pedido.html", pedido=pedido)

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

@app.route("/actualizar_proveedor", methods=["POST"])
def actualizar_proveedor():
    idproveedor = request.form["idproveedor"]
    proveedor = request.form["proveedor"]
    controlador_productos.actualizar_proveedor(idproveedor, proveedor)
    return redirect("/proveedor")

@app.route("/actualizar_pedido", methods=["POST"])
def actualizar_pedido():
    idpedido = request.form["idpedido"]
    fechapedido = request.form["fechapedido"]
    estadopedido = request.form["estadopedido"]
    idproducto = request.form["idproducto"]
    controlador_productos.actualizar_pedido(idpedido, fechapedido, estadopedido, idproducto)
    return redirect("/pedidos")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

