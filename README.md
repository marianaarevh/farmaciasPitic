# farmaciasPitic
El proyecto se esta manejando en un entorno virtual por lo que para que funcione se debe instalar
pip install Flask
pip instal pymysql
para crear un entorno vitual y trabajar en el recomiento ver la siguiente pagina:
https://www.programaenpython.com/miscelanea/crear-entornos-virtuales-en-python/
NOTA: para activar el entorno virtual en visual studio code debes de estar en la carpeta donde creaste el entorno virtual y posteriormente acctivarlo con el siguiente
comando: .\scripts\activate
NOTA2: para correr correctamente el programa es python main.py(main.py es el nombre de la clase principal puedes cambiarle el nombre pero siempre debes correrlo como 
python ___.py
Se nececita crear una base de datos de la siguiente manera:
CREATE DATABASE opticapitic;
USE opticapitic;

posteriormente se crean las tablas:
CREATE TABLE proveedor(
idproveedor INT UNSIGNED NOT NULL,
proveedor varchar(50) NOT NULL,
PRIMARY KEY(idproveedor)
);

CREATE TABLE productos(
idproducto INT UNSIGNED NOT NULL,
descripcion varchar(200) NOT NULL,
precio float NOT NULL,
stock INT UNSIGNED NOT NULL,
disponible BOOLEAN,
idproveedor INT UNSIGNED NOT NULL,
PRIMARY KEY(idproducto)
);

CREATE TABLE pedidos(
idPedido INT UNSIGNED NOT NULL,
fechapedido varchar(50) NOT NULL,
estadopedido varchar(20) NOT NULL,
idproducto INT UNSIGNED NOT NULL,
PRIMARY KEY(idpedido)
);

CREATE TABLE entregaproveedor(
identrega INT UNSIGNED NOT NULL,
fechaentrega varchar(50) NOT NULL,
idproveedor INT UNSIGNED NOT NULL,
idproducto INT UNSIGNED NOT NULL,
cantidad INT UNSIGNED NOT NULL,
PRIMARY KEY(identrega)
);

Luego se agregan proveedores a la tabla ya que no es posible agregar productos si no existen proveedores.
INSERT INTO proveedor (idproveedor, proveedor)
VALUES
  (1, 'Eyewear Inc.'),
  (2, 'Glasses Direct'),
  (3, 'Vision Express'),
  (4, 'LensCrafters'),
  (5, 'Sunglass Hut');
 
Y luego agregamos productos para que el programa tenga cosas que reflejar y verifiquemos que se estan jalando los datos correctamente
INSERT INTO productos (idproducto, descripcion, precio, stock, disponible, idproveedor)
VALUES
  (1, 'Lentes de lectura', 25.99, 50, true, 1),
  (2, 'Gafas de sol', 69.99, 20, true, 1),
  (3, 'Lentes de contacto', 35.50, 100, true, 1),
  (4, 'Lentes de armazón', 99.99, 10, true, 1),
  (5, 'Líquido para lentes de contacto', 12.50, 200, true, 1);

