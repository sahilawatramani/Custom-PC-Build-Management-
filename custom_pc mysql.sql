CREATE DATABASE PC_BUILD;
USE PC_BUILD;

CREATE TABLE CPU (
	CPU_ID INT AUTO_INCREMENT PRIMARY KEY,
    BRAND VARCHAR(10),
    MODEL VARCHAR(50),
    CORES INT,
    BASE_CLOCK FLOAT,
    PRICE DECIMAL(10,2)
);
SELECT * FROM CPU;

CREATE TABLE GPU (
	GPU_ID INT AUTO_INCREMENT PRIMARY KEY,
    BRAND VARCHAR(10),
    MODEL VARCHAR(50),
    VRAM INT,
    PRICE DECIMAL(10,2)
);
SELECT * FROM GPU;

CREATE TABLE POWER_SUPPLY (
	PSU_ID INT AUTO_INCREMENT PRIMARY KEY,
    BRAND VARCHAR(10),
    WATTAGE INT,
    EFFICIENCY VARCHAR(30),
    PRICE DECIMAL(10,2)
);
SELECT * FROM POWER_SUPPLY;

CREATE TABLE RAM (
	RAM_ID INT AUTO_INCREMENT PRIMARY KEY,
    BRAND VARCHAR(10),
    CAPACITY INT,
    SPEED INT,
    PRICE DECIMAL(10,2)
);
SELECT * FROM RAM;

CREATE TABLE STORAGE (
	STR_ID INT AUTO_INCREMENT PRIMARY KEY,
    BRAND VARCHAR(10),
    TYPE VARCHAR(5),
    CAPACITY INT,
    PRICE DECIMAL(10,2)
);
SELECT * FROM STORAGE;

CREATE TABLE MOTHERBOARD (
	MB_ID INT AUTO_INCREMENT PRIMARY KEY,
    BRAND VARCHAR(10),
    CHIPSET VARCHAR(10),
    FORM_FACTOR VARCHAR(15),
    PRICE DECIMAL(10,2)
);
SELECT * FROM MOTHERBOARD;

CREATE TABLE MONITOR (
	MON_ID INT AUTO_INCREMENT PRIMARY KEY,
    BRAND VARCHAR(10),
    RESOLUTION VARCHAR(10),
    SIZE INT,
    IS_4K VARCHAR(6),
    PRICE DECIMAL(10,2)
);
SELECT * FROM MONITOR;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
SELECT * FROM users;

CREATE TABLE PC_BUILD (
	BUILD_ID INT AUTO_INCREMENT PRIMARY KEY,
	CPU_ID INT,
		FOREIGN KEY(CPU_ID) REFERENCES CPU(CPU_ID),
	GPU_ID INT,
		FOREIGN KEY(GPU_ID) REFERENCES GPU(GPU_ID),
	RAM_ID INT,
		FOREIGN KEY(RAM_ID) REFERENCES RAM(RAM_ID),
	PSU_ID INT,
		FOREIGN KEY(PSU_ID) REFERENCES POWER_SUPPLY(PSU_ID),
	MON_ID INT,
		FOREIGN KEY(MON_ID) REFERENCES MONITOR(MON_ID),
	MB_ID INT,
		FOREIGN KEY(MB_ID) REFERENCES MOTHERBOARD(MB_ID),
	STR_ID INT,
		FOREIGN KEY(STR_ID) REFERENCES STORAGE(STR_ID),
    TOTAL_PRICE DECIMAL(10,2)
);
SELECT * FROM PC_BUILD;