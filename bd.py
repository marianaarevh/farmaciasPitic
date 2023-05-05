import pymysql

def obtener_conexion():
    try:
        conexion = pymysql.connect(host='localhost', user='root', password='', db='opticapitic')
        print("Conexión exitosa a la base de datos.")
        return conexion
    except pymysql.Error as error:
        print("Error al conectarse a la base de datos: ", error)
