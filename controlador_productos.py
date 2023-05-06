from bd import obtener_conexion

def insertar_producto(idproducto, descripcion, precio, stock, disponible, idproveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO productos(idproducto, descripcion, precio, stock, disponible, idproveedor) VALUES (%s, %s, %s,%s, %s, %s)",
        (idproducto, descripcion, precio, stock, disponible, idproveedor))
    conexion.commit()
    conexion.close()

def insertar_proveedor(idproveedor, proveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO proveedor(idproveedor,proveedor) VALUES (%s, %s)",
        (idproveedor, proveedor))
    conexion.commit()
    conexion.close()

def insertar_pedido(idpedido, fechapedido, estadopedido, idproducto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO pedidos(idpedido, fechapedido, estadopedido, idproducto) VALUES (%s, %s, %s, %s)",
        (idpedido, fechapedido, estadopedido, idproducto))
    conexion.commit()
    conexion.close()

def obtener_producto():
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
        cursor.execute("SELECT idpedido, fechapedido, estadopedido, idproducto FROM pedidos")
        pedidos = cursor.fetchall()
    conexion.close()
    return pedidos

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