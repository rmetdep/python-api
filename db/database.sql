CREATE DATABASE IF NOT EXISTS api;
USE api;
CREATE TABLE IF NOT EXISTS driver (
  driverId int(11) NOT NULL AUTO_INCREMENT,
  driverName varchar(50) DEFAULT NULL,
  PRIMARY KEY (driverId)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS team (
  teamId int(11) NOT NULL AUTO_INCREMENT,
  teamName varchar(50) DEFAULT NULL,
  PRIMARY KEY (teamId)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS circuits (
  circuitId int(11) NOT NULL AUTO_INCREMENT,
  circuitName varchar(50) DEFAULT NULL,
  PRIMARY KEY (circuitId)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
INSERT INTO driver (driverName) VALUES ('Lewis Hamilton');
INSERT INTO driver (driverName) VALUES ('Valtteri Bottas');
INSERT INTO driver (driverName) VALUES ('Sebastian Vettel');
INSERT INTO driver (driverName) VALUES ('Kimi Raikkonen');
INSERT INTO driver (driverName) VALUES ('Max Verstappen');
INSERT INTO driver (driverName) VALUES ('Daniel Ricciardo');
INSERT INTO driver (driverName) VALUES ('Sergio Perez');
INSERT INTO driver (driverName) VALUES ('Esteban Ocon');
INSERT INTO driver (driverName) VALUES ('Nico Hulkenberg');
INSERT INTO driver (driverName) VALUES ('Carlos Sainz');
INSERT INTO driver (driverName) VALUES ('Lance Stroll');
INSERT INTO driver (driverName) VALUES ('Stoffel Vandoorne');
INSERT INTO driver (driverName) VALUES ('Kevin Magnussen');
INSERT INTO driver (driverName) VALUES ('Romain Grosjean');
INSERT INTO driver (driverName) VALUES ('Fernando Alonso');
INSERT INTO driver (driverName) VALUES ('Brendon Hartley');
INSERT INTO driver (driverName) VALUES ('Sergey Sirotkin');
INSERT INTO driver (driverName) VALUES ('Charles Leclerc');
INSERT INTO driver (driverName) VALUES ('Pierre Gasly');
INSERT INTO driver (driverName) VALUES ('Marcus Ericsson');
INSERT INTO driver (driverName) VALUES ('Lando Norris');
INSERT INTO driver (driverName) VALUES ('Antonio Giovinazzi');
INSERT INTO driver (driverName) VALUES ('Alexander Albon');
INSERT INTO driver (driverName) VALUES ('Daniil Kvyat');
INSERT INTO driver (driverName) VALUES ('George Russell');
INSERT INTO driver (driverName) VALUES ('Robert Kubica');
INSERT INTO team (teamName) VALUES ('Mercedes');
INSERT INTO team (teamName) VALUES ('Ferrari');
INSERT INTO team (teamName) VALUES ('Red Bull');
INSERT INTO team (teamName) VALUES ('Renault');
INSERT INTO team (teamName) VALUES ('Haas');
INSERT INTO team (teamName) VALUES ('McLaren');
INSERT INTO circuits (circuitName) VALUES ('Melbourne');
INSERT INTO circuits (circuitName) VALUES ('Shanghai');
INSERT INTO circuits (circuitName) VALUES ('Bahrain');
INSERT INTO circuits (circuitName) VALUES ('Catalunya');
INSERT INTO circuits (circuitName) VALUES ('Monaco');