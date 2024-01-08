CREATE TABLE IF NOT EXISTS TRAIN (
  TRAIN_NUMBER INT,
  TRAIN_NAME VARCHAR(30) NOT NULL,
  PREMIUM_FAIR INT NOT NULL,
  GENERAL_FAIR INT NOT NULL,
  SOURCE_STATION VARCHAR(30) NOT NULL,
  DESTINATION_STATION VARCHAR(30) NOT NULL,
  PRIMARY KEY (TRAIN_NUMBER, TRAIN_NAME)
);

CREATE TABLE IF NOT EXISTS TRAIN_STATUS (
  TRAIN_DATE DATE NOT NULL,
  TRAIN_NAME VARCHAR(30),
  PREMIUM_SEATS_AVAILABLE INT NOT NULL,
  GENERAL_SEATS_AVAILABLE INT NOT NULL,
  PREMIUM_SEATS_OCCUPIED INT NOT NULL,
  GENERAL_SEATS_OCCUPIED INT NOT NULL,
  PRIMARY KEY (TRAIN_DATE, TRAIN_NAME)
  FOREIGN KEY (TRAIN_NAME) REFERENCES TRAIN(TRAIN_NAME)
);

CREATE TABLE IF NOT EXISTS PASSENGER (
  FIRST_NAME VARCHAR(30) NOT NULL,
  LAST_NAME VARCHAR(30) NOT NULL,
  ADDRESS VARCHAR(50) NOT NULL,
  CITY VARCHAR(30) NOT NULL,
  COUNTY VARCHAR(30) NOT NULL,
  PHONE CHAR(12) NOT NULL,
  SSN INT(9) PRIMARY KEY,
  BDATE DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS BOOKED (
  PASSENGER_SSN INT(9),
  TRAIN_NUMBER INT NOT NULL,
  TICKET_TYPE CHAR(7) NOT NULL,
  STATUS VARCHAR(6) NOT NULL,
  PRIMARY KEY (PASSENGER_SSN, TRAIN_NUMBER),
  FOREIGN KEY (PASSENGER_SSN) REFERENCES PASSENGER(SSN),
  FOREIGN KEY (TRAIN_NUMBER) REFERENCES TRAIN(TRAIN_NUMBER)
);

CREATE TABLE IF NOT EXISTS BOOKED_LOGS(
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  PASSENGER_SSN INT(9),
  TRAIN_NUMBER INT,
  TICKET_TYPE CHAR(7),
  STATUS VARCHAR(6)
);

CREATE TRIGGER IF NOT EXISTS DELETE_TICKET
AFTER DELETE
ON BOOKED
BEGIN
	UPDATE BOOKED
    SET STATUS = 'Booked'
    WHERE PASSENGER_SSN =
    (SELECT PASSENGER_SSN FROM BOOKED
     WHERE OLD.TRAIN_NUMBER = BOOKED.TRAIN_NUMBER
     AND OLD.TICKET_TYPE = BOOKED.TICKET_TYPE
     AND BOOKED.STATUS = 'WaitL'
     LIMIT 1);
END;

CREATE TRIGGER IF NOT EXISTS UPDATED_TICKETS
AFTER UPDATE ON BOOKED
BEGIN
	INSERT INTO BOOKED_LOGS (PASSENGER_SSN, TRAIN_NUMBER, TICKET_TYPE, STATUS)
    SELECT *
	FROM BOOKED B
	WHERE B.PASSENGER_SSN = NEW.PASSENGER_SSN
	AND B.TRAIN_NUMBER = NEW.TRAIN_NUMBER
	AND B.TICKET_TYPE = NEW.TICKET_TYPE
	AND OLD.STATUS = 'WaitL';
END;

INSERT INTO PASSENGER 
VALUES("James","Butt","6649 N Blue Gum St","New Orleans","Orleans","504-845-1427",264816896,"1968-10-10");
INSERT INTO PASSENGER 
VALUES("Josephine","Darakjy","4 B Blue Ridge Blvd","Brighton","Livingston","810-374-9840",240471168,"1975-11-01");
INSERT INTO PASSENGER 
VALUES("Art","Venere","8 W Cerritos Ave #54","Bridgeport","Gloucester","856-264-4130",285200976,"1982-11-13");
INSERT INTO PASSENGER 
VALUES("Lenna","Paprocki","639 Main St","Anchorage","Anchorage","907-921-2010",309323096,"1978-08-09");
INSERT INTO PASSENGER 
VALUES("Donette","Foller","34 Center St","Hamilton","Butler","513-549-4561",272610795,"1990-06-11");
INSERT INTO PASSENGER 
VALUES("Simona","Morasca","3 Mcauley Dr","Ashland","Ashland","419-800-6759",250951162,"1994-08-15");
INSERT INTO PASSENGER 
VALUES("Mitsue","Tollner","7 Eads St","Chicago","Cook","773-924-8565",272913578,"1984-07-04");
INSERT INTO PASSENGER 
VALUES("Leota","Dilliard","7 W Jackson Blvd","San Jose","Santa Clara","408-813-1105",268682534,"1991-05-09");
INSERT INTO PASSENGER 
VALUES("Sage","Wieser","5 Boston Ave #88","Sioux Falls","Minnehaha","605-794-4895",310908858,"1982-02-25");
INSERT INTO PASSENGER 
VALUES("Kris","Marrier","228 Runamuck Pl #2808","Baltimore","Baltimore City","410-804-4694",322273872,"1956-04-04");
INSERT INTO PASSENGER 
VALUES("Minna","Amigon","2371 Jerrold Ave","Kulpsville","Montgomery","215-422-8694",256558303,"1995-09-09");
INSERT INTO PASSENGER 
VALUES("Abel","Maclead","37275 St  Rt 17m M","Middle Island","Suffolk","631-677-3675",302548590,"1960-11-05");
INSERT INTO PASSENGER 
VALUES("Kiley","Caldarera","25 E 75th St #69","Los Angeles","Los Angeles","310-254-3084",284965676,"1981-05-09");
INSERT INTO PASSENGER 
VALUES("Graciela","Ruta","98 Connecticut Ave Nw","Chagrin Falls","Geauga","440-579-7763",277292710,"1982-02-25");
INSERT INTO PASSENGER 
VALUES("Cammy","Albares","56 E Morehead St","Laredo","Webb","956-841-7216",331160133,"1956-04-04");
INSERT INTO PASSENGER 
VALUES("Mattie","Poquette","73 State Road 434 E","Phoenix","Maricopa","602-953-6360",331293204,"1995-09-09");
INSERT INTO PASSENGER 
VALUES("Meaghan","Garufi","69734 E Carrillo St","Mc Minnville","Warren","931-235-7959",290123298,"1960-11-02");
INSERT INTO PASSENGER 
VALUES("Gladys","Rim","322 New Horizon Blvd","Milwaukee","Milwaukee","414-377-2880",286411536,"1991-05-09");
INSERT INTO PASSENGER 
VALUES("Yuki","Whobrey","1 State Route 27","Taylor","Wayne","313-341-4470",294860856,"1985-02-25");
INSERT INTO PASSENGER 
VALUES("Fletcher","Flosi","394 Manchester Blvd","Rockford","Winnebago","815-426-5657",317434088,"1961-04-04");

INSERT INTO TRAIN
VALUES (1, "Orient Express" ,800,600, "Paris", "Istanbul");
INSERT INTO TRAIN
VALUES (2, "Flying Scottsman",4000,3500, "Edinburgh", "London");
INSERT INTO TRAIN
VALUES (3, "Golden Arrow" ,980,860, "Victoria", "Dover");
INSERT INTO TRAIN
VALUES (4, "Golden Chariot",4300,3800, "Bangalore", "Goa");
INSERT INTO TRAIN
VALUES (5, "Maharaja Express",5980,4510, "Delhi", "Mumbai");

INSERT INTO BOOKED
VALUES(264816896, 3, "Premium", "Booked");
INSERT INTO BOOKED
VALUES (240471168,2,"General","Booked");
INSERT INTO BOOKED
VALUES (285200976,4,"Premium","Booked");
INSERT INTO BOOKED
VALUES (285200976,2,"Premium","Booked");
INSERT INTO BOOKED
VALUES (317434088,2,"Premium","Booked");
INSERT INTO BOOKED
VALUES (310908858,2,"General","Booked");
INSERT INTO BOOKED
VALUES (322273872,2,"General","Booked");
INSERT INTO BOOKED
VALUES (256558303,3,"Premium","WaitL");
INSERT INTO BOOKED
VALUES (302548590,2,"General","WaitL");
INSERT INTO BOOKED
VALUES (284965676,3,"Premium","WaitL");
INSERT INTO BOOKED
VALUES (277292710,3,"General","WaitL");
INSERT INTO BOOKED
VALUES (331160133,3,"General","WaitL");
INSERT INTO BOOKED
VALUES (331293204,3,"General","WaitL");
INSERT INTO BOOKED
VALUES (290123298,3,"General","WaitL");
INSERT INTO BOOKED
VALUES (286411536,4,"Premium","Booked");
INSERT INTO BOOKED
VALUES (294860856,4,"Premium","Booked");
INSERT INTO BOOKED
VALUES (317434088,4,"Premium","Booked");
INSERT INTO BOOKED
VALUES (310908858,4,"Premium","Booked");
INSERT INTO BOOKED
VALUES (322273872,4,"Premium","Booked");
INSERT INTO BOOKED
VALUES (256558303,4,"Premium","Booked");
INSERT INTO BOOKED
VALUES (302548590,4,"Premium","Booked");
INSERT INTO BOOKED
VALUES (284965676,4,"General","Booked");
INSERT INTO BOOKED
VALUES (277292710,4,"General","Booked");
INSERT INTO BOOKED
VALUES (331160133,4,"General","Booked");
INSERT INTO BOOKED
VALUES (331293204,4,"General","Booked");

INSERT INTO TRAIN_STATUS
VALUES ("2022-02-19", "Orient Express",10,10,0,0);
INSERT INTO TRAIN_STATUS
VALUES ("2022-02-20", "Flying Scottsman",8,5,2,5);
INSERT INTO TRAIN_STATUS
VALUES ("2022-02-21", "Maharaja Express",7,6,3,4);
INSERT INTO TRAIN_STATUS
VALUES ("2022-02-21", "Golden Chariot",6,3,4,7);
INSERT INTO TRAIN_STATUS
VALUES ("2022-02-22","Golden Arrow",8,7,2,3);
INSERT INTO TRAIN_STATUS
VALUES ("2022-03-10","Golden Arrow",8,5,2,5);
INSERT INTO TRAIN_STATUS
VALUES ("2022-02-20", "Maharaja Express",7,6,3,4);
INSERT INTO TRAIN_STATUS
VALUES ("2022-02-21", "Flying Scottsman",5,5,5,5);