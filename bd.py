import pymysql

def obtener_conexion():
    try:
        conexion = pymysql.connect(host='optica.pymehermosillo.com', user='pymeherm_optica', password='emFWzzU]{Ul#', db='pymeherm_optica')
        print("Conexión exitosa a la base de datos.")
        return conexion
    except pymysql.Error as error:
        print("Error al conectarse a la base de datos: ", error)
