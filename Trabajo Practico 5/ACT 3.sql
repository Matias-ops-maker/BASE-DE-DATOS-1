CREATE TABLE `Radios` (
  `radio` varchar(255),
  `año` int,
  `frecuencia_radio` varchar(255),
  `gerente` varchar(255),
  PRIMARY KEY (`radio`, `año`)
);

CREATE TABLE `Gerentes` (
  `gerente` varchar(255) PRIMARY KEY
);

CREATE TABLE `Programas` (
  `radio` varchar(255),
  `año` int,
  `programa` varchar(255),
  `conductor` varchar(255),
  `primary` key(radio,año,programa)
);

ALTER TABLE `Programas` ADD FOREIGN KEY (`radio`) REFERENCES `Radios` (`radio`);

ALTER TABLE `Programas` ADD FOREIGN KEY (`año`) REFERENCES `Radios` (`año`);
