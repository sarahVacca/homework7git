CREATE TABLE Course(
    name VARCHAR(100) SERIAL PRIMARY KEY,
    start_time TIME,
    end_time TIME,
    room INT,
    FOREIGN KEY (room) REFERENCES Room(id)
);

CREATE TABLE Department(
    name VARCHAR(100) SERIAL PRIMARY KEY,
    office VARCHAR(100)
);

CREATE TABLE Enrolled (
    student INT SERIAL PRIMARY KEY,
    course VARCHAR(100) SERIAL PRIMARY KEY,
    credit_status VARCHAR(100),
    FOREIGN KEY (student) REFERENCES Room(id),
    FOREIGN KEY (course) REFERENCES Course(name)

CREATE TABLE MajorsIn(
    student INT SERIAL PRIMARY KEY,
    dept VARCHAR(100) SERIAL PRIMARY KEY
    FOREIGN KEY (student) REFERENCES Student(id)
    FOREIGN KEY (dept) REFERENCES Department(name)
);











CREATE TABLE Room (
    id INT SERIAL PRIMARY KEY,
    name VARCHAR(100),
    capacity INT,
);



















