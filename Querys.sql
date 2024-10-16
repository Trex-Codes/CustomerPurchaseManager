SELECT * FROM cliente;
SELECT * FROM tipo_producto;
SELECT * FROM producto;
SELECT * FROM venta;
SELECT * FROM venta_producto;

SELECT * 
FROM venta_producto
JOIN venta ON venta_producto.venta_id = venta.venta_id
JOIN producto ON venta_producto.producto_id = producto.producto_id; 

SELECT
	cliente.cliente_id,
    cliente.nombre,
    cliente.edad,
    cliente.ciudad,
    
    venta.venta_id AS "VENTA ID",
    venta.cliente_id AS "VENTA CLIENTE ID",
    venta.cantidad,
    
    producto.producto_id,
    producto.tipo_producto,
    producto.descripcion,
    producto.precio
FROM cliente 
JOIN venta ON cliente.cliente_id = venta.cliente_id
JOIN venta_producto ON venta.venta_id = venta_producto.venta_id
JOIN producto ON venta_producto.producto_id = producto.producto_id;