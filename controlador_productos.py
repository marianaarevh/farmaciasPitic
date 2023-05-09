from bd import obtener_conexion

def insertar_producto(descripcion, precio, stock, disponible, idproveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO productos(descripcion, precio, stock, disponible, idproveedor) VALUES (%s, %s,%s, %s, %s)",
        (descripcion, precio, stock, disponible, idproveedor))
    conexion.commit()
    conexion.close()

def insertar_proveedor(proveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO proveedor(proveedor) VALUES (%s)",
        (proveedor))
    conexion.commit()
    conexion.close()

def insertar_pedido(fechapedido, estadopedido, idproducto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO pedidos(fechapedido, estadopedido, idproducto) VALUES (%s, %s, %s)",
        (fechapedido, estadopedido, idproducto))
    conexion.commit()
    with conexion.cursor() as cursor:
        cursor.execute("CALL restar_stock(%s)",
        (idproducto))
    conexion.commit()
    conexion.close()

def insertar_enpr(fechaentrega, idproveedor, idproducto, cantidad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO entregaproveedor(fechaentrega, idproveedor, idproducto, cantidad) VALUES (%s, %s, %s,%s)",
        (fechaentrega, idproveedor, idproducto, cantidad))
    conexion.commit()
    with conexion.cursor() as cursor:
        cursor.execute("CALL aumentar_stock(%s, %s)",
        (idproducto, cantidad))
    conexion.commit()
    conexion.close()

def obtener_producto():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM vista_productos")
        productos = cursor.fetchall()
    conexion.close()
    return productos
def obtener_producto_activos():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idproducto, descripcion, precio, stock, disponible, idproveedor FROM productos WHERE disponible=1")
        productos = cursor.fetchall()
    conexion.close()
    return productos

def obtener_producto_todos():
    conexion = obtener_conexion()
    productos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idproducto, descripcion, precio, stock, disponible, idproveedor FROM productos")
        productos = cursor.fetchall()
    conexion.close()
    return productos
def obtener_proveedor():
    conexion = obtener_conexion()
    proveedor = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idproveedor, proveedor FROM proveedor")
        proveedor = cursor.fetchall()
    conexion.close()
    return proveedor

def obtener_pedido():
    conexion = obtener_conexion()
    pedidos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM vista_pedidos;")
        pedidos = cursor.fetchall()
    conexion.close()
    return pedidos

def obtener_enpr():
    conexion = obtener_conexion()
    entregas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM vista_entregas")
        entregas = cursor.fetchall()
    conexion.close()
    return entregas

def eliminar_productos(idproducto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE idproducto = %s", (idproducto,))
    conexion.commit()
    conexion.close()

def eliminar_proveedor(idproveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM proveedor WHERE idproveedor = %s", (idproveedor,))
    conexion.commit()
    conexion.close()

def eliminar_pedido(idpedido):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM pedidos WHERE idpedido = %s", (idpedido,))
    conexion.commit()
    conexion.close()

def eliminar_enpr(identrega):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM entregaproveedor WHERE identrega = %s", (identrega,))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(idproducto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM productos WHERE idproducto = %s", (idproducto,))
        producto = cursor.fetchone()
    return producto

def obtener_proveedor_por_id(idproveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM proveedor WHERE idproveedor = %s", (idproveedor,))
        proveedor = cursor.fetchone()
    return proveedor

def obtener_pedido_por_id(idpedido):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM pedidos WHERE idpedido = %s", (idpedido,))
        pedidos = cursor.fetchone()
    return pedidos

def obtener_enpr_por_id(identrega):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM entregaproveedor WHERE identrega = %s", (identrega,))
        entregas = cursor.fetchone()
    return entregas

def actualizar_producto(idproducto, descripcion, precio, stock, disponible, idproveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE productos SET descripcion = %s, precio = %s, stock = %s, disponible = %s, idproveedor = %s WHERE idproducto = %s",
        (descripcion, precio, stock, disponible, idproveedor, idproducto))
    conexion.commit()
    conexion.close()

def actualizar_proveedor(idproveedor, proveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE proveedor SET proveedor = %s  WHERE idproveedor = %s",
        (proveedor, idproveedor))
    conexion.commit()
    conexion.close()

def actualizar_pedido(idpedido, fechapedido, estadopedido, idproducto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE pedidos SET fechapedido = %s, estadopedido = %s, idproducto = %s WHERE idpedido = %s",
        (fechapedido, estadopedido, idproducto, idpedido))
    conexion.commit()
    conexion.close()

def actualizar_enpr(identrega, fechaentrega, idproveedor, idproducto, cantidad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE entregaproveedor SET fechaentrega = %s, idproveedor = %s, idproducto = %s, cantidad = %s WHERE identrega = %s",
        (fechaentrega, idproveedor, idproducto, cantidad, identrega))
    conexion.commit()
    conexion.close()