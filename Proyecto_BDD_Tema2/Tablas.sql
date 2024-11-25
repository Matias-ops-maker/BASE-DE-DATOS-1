DROP DATABASE IF EXISTS VentasOnline;
CREATE DATABASE VentasOnline;
USE VentasOnline;

DROP TABLE IF EXISTS Ordenes;
DROP TABLE IF EXISTS Clientes;
DROP TABLE IF EXISTS Productos;
DROP TABLE IF EXISTS Categorias;

CREATE TABLE Categorias(
	id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(255) NOT NULL
);

CREATE TABLE Productos(
	id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre_producto VARCHAR(255) NOT NULL UNIQUE,
    precio DOUBLE NOT NULL,
    id_categoria INT NOT NULL,
    cantidad_stock INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria) 
    ON DELETE RESTRICT 
    ON UPDATE CASCADE
);

CREATE TABLE Clientes(
	id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre_cliente VARCHAR(255) NOT NULL,
    apellido_cliente VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL
);

CREATE TABLE Ordenes(
	id_orden INT PRIMARY KEY AUTO_INCREMENT,
    id_producto INT,
    id_cliente INT,
    fecha DATE NOT NULL,
    cantidad_unidades INT NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto) 
		ON DELETE RESTRICT 
		ON UPDATE CASCADE,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente) 
		ON DELETE RESTRICT
        ON UPDATE CASCADE
);

INSERT INTO Categorias (nombre_categoria) VALUES 
('Electrónica'),
('Accesorios'),
('Moda'),
('Oficina');

INSERT INTO Productos (nombre_producto, precio, id_categoria, cantidad_stock) VALUES 
('Laptop', 1200.00, 1, 50),
('Smartphone', 800.00, 1, 100),
('Auriculares', 50.00, 2, 200),
('Teclado', 30.00, 2, 150),
('Monitor', 300.00, 1, 75),
('Mochila', 40.00, 3, 120),
('Reloj Inteligente', 150.00, 1, 90),
('Cargador', 20.00, 2, 300),
('Mouse', 25.00, 2, 250),
('Impresora', 200.00, 4, 60);

INSERT INTO Clientes (nombre_cliente, apellido_cliente, direccion) VALUES 
('Juan', 'Pérez', 'Calle Falsa 123'),
('María', 'López', 'Av. Libertador 456'),
('Carlos', 'Gómez', 'Calle 25 de Mayo 789'),
('Ana', 'Martínez', 'Av. Belgrano 101'),
('Luis', 'Hernández', 'Calle San Martín 202'),
('Sofía', 'García', 'Av. Córdoba 303'),
('Pedro', 'Ramírez', 'Calle Rivadavia 404'),
('Laura', 'Sánchez', 'Calle Sarmiento 505'),
('Miguel', 'Fernández', 'Av. Santa Fe 606'),
('Andrea', 'Castro', 'Calle Corrientes 707');

INSERT INTO Ordenes (id_producto, id_cliente, fecha, cantidad_unidades) VALUES
(5, 1, '2024-11-06', 1),
(6, 1, '2024-11-06', 2),
(9, 1, '2024-11-14', 3),
(6, 1, '2024-11-09', 3),
(7, 1, '2024-11-13', 2),
(9, 1, '2024-11-09', 4),
(2, 1, '2024-11-05', 5),
(4, 1, '2024-11-29', 4),
(7, 1, '2024-11-12', 5),
(6, 1, '2024-11-12', 2),
(3, 1, '2024-11-22', 1),
(7, 1, '2024-11-27', 4),
(10, 2, '2024-11-20', 1),
(10, 2, '2024-11-26', 4),
(5, 2, '2024-11-21', 1),
(8, 2, '2024-11-24', 4),
(4, 2, '2024-11-08', 4),
(8, 3, '2024-11-14', 4),
(4, 3, '2024-11-25', 5),
(2, 3, '2024-11-09', 3),
(8, 3, '2024-11-25', 1),
(4, 3, '2024-11-28', 1),
(8, 3, '2024-11-24', 4),
(2, 3, '2024-11-27', 1),
(3, 3, '2024-11-05', 1),
(1, 3, '2024-11-23', 2),
(3, 3, '2024-11-26', 4),
(3, 3, '2024-11-30', 1),
(7, 3, '2024-11-19', 2),
(8, 3, '2024-11-19', 1),
(3, 3, '2024-11-11', 1),
(2, 3, '2024-11-25', 1),
(5, 4, '2024-11-30', 2),
(1, 4, '2024-11-07', 4),
(5, 4, '2024-11-20', 2),
(3, 4, '2024-11-18', 5),
(10, 4, '2024-11-26', 1),
(9, 4, '2024-11-30', 1),
(8, 4, '2024-11-15', 2),
(5, 4, '2024-11-24', 4),
(7, 4, '2024-11-21', 3),
(2, 4, '2024-11-08', 2),
(7, 4, '2024-11-18', 5),
(6, 4, '2024-11-23', 4),
(1, 4, '2024-11-27', 2),
(7, 4, '2024-11-25', 5),
(8, 4, '2024-11-18', 2),
(1, 5, '2024-11-22', 4),
(6, 5, '2024-11-10', 2),
(6, 5, '2024-11-11', 2),
(3, 5, '2024-11-08', 3),
(9, 5, '2024-11-05', 1),
(7, 5, '2024-11-20', 4),
(5, 5, '2024-11-19', 2),
(4, 5, '2024-11-14', 1),
(10, 5, '2024-11-23', 3),
(2, 5, '2024-11-11', 5),
(1, 5, '2024-11-24', 2),
(3, 5, '2024-11-18', 1),
(8, 5, '2024-11-26', 2),
(5, 6, '2024-11-03', 4),
(2, 6, '2024-11-16', 3),
(6, 6, '2024-11-07', 2),
(9, 6, '2024-11-12', 3),
(4, 6, '2024-11-14', 1),
(1, 6, '2024-11-25', 5),
(8, 6, '2024-11-02', 4),
(3, 6, '2024-11-09', 2),
(7, 6, '2024-11-28', 2),
(10, 6, '2024-11-05', 1),
(7, 7, '2024-11-13', 3),
(3, 7, '2024-11-17', 4),
(5, 7, '2024-11-08', 5),
(8, 7, '2024-11-23', 1),
(9, 7, '2024-11-10', 2),
(1, 7, '2024-11-15', 4),
(6, 7, '2024-11-12', 2),
(2, 7, '2024-11-21', 3),
(4, 7, '2024-11-27', 1),
(8, 7, '2024-11-30', 2),
(2, 8, '2024-11-11', 4),
(9, 8, '2024-11-04', 2),
(7, 8, '2024-11-06', 5),
(1, 8, '2024-11-09', 3),
(5, 8, '2024-11-24', 2),
(6, 8, '2024-11-10', 4),
(3, 8, '2024-11-19', 1),
(10, 8, '2024-11-22', 5),
(8, 8, '2024-11-16', 2),
(4, 8, '2024-11-18', 3),
(9, 9, '2024-11-14', 2),
(3, 9, '2024-11-17', 4),
(2, 9, '2024-11-23', 1),
(8, 9, '2024-11-11', 3),
(7, 9, '2024-11-21', 2),
(1, 9, '2024-11-28', 4),
(10, 9, '2024-11-26', 1),
(6, 9, '2024-11-30', 2),
(4, 9, '2024-11-05', 5),
(5, 9, '2024-11-07', 3),
(6, 10, '2024-11-01', 4),
(9, 10, '2024-11-10', 3),
(7, 10, '2024-11-15', 1),
(4, 10, '2024-11-20', 5),
(8, 10, '2024-11-24', 2),
(2, 10, '2024-11-13', 4),
(10, 10, '2024-11-19', 1),
(1, 10, '2024-11-16', 2),
(3, 10, '2024-11-29', 5),
(5, 10, '2024-11-27', 3);

CREATE INDEX idx_id_cliente ON Ordenes(id_cliente);
CREATE INDEX idx_id_cliente ON Clientes(id_cliente);