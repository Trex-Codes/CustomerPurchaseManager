CREATE DATABASE Biblioteca_DB;
USE biblioteca_db;

CREATE TABLE libros (
	codigo_libro_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre_libro VARCHAR(500) NOT NULL,
    editorial VARCHAR(500) NOT NULL, 
    autor VARCHAR(300) NOT NULL, 
    genero VARCHAR(100) NOT NULL, 
    pais_autor VARCHAR(100) NOT NULL,
    numero_paginas INT NOT NULL,
    año_edicion YEAR NOT NULL,
    PRECIO_LIBRO DECIMAL NOT NULL
);

CREATE TABLE prestamos (
num_prestamos_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
codigo_libro INT NOT NULL,
codigo_usuario INT NOT NULL,
fecha_salida TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
fecha_devolucion TIMESTAMP NOT NULL,
fecha_maxima_devolucion TIMESTAMP NOT NULL
);

CREATE TABLE usuarios (
	codigo_usuarios_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(200) NOT NULL,
    apellidos VARCHAR(200) NOT NULL,
    DNI VARCHAR(50) NOT NULL,
    domicilio VARCHAR(500) NOT NULL,
    departamento VARCHAR(500) NOT NULL,
    ciudad VARCHAR(500) NOT NULL,
    fecha_nacimiento DATE NOT NULL
);


INSERT INTO libros (nombre_libro, editorial, autor, genero, pais_autor, numero_paginas, año_edicion, precio_libro)
VALUES 
	("Don Quijote de La Mancha I", "Anaya", "Miguel de Cervantes", "caballeresco", "España", 611, 1991, 2750),
	("Don Quijote de La Mancha II", "Anaya", "Miguel de Cervantes", "caballeresco", "España", 611, 1991, 3125),
	("Historias de Nueva Orleans", "Alfaguara", "Wiliam Faulkner", "Novela", "Estados Unidos", 186, 1985, 675),
	("El principito", "Andina", "Antoine Saint-Exupery", "Aventura", "Francia", 120, 1996, 750),
	("El principe", "S.M.", "Maquiavelo", "Político", "Italia", 210, 1995, 1125),
	("Diplomacia", "S.M.", "Henry Kissinger", "Político", "Alemania", 825, 1997, 1750),
	("Los Windsor", "Plaza & janés", "Kitty Kelley", "Biografías", "Gran Bretaña", 620, 1998, 1130),
	("EL Último Emperador", "Caralt", "Pu-Yi", "Autobiografía", "China", 353, 1989, 995),
	("Fortunata y Jacinta", "Plaza & janés", "Pérez Galdós", "Novela", "España", 625, 1984, 725);
    
    INSERT INTO usuarios (nombres, apellidos, DNI, domicilio, Departamento, Ciudad, fecha_nacimiento)
VALUES 
	-- ("Inés del Zocorro", "Posadas Gil", "36.191.887", "AV. Escaleritas 12", "César", "Valledupar", "1971-07-04");
	("José Felipe", "Sánchez Pons", "12.158.254", "Mesa y López 51", "Caldas", "manizales", "1966-09-06"),
	("Miguel Chavarria", "Gómez Saéz", "1003.254.684", "Gran via 71", "Cundinamarca", "Bogotá", "1976-12-09"),
	("Eva Maria", "Santana Páez", "95.244.105", "Pio Baroja 23", "Cundinamarca", "Bogotá", "1980-05-23"),
	("Yolanda Serrano", "Betancour Díaz", "1232.254.244", "El Cid 45", "Amazonas", "Leticia", "2004-05-13"),
	("juan Luis", "Blasco Pita", "87.542.254", "Jaime I, 65", "Huila", "Neiva", "2013-12-31");
    
    INSERT INTO prestamos (codigo_libro, codigo_usuario, fecha_salida, fecha_devolucion, fecha_maxima_devolucion)
VALUES 
	(1, 1, "2024-04-22 10:34:23", "2024-04-27 10:34:23", "2024-04-27 10:34:23"),
    (2, 3, '2024-05-01 09:15:00', '2024-05-06 09:15:00', '2024-05-06 09:15:00'),
    (5, 2, '2024-06-15 14:45:00', '2024-06-20 14:45:00', '2024-06-20 14:45:00'),
    (7, 4, '2024-07-10 11:20:00', '2024-07-15 11:20:00', '2024-07-15 11:20:00'),
    (3, 1, '2024-08-05 16:30:00', '2024-08-10 16:30:00', '2024-08-10 16:30:00'),
    (9, 6, '2024-09-12 08:00:00', '2024-09-17 08:00:00', '2024-09-17 08:00:00'),
    (1, 2, '2024-09-12 08:00:00', '2024-09-17 08:00:00', '2024-09-17 08:00:00'),
	(1, 3, "2024-04-22 10:34:23", "2024-04-27 10:34:23", "2024-04-27 10:34:23");	



-- Relation 1:N Libros.codigo_libro_id:prestamos.codigo_libro

ALTER TABLE prestamos 
ADD CONSTRAINT fk_librosPrestamos
FOREIGN KEY (codigo_libro) REFERENCES libros(codigo_libro_id);
	
-- UNIQUE prestamos.codigo_libro:prestamos.codigo_usuario

ALTER TABLE prestamos 
ADD CONSTRAINT uc_libro_usuario UNIQUE(codigo_libro, codigo_usuario);

-- Relation 1:N usuarios.codigo_usuario_id_prestamos:codigo_usuario

ALTER TABLE prestamos
ADD CONSTRAINT fk_usuariosPrestamos
FOREIGN KEY(codigo_usuario) REFERENCES usuarios(codigo_usuarios_id);


-- QUERYS

-- 1. Query books that were borrowed in November during any year

SELECT 
	codigo_libro,
    nombre_libro,
    fecha_salida
FROM prestamos 
JOIN libros ON prestamos.codigo_libro = libros.codigo_libro_id
WHERE fecha_salida LIKE "%-04-%";

-- 2. Number of times a book has been borrowed by its name and the quantity of times it has been borrowed

SELECT 
    codigo_libro,
    nombre_libro,
    COUNT(prestamos.codigo_libro) AS "CANTIDAD DE VECES SOLICITADO"
FROM prestamos
JOIN libros ON prestamos.codigo_libro = libros.codigo_libro_id
GROUP BY nombre_libro, codigo_libro;

-- 3. Books that each user has requested

SELECT 
	usuarios.nombres,
    COUNT(prestamos.codigo_libro) AS "LIBROS SOLICITADOS POR USUARIOS"
FROM prestamos 
JOIN libros ON prestamos.codigo_libro = libros.codigo_libro_id
JOIN usuarios ON prestamos.codigo_usuario = usuarios.codigo_usuarios_id
GROUP BY usuarios.nombres;

SELECT 
	usuarios.codigo_usuarios_id,
	usuarios.nombres,
    libros.nombre_libro AS "LIBROS SOLICITADOS POR USUARIOS"
FROM prestamos 
JOIN libros ON prestamos.codigo_libro = libros.codigo_libro_id
JOIN usuarios ON prestamos.codigo_usuario = usuarios.codigo_usuarios_id
ORDER BY usuarios.codigo_usuarios_id ASC;

-- 4. Total number of pages read by a user

SELECT 
	usuarios.nombres,
    COUNT(prestamos.codigo_libro) AS "LIBROS SOLICITADOS POR USUARIOS",
    SUM(libros.numero_paginas) AS "CANTIDAD DE PAGINAS LEIDAS EN TOTAL"
FROM prestamos 
JOIN libros ON prestamos.codigo_libro = libros.codigo_libro_id
JOIN usuarios ON prestamos.codigo_usuario = usuarios.codigo_usuarios_id
GROUP BY usuarios.nombres;

-- 5. Number of books read by departments

SELECT 
	usuarios.departamento,
    COUNT(prestamos.codigo_libro) AS "LIBROS LEIDOS"
FROM prestamos 
JOIN libros ON prestamos.codigo_libro = libros.codigo_libro_id
JOIN usuarios ON prestamos.codigo_usuario = usuarios.codigo_usuarios_id
GROUP BY usuarios.departamento;

-- 6. Books read by each month 

SELECT 
	prestamos.fecha_salida,
    COUNT(prestamos.fecha_salida) AS "Cantidad por meses"
FROM prestamos 
JOIN libros ON prestamos.codigo_libro = libros.codigo_libro_id
JOIN usuarios ON prestamos.codigo_usuario = usuarios.codigo_usuarios_id
GROUP BY prestamos.fecha_salida;

-- Number of books by authors

SELECT 
	libros.autor,
    COUNT(prestamos.codigo_libro)
FROM prestamos 
JOIN libros ON prestamos.codigo_libro = libros.codigo_libro_id
JOIN usuarios ON prestamos.codigo_usuario = usuarios.codigo_usuarios_id
GROUP BY libros.autor;

-- All information share through all the tables 

USE biblioteca_db;
SELECT * 
FROM prestamos
LEFT JOIN usuarios
ON prestamos.codigo_usuario = usuarios.codigo_usuarios_id
UNION
SELECT * 
FROM prestamos
RIGHT JOIN usuarios
ON prestamos.codigo_usuario = usuarios.codigo_usuarios_id;