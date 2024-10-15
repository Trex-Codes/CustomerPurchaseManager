CREATE DATABASE company;
USE company;

CREATE TABLE cliente(
	cliente_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad VARCHAR(100) NOT NULL,
    telefono VARCHAR(40), 
    email VARCHAR(100),
    ciudad VARCHAR(50) NOT NULL,
    direccion VARCHAR(500) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE venta (
	venta_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    cantidad INT NOT NULL
);

CREATE TABLE producto (
	producto_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo_producto INT NOT NULL, 
    descripcion VARCHAR(200) NOT NULL,
    precio DECIMAL NOT NULL
);

CREATE TABLE tipo_producto (
	tipo_producto_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	categoria VARCHAR(50)
);

CREATE TABLE venta_producto (
	venta_producto_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    venta_id INT NOT NULL,
    producto_id INT NOT NULL,
    UNIQUE(venta_id, producto_id)
);


-- RELATIONSHIPS SQL

-- 1. cliente:venta
ALTER TABLE venta 
ADD CONSTRAINT fk_cliente_id 
FOREIGN KEY(cliente_id) REFERENCES cliente(cliente_id);

-- 2. venta_producto:venta
ALTER TABLE venta_producto
ADD CONSTRAINT fk_ventaProducto_venta_id
FOREIGN KEY (venta_id) REFERENCES venta (venta_id);

-- 3. venta_producto:producto
ALTER TABLE venta_producto
ADD CONSTRAINT fk_ventaProducto_producto_id
FOREIGN KEY (producto_id) REFERENCES producto(producto_id);

-- 4. producto:tipo_producto
ALTER TABLE producto
ADD CONSTRAINT fk_producto_tipoProducto
FOREIGN KEY(tipo_producto) REFERENCES tipo_producto(tipo_producto_id);
    
    