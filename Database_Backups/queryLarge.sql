SELECT
	cliente.cliente_id,
    cliente.nombre,
    venta.cantidad,  
    venta_producto.venta_id AS "ID VENTA venta_producto",
    venta_producto.producto_id AS "ID PRODUCTO venta_producto",
    producto.descripcion,
    producto.tipo_producto,
    categoria,
    producto.precio,
    SUM(producto.precio * venta.cantidad) AS "VALOR PAGADO"
FROM cliente 
JOIN venta ON cliente.cliente_id = venta.cliente_id
JOIN venta_producto ON venta.venta_id = venta_producto.venta_id
JOIN producto ON venta_producto.producto_id = producto.producto_id
JOIN tipo_producto ON tipo_producto.tipo_producto_id = producto.tipo_producto
WHERE cliente.cliente_id = 1
GROUP BY 
    cliente.cliente_id,
    cliente.nombre,
    venta_producto.venta_id,
    venta_producto.producto_id,
    producto.descripcion,
    producto.tipo_producto,
    tipo_producto.categoria,
    producto.precio;