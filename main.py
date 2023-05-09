from flask import Flask, render_template, request, redirect, flash, session
import controlador_productos, controlador_login
from bd import obtener_conexion
from datetime import date


app = Flask(__name__)

secret_key = "25e630a27f4f583aafb35ca6b37dce88a422d10007141147c2120e13de8c00f8"
app.config['SECRET_KEY'] = secret_key

@app.route("/agregar_proveedor")
def formulario_agregar_proveedor():
    if session.get('logged_in', False):
        return render_template("agregar_proveedor.html")
    else: return redirect("/login")

@app.route("/agregar_producto")
def formulario_agregar_producto():
    if session.get('logged_in', False):
        proveedores=controlador_productos.obtener_proveedor()
        return render_template("agregar_productos.html",proveedores=proveedores)
    else: return redirect("/login")

@app.route("/agregar_pedido")
def formulario_agregar_pedido():
    if session.get('logged_in', False):
        proveedores=controlador_productos.obtener_proveedor()
        productos=controlador_productos.obtener_producto_activos()
        return render_template("agregar_pedidos.html",proveedores=proveedores,productos=productos, fecha_actual=date.today())
    else: return redirect("/login")

@app.route("/agregar_entrega")
def formulario_agregar_entrega():
    if session.get('logged_in', False):
        proveedores=controlador_productos.obtener_proveedor()
        productos=controlador_productos.obtener_producto_todos()
        return render_template("agregar_entrega.html",proveedores=proveedores,productos=productos,fecha_actual=date.today())
    else: return redirect("/login")


@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    if session.get('logged_in', False):
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        stock = request.form["stock"]
        disponible = request.form["disponible"]
        idproveedor = request.form["idproveedor"]
        controlador_productos.insertar_producto( descripcion, precio, stock, disponible, idproveedor)
        # De cualquier modo, y si todo fue bien, redirecciona
        return redirect("/productos")
    else: return redirect("/login")

@app.route("/guardar_proveedor", methods=["POST"])
def guardar_proveedor():
    if session.get('logged_in', False):
        proveedor = request.form["proveedor"]
        controlador_productos.insertar_proveedor(proveedor)
        # De cualquier modo, y si todo fue bien, redirecciona
        return redirect("/proveedor")
    else: return redirect("/login")

@app.route("/guardar_pedido", methods=["POST"])
def guardar_pedido():
    if session.get('logged_in', False):
        fechapedido = request.form["fechapedido"]
        estadopedido = request.form["estadopedido"]
        idproducto = request.form["idproducto"]
        controlador_productos.insertar_pedido(fechapedido, estadopedido, idproducto)
        # De cualquier modo, y si todo fue bien, redirecciona
        return redirect("/pedidos")
    else: return redirect("/login")

@app.route("/guardar_entrega", methods=["POST"])
def guardar_entrega():
    if session.get('logged_in', False):
        fechaentrega = request.form["fechaentrega"]
        idproveedor = request.form["idproveedor"]
        idproducto = request.form["idproducto"]
        cantidad = request.form["cantidad"]
        controlador_productos.insertar_enpr(fechaentrega, idproveedor, idproducto, cantidad)
        # De cualquier modo, y si todo fue bien, redirecciona
        return redirect("/entregas")
    else: return redirect("/login")

#@app.route("/")
@app.route("/productos")
def productos():
    if session.get('logged_in', False):
        productos = controlador_productos.obtener_producto()
        return render_template("productos.html", productos=productos)
    else: return redirect("/login")

@app.route("/proveedor")
def proveedor():
    if session.get('logged_in', False):
        proveedor = controlador_productos.obtener_proveedor()
        print(proveedor)
        return render_template("proveedor.html", proveedor=proveedor)
    else: return redirect("/login")

@app.route("/pedidos")
def pedidos():
    if session.get('logged_in', False):
        pedidos = controlador_productos.obtener_pedido()
        return render_template("pedidos.html", pedidos=pedidos)
    else: return redirect("/login")

@app.route("/entregas")
def entregas():
    if session.get('logged_in', False):
        entregas = controlador_productos.obtener_enpr()
        return render_template("entregas.html", entregas=entregas)
    else: return redirect("/login")

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    if session.get('logged_in', False):
        controlador_productos.eliminar_productos(request.form["id"])
        return redirect("/productos")
    else: return redirect("/login")


@app.route("/eliminar_proveedor", methods=["POST"])
def eliminar_proveedor():
    if session.get('logged_in', False):
        idproveedor = request.form.get("idproveedor")
        if idproveedor is not None:
            controlador_productos.eliminar_proveedor(idproveedor)
        return redirect("/proveedor")
    else: return redirect("/login")

@app.route("/eliminar_pedido", methods=["POST"])
def eliminar_pedido():
    if session.get('logged_in', False):
        controlador_productos.eliminar_pedido(request.form["id"])
        return redirect("/pedidos")
    else: return redirect("/login")

@app.route("/eliminar_entrega", methods=["POST"])
def eliminar_entrega():
    if session.get('logged_in', False):
        controlador_productos.eliminar_enpr(request.form["id"])
        return redirect("/entregas")
    else: return redirect("/login")

@app.route("/formulario_editar_producto/<int:id>")
def editar_producto(id):
    if session.get('logged_in', False):
        # obtener el producto por ID:
        producto = controlador_productos.obtener_producto_por_id(id)
        proveedores=controlador_productos.obtener_proveedor()
        return render_template("editar_producto.html", producto=producto,proveedores=proveedores)
    else: return redirect("/login")

@app.route("/formulario_editar_proveedor/<int:id>")
def editar_proveedor(id):
    if session.get('logged_in', False):
        # obtener el producto por ID:
        proveedor = controlador_productos.obtener_proveedor_por_id(id)
        return render_template("editar_proveedor.html", proveedor=proveedor)
    else: return redirect("/login")

@app.route("/formulario_editar_pedido/<int:id>")
def editar_pedido(id):
    if session.get('logged_in', False):
        # obtener el producto por ID:
        productos=controlador_productos.obtener_producto_todos()
        pedido = controlador_productos.obtener_pedido_por_id(id)
        return render_template("editar_pedido.html", pedido=pedido,productos=productos)
    else: return redirect("/login")

@app.route("/formulario_editar_entrega/<int:id>")
def editar_entrega(id):
    if session.get('logged_in', False):
        # obtener el producto por ID:
        entrega = controlador_productos.obtener_enpr_por_id(id)
        productos=controlador_productos.obtener_producto_activos()
        proveedores=controlador_productos.obtener_proveedor()
        return render_template("editar_entrega.html", entrega=entrega,productos=productos,proveedores=proveedores)
    else: return redirect("/login")

@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    if session.get('logged_in', False):
        idproducto = request.form["idproducto"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        stock = request.form["stock"]
        disponible = request.form["disponible"]
        idproveedor = request.form["idproveedor"]
        controlador_productos.actualizar_producto(idproducto, descripcion, precio, stock, disponible, idproveedor)
        return redirect("/productos")
    else: return redirect("/login")

@app.route("/actualizar_proveedor", methods=["POST"])
def actualizar_proveedor():
    if session.get('logged_in', False):
        idproveedor = request.form["idproveedor"]
        proveedor = request.form["proveedor"]
        controlador_productos.actualizar_proveedor(idproveedor, proveedor)
        return redirect("/proveedor")
    else: return redirect("/login")

@app.route("/actualizar_pedido", methods=["POST"])
def actualizar_pedido():
    if session.get('logged_in', False):
        idpedido = request.form["idpedido"]
        fechapedido = request.form["fechapedido"]
        estadopedido = request.form["estadopedido"]
        idproducto = request.form["idproducto"]
        controlador_productos.actualizar_pedido(idpedido, fechapedido, estadopedido, idproducto)
        return redirect("/pedidos")
    else: return redirect("/login")

@app.route("/actualizar_entrega", methods=["POST"])
def actualizar_entrega():
    if session.get('logged_in', False):
        identrega = request.form["identrega"]
        fechaentrega = request.form["fechaentrega"]
        idproveedor = request.form["idproveedor"]
        idproducto = request.form["idproducto"]
        cantidad = request.form["cantidad"]
        controlador_productos.actualizar_enpr(identrega, fechaentrega, idproveedor, idproducto, cantidad)
        return redirect("/entregas")
    else: return redirect("/login")

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session.get('logged_in', False):
        return render_template("dashboard.html")
    else:
        return redirect("/login")

@app.route('/login', methods=['GET', 'POST'])
def loginI():
    if session.get('logged_in', False):
        return redirect('/dashboard')
    
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        username = request.form['username']
        contrasena = request.form['contrasena']
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM login_python WHERE username=%s AND contrasena=%s", (username, contrasena))
        user = cursor.fetchone()
        if user is not None:
            session['logged_in'] = True
            return redirect('/dashboard')
        else:
            return render_template('login.html', error=True)


@app.route('/')
def index():
    if session.get('logged_in', False):
        return redirect("/dashboard")
    else:
        return redirect("/login")

@app.route('/logout')
def logout(): 
    session['logged_in'] = False
    return redirect('/login')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

