CREATE TABLE Course(
    name VARCHAR(100) SERIAL PRIMARY KEY,
    start_time TIME,
    end_time TIME,
    room INT
);

CREATE TABLE Department(
    name VARCHAR(100) SERIAL PRIMARY KEY,
    office VARCHAR(100)
);

CREATE TABLE Enrolled (
    student INT SERIAL PRIMARY KEY,
    course VARCHAR(100) SERIAL PRIMARY KEY,
    credit_status VARCHAR(100),
);






















CREATE TABLE Student (
   id INT SERIAL PRIMARY KEY, 
   name VARCHAR(100),
);









