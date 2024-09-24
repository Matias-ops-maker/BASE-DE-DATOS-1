CREATE TABLE `Socios` (
  `id_socio` INT PRIMARY KEY,
  `nombre` VARCHAR(100),
  `direccion` VARCHAR(255)
);

CREATE TABLE `Barcos` (
  `matricula` VARCHAR(20) PRIMARY KEY,
  `nombre` VARCHAR(100),
  `numero_amarre` INT,
  `cuota` DECIMAL(10,2),
  `id_socio` INT
);

CREATE TABLE `Salidas` (
  `id_salida` INT PRIMARY KEY,
  `matricula` VARCHAR(20),
  `fecha_salida` DATE,
  `hora_salida` TIME,
  `destino` VARCHAR(100),
  `patron_nombre` VARCHAR(100),
  `patron_direccion` VARCHAR(255)
);

ALTER TABLE `Barcos` ADD FOREIGN KEY (`id_socio`) REFERENCES `Socios` (`id_socio`);

ALTER TABLE `Salidas` ADD FOREIGN KEY (`matricula`) REFERENCES `Barcos` (`matricula`);
