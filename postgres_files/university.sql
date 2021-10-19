CREATE TABLE Enrolled (
    student SERIAL PRIMARY KEY,
    course SERIAL UNIQUE,
    credit_status VARCHAR(100),
    FOREIGN KEY (student) REFERENCES Room(id),
    FOREIGN KEY (course) REFERENCES Course(name)
);

CREATE TABLE MajorsIn(
    student SERIAL PRIMARY KEY,
    dept SERIAL UNIQUE,
    FOREIGN KEY (student) REFERENCES Student(id),
    FOREIGN KEY (dept) REFERENCES Department(name)
);

