CREATE TABLE productos(
idproducto INT UNSIGNED NOT NULL,
descripcion varchar(200) NOT NULL,
precio float NOT NULL,
stock INT UNSIGNED NOT NULL,
disponible BOOLEAN,
idproveedor INT UNSIGNED NOT NULL,
PRIMARY KEY(idproducto)
);