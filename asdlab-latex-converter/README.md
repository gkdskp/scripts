# asdlab-latex-converter
Produces LaTeX code from the SQL source file

## Usage
```
python converter.py /path/to/sql/file.sql no_of_questions expt_num
```

## Example
Screenshots are assumed to be in the img/p{expt_num}/ folder with each file having the name ss{question_num}.png

**Sample .sql file**   
Questions must be inside the `/*..*/` block. Questions should start with question_num. followed by a space.
Syntax to the solution each answer must be seperated by an empty line. This applies for the last question too
```SQL
/*
1. Insert records into the employee table (Fields : EmpId, Ename,
Designation, Salary, Dept.id) created.

2. Display the details of all the employees.
3. Display the employee numbers, names and designation of all employees.
4. Suppose the emp_no 68454 has left the company. Delete the employee
from the database.
5. Suppose a new employee joins the company under department 2001 as
an analyst. The salary of the employee is not yet fixed. Add his record to
the database.
Emp_no Ename Designation Salary Dept.Id
66928 BLAZE MANAGER 55000 3001
67832 CLARE MANAGER 51000 1001
65646 JONAS MANAGER 59140 2001
67858 SCARLET ANALYST 62000 2001
69062 FRANK ANALYST 62000 2001
63679 SANDRINE CLERK 18000 2001
64989 ADELYN SALESMAN 34000 3001
65271 WADE SALESMAN 27000 3001
66564 MADDEN SALESMAN 27000 3001
68454 TUCKER SALESMAN 32000 3001
68736 ADNRES CLERK 24000 2001
69000 JULIUS CLERK 21000 3001
69324 MARKER CLERK 28000 1001
6. Find the details of employees with salary > 25000 working in department
*/

CREATE TABLE Employee(
	Emp_no INT(6) PRIMARY KEY,
	Ename VARCHAR(10),
	Designation VARCHAR(10),
	Salary INT(6),
	Dept_id INT(4)
);
INSERT INTO Employee
VALUES
	(66928, "BLAZE", "MANAGER", 55000, 3001),
	(67832, "CLARE", "MANAGER", 51000, 1001),
	(65646, "JONAS", "MANAGER", 59140, 2001),
	(67858, "SCARLET", "ANALYST", 62000, 2001),
	(69062, "FRANK", "ANALYST", 62000, 2001),
	(63679, "SANDRINE", "CLERK", 18000, 3001),
	(64989, "ADELYN", "SALESMAN", 34000, 3001),
	(65271, "WADE", "SALESMAN", 27000, 3001),
	(66564, "MADDEN", "SALESMAN", 27000, 3001),
	(68454, "TUCKER", "SALESMAN", 32000, 3001),
	(68736, "ANDRES", "CLERK", 24000, 2001),
	(69000, "JULIUS", "CLERK", 21000, 3001),
	(69324, "MARKER", "CLERK", 28000, 1001);

SELECT * FROM Employee;

SELECT Emp_no, Ename, Designation
FROM Employee;

DELETE FROM Employee
WHERE Emp_no=68454;

INSERT INTO Employee
(Emp_no, Ename, Designation, Dept_id) VALUES
	(69876, "Rahul", "ANALYST", 2001);

SELECT * FROM Employee
WHERE Salary>25000 AND Dept_id=2001;


```

**Sample Output**
```TeX
\item
Insert records into the employee table (Fields : EmpId, Ename,
 Designation, Salary, Dept.id) created.
 
 
Syntax:
\begin{verbatim}
CREATE TABLE Employee(
        Emp_no INT(6) PRIMARY KEY,
        Ename VARCHAR(10),
        Designation VARCHAR(10),
        Salary INT(6),
        Dept_id INT(4)
);
INSERT INTO Employee
VALUES
        (66928, "BLAZE", "MANAGER", 55000, 3001),
        (67832, "CLARE", "MANAGER", 51000, 1001),
        (65646, "JONAS", "MANAGER", 59140, 2001),
        (67858, "SCARLET", "ANALYST", 62000, 2001),
        (69062, "FRANK", "ANALYST", 62000, 2001),
        (63679, "SANDRINE", "CLERK", 18000, 3001),
        (64989, "ADELYN", "SALESMAN", 34000, 3001),
        (65271, "WADE", "SALESMAN", 27000, 3001),
        (66564, "MADDEN", "SALESMAN", 27000, 3001),
        (68454, "TUCKER", "SALESMAN", 32000, 3001),
        (68736, "ANDRES", "CLERK", 24000, 2001),
        (69000, "JULIUS", "CLERK", 21000, 3001),
        (69324, "MARKER", "CLERK", 28000, 1001);

\end{verbatim}
\includegraphics[]{img/p1/ss1.png}


\item
Display the details of all the employees.
 
Syntax:
\begin{verbatim}
SELECT * FROM Employee;

\end{verbatim}
\includegraphics[]{img/p1/ss2.png}


\item
Display the employee numbers, names and designation of all employees.
 
Syntax:
\begin{verbatim}
SELECT Emp_no, Ename, Designation
FROM Employee;

\end{verbatim}
\includegraphics[]{img/p1/ss3.png}


\item
Suppose the emp_no 68454 has left the company. Delete the employee
 from the database.
 
Syntax:
\begin{verbatim}
DELETE FROM Employee
WHERE Emp_no=68454;

\end{verbatim}
\includegraphics[]{img/p1/ss4.png}


\item
Suppose a new employee joins the company under department 2001 as
 an analyst. The salary of the employee is not yet fixed. Add his record to
 the database.
 Emp_no Ename Designation Salary Dept.Id
 66928 BLAZE MANAGER 55000 3001
 67832 CLARE MANAGER 51000 1001
 65646 JONAS MANAGER 59140 2001
 67858 SCARLET ANALYST 62000 2001
 69062 FRANK ANALYST 62000 2001
 63679 SANDRINE CLERK 18000 2001
 64989 ADELYN SALESMAN 34000 3001
 65271 WADE SALESMAN 27000 3001
 66564 MADDEN SALESMAN 27000 3001
 68454 TUCKER SALESMAN 32000 3001
 68736 ADNRES CLERK 24000 2001
 69000 JULIUS CLERK 21000 3001
 69324 MARKER CLERK 28000 1001
 
Syntax:
\begin{verbatim}
INSERT INTO Employee
(Emp_no, Ename, Designation, Dept_id) VALUES
        (69876, "Rahul", "ANALYST", 2001);

\end{verbatim}
\includegraphics[]{img/p1/ss5.png}


\item
Find the details of employees with salary > 25000 working in department

Syntax:
\begin{verbatim}
SELECT * FROM Employee
WHERE Salary>25000 AND Dept_id=2001;

\end{verbatim}
\includegraphics[]{img/p1/ss6.png}
```

**NOTE**: This won't work if a single question has sub questions with multiple screenshots. Then you'll have to edit manually.