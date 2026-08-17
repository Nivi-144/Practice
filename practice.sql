 SALARY                                    NOT NULL NUMBER(10)
 DEPT                                               NUMBER(38)
 COMMISSION                                         NUMBER(10)
 MANAGER_ID                                         NUMBER(5)
 DATE_OF_JOINING                                    VARCHAR2(8)

SQL> ALTER TABLE employee
  2  MODIFY date_of_joining DATE;

Table altered.

SQL> INSERT INTO employee
  2  VALUES (1, 'Arun', 'Khan', 'Manager', 90000, NULL, 'Production', NULL, TO_DATE('04-Jan-1998','DD-Mon-YYYY'));
VALUES (1, 'Arun', 'Khan', 'Manager', 90000, NULL, 'Production', NULL, TO_DATE('04-Jan-1998','DD-Mon-YYYY'))
                                                   *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (2, 'Barun', 'Kumar', 'Manager', 80000, NULL, 'Marketing', 1, TO_DATE('09-Feb-1998','DD-Mon-YYYY'));
VALUES (2, 'Barun', 'Kumar', 'Manager', 80000, NULL, 'Marketing', 1, TO_DATE('09-Feb-1998','DD-Mon-YYYY'))
                                                     *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (3, 'Chitra', 'Kapoor', 'Engineer', 60000, NULL, 'Production', 1, TO_DATE('08-Jan-1998','DD-Mon-YYYY'));
VALUES (3, 'Chitra', 'Kapoor', 'Engineer', 60000, NULL, 'Production', 1, TO_DATE('08-Jan-1998','DD-Mon-YYYY'))
                                                        *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (4, 'Dheeraj', 'Mishra', 'Manager', 75000, NULL, 'Sales', 4, TO_DATE('27-Dec-2001','DD-Mon-YYYY'));
VALUES (4, 'Dheeraj', 'Mishra', 'Manager', 75000, NULL, 'Sales', 4, TO_DATE('27-Dec-2001','DD-Mon-YYYY'))
                                                        *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (5, 'Emma', 'Dutt', 'Engineer', 55000, NULL, 'Production', 1, TO_DATE('20-Mar-2002','DD-Mon-YYYY'));
VALUES (5, 'Emma', 'Dutt', 'Engineer', 55000, NULL, 'Production', 1, TO_DATE('20-Mar-2002','DD-Mon-YYYY'))
                                                    *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (6, 'Floki', 'Dutt', 'Accountant', 70000, NULL, 'Accounts', NULL, TO_DATE('16-Jul-2000','DD-Mon-YYYY'));
VALUES (6, 'Floki', 'Dutt', 'Accountant', 70000, NULL, 'Accounts', NULL, TO_DATE('16-Jul-2000','DD-Mon-YYYY'))
                                                       *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (7, 'Dheeraj', 'Kumar', 'Clerk', 40000, NULL, 'Accounts', 6, TO_DATE('01-Jul-2016','DD-Mon-YYYY'));
VALUES (7, 'Dheeraj', 'Kumar', 'Clerk', 40000, NULL, 'Accounts', 6, TO_DATE('01-Jul-2016','DD-Mon-YYYY'))
                                                     *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (8, 'Saul', 'Good', 'Engineer', 60000, NULL, 'R & D', NULL, TO_DATE('06-Sep-2014','DD-Mon-YYYY'));
VALUES (8, 'Saul', 'Good', 'Engineer', 60000, NULL, 'R & D', NULL, TO_DATE('06-Sep-2014','DD-Mon-YYYY'))
                                                    *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (9, 'Mou', 'Bhat', 'Clerk', 30000, NULL, 'Sales', 4, TO_DATE('08-Mar-2018','DD-Mon-YYYY'));
VALUES (9, 'Mou', 'Bhat', 'Clerk', 30000, NULL, 'Sales', 4, TO_DATE('08-Mar-2018','DD-Mon-YYYY'))
                                                *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (10, 'Sunny', 'Deol', 'Salesman', 20000, 10000, 'Marketing', 2, TO_DATE('31-Mar-2001','DD-Mon-YYYY'));
VALUES (10, 'Sunny', 'Deol', 'Salesman', 20000, 10000, 'Marketing', 2, TO_DATE('31-Mar-2001','DD-Mon-YYYY'))
                                                       *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (11, 'Bobby', 'Deol', 'Engineer', 35000, NULL, 'R & D', 8, TO_DATE('17-Oct-2017','DD-Mon-YYYY'));
VALUES (11, 'Bobby', 'Deol', 'Engineer', 35000, NULL, 'R & D', 8, TO_DATE('17-Oct-2017','DD-Mon-YYYY'))
                                                      *
ERROR at line 2:
ORA-01722: invalid number


SQL>
SQL> INSERT INTO employee
  2  VALUES (12, 'Vamiril', 'Khan', 'Salesman', 15000, 5000, 'Marketing', 2, TO_DATE('11-Jan-2013','DD-Mon-YYYY'));
VALUES (12, 'Vamiril', 'Khan', 'Salesman', 15000, 5000, 'Marketing', 2, TO_DATE('11-Jan-2013','DD-Mon-YYYY'))
                                                        *
ERROR at line 2:
ORA-01722: invalid number


SQL> VALUES (1, 'Arun', 'Khan', 'Manager', 90000,'Production', NULL, NULL, TO_DATE('04-Jan-1998','DD-Mon-YYYY'));
SP2-0734: unknown command beginning "VALUES (1,..." - rest of line ignored.
SQL> INSERT INTO VALUES (1, 'Arun', 'Khan', 'Manager', 90000,'Production', NULL, NULL, TO_DATE('04-Jan-1998','DD-Mon-YYYY'));
INSERT INTO VALUES (1, 'Arun', 'Khan', 'Manager', 90000,'Production', NULL, NULL, TO_DATE('04-Jan-1998','DD-Mon-YYYY'))
            *
ERROR at line 1:
ORA-00903: invalid table name


SQL> INSERT INTO employee VALUES (1, 'Arun', 'Khan', 'Manager', 90000,'Production', NULL, NULL, TO_DATE('04-Jan-1998','DD-Mon-YYYY'));
INSERT INTO employee VALUES (1, 'Arun', 'Khan', 'Manager', 90000,'Production', NULL, NULL, TO_DATE('04-Jan-1998','DD-Mon-YYYY'))
                                                                 *
ERROR at line 1:
ORA-01722: invalid number


SQL> INSERT INTO employee VALUES (1, 'Arun', 'Khan', 'Manager', 90000,'Production', NULL, NULL, TO_DATE('04-Jan-1998','DD-Mon-YYYY'));
INSERT INTO employee VALUES (1, 'Arun', 'Khan', 'Manager', 90000,'Production', NULL, NULL, TO_DATE('04-Jan-1998','DD-Mon-YYYY'))
                                                                 *
ERROR at line 1:
ORA-01722: invalid number


SQL> ALTER TABLE employee
  2  DROP CONSTRAINT emp_dept_fk;
DROP CONSTRAINT emp_dept_fk
                *
ERROR at line 2:
ORA-02443: Cannot drop constraint  - nonexistent constraint


SQL> DROP TABLE employee;

Table dropped.

SQL> CREATE TABLE employee (
  2      emp_id NUMBER(5) PRIMARY KEY,
  3      f_name VARCHAR2(20) NOT NULL,
  4      l_name VARCHAR2(20),
  5      job_type VARCHAR2(20),
  6      salary NUMBER(10) NOT NULL,
  7      dept VARCHAR2(20),
  8      commission NUMBER(10),
  9      manager_id NUMBER(5),
 10      date_of_joining DATE
 11  );

Table created.

SQL> ALTER TABLE employee
  2  ADD CONSTRAINT emp_dept_fk
  3  FOREIGN KEY (dept)
  4  REFERENCES department(d_name);

Table altered.

SQL> DESC employee;
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 EMP_ID                                    NOT NULL NUMBER(5)
 F_NAME                                    NOT NULL VARCHAR2(20)
 L_NAME                                             VARCHAR2(20)
 JOB_TYPE                                           VARCHAR2(20)
 SALARY                                    NOT NULL NUMBER(10)
 DEPT                                               VARCHAR2(20)
 COMMISSION                                         NUMBER(10)
 MANAGER_ID                                         NUMBER(5)
 DATE_OF_JOINING                                    DATE

SQL> INSERT INTO employee
  2  VALUES (
  3      1,
  4      'Arun',
  5      'Khan',
  6      'Manager',
  7      90000,
  8      'Production',
  9      NULL,
 10      NULL,
 11      TO_DATE('04-Jan-1998','DD-Mon-YYYY')
 12  );

1 row created.

SQL> INSERT INTO employee VALUES
  2  (2, 'Barun', 'Kumar', 'Manager', 80000, 'Marketing', NULL, 1,
  3   TO_DATE('09-Feb-1998','DD-Mon-YYYY'));

1 row created.

SQL> INSERT INTO employee VALUES
  2  (3, 'Chitra', 'Kapoor', 'Engineer', 60000, 'Production', NULL, 1,
  3   TO_DATE('08-Jan-1998','DD-Mon-YYYY'));

1 row created.

SQL> INSERT INTO employee VALUES
  2  (4, 'Dheeraj', 'Mishra', 'Manager', 75000, 'Sales', NULL, 4,
  3   TO_DATE('27-Dec-2001','DD-Mon-YYYY'));

1 row created.

SQL>
SQL> INSERT INTO employee VALUES
  2  (5, 'Emma', 'Dutt', 'Engineer', 55000, 'Production', NULL, 1,
  3   TO_DATE('20-Mar-2002','DD-Mon-YYYY'));

1 row created.

SQL> INSERT INTO employee VALUES
  2  (6, 'Floki', 'Dutt', 'Accountant', 70000, 'Accounts', NULL, NULL,
  3   TO_DATE('16-Jul-2000','DD-Mon-YYYY'));

1 row created.

SQL>
SQL> INSERT INTO employee VALUES
  2  (7, 'Dheeraj', 'Kumar', 'Clerk', 40000, 'Accounts', NULL, 6,
  3   TO_DATE('01-Jul-2016','DD-Mon-YYYY'));

1 row created.

SQL> INSERT INTO employee VALUES
  2  (8, 'Saul', 'Good', 'Engineer', 60000, 'R & D', NULL, NULL,
  3   TO_DATE('06-Sep-2014','DD-Mon-YYYY'));

1 row created.

SQL> INSERT INTO employee VALUES
  2  (9, 'Mou', 'Bhat', 'Clerk', 30000, 'Sales', NULL, 4,
  3   TO_DATE('08-Mar-2018','DD-Mon-YYYY'));

1 row created.

SQL> INSERT INTO employee VALUES
  2  (10, 'Sunny', 'Deol', 'Salesman', 20000, 'Marketing', 10000, 2,
  3   TO_DATE('31-Mar-2001','DD-Mon-YYYY'));

1 row created.

SQL> INSERT INTO employee VALUES
  2  (11, 'Bobby', 'Deol', 'Engineer', 35000, 'R & D', NULL, 8,
  3   TO_DATE('17-Oct-2017','DD-Mon-YYYY'));

1 row created.

SQL> INSERT INTO employee VALUES
  2  (12, 'Vamiril', 'Khan', 'Salesman', 15000, 'Marketing', 5000, 2,
  3   TO_DATE('11-Jan-2013','DD-Mon-YYYY'));

1 row created.

SQL> SELECT d_name, d_loc
  2  FROM department;

D_NAME               D_LOC
-------------------- --------------------
Sales                Kol
Accounts             Delhi
Production           Kol
Marketing            Kol
R & D                Marketing

SQL> SELECT f_name, l_name, salary, salary + 1000 AS new_salary
  2  FROM employee;

F_NAME               L_NAME                   SALARY NEW_SALARY
-------------------- -------------------- ---------- ----------
Arun                 Khan                      90000      91000
Barun                Kumar                     80000      81000
Chitra               Kapoor                    60000      61000
Dheeraj              Mishra                    75000      76000
Emma                 Dutt                      55000      56000
Floki                Dutt                      70000      71000
Dheeraj              Kumar                     40000      41000
Saul                 Good                      60000      61000
Mou                  Bhat                      30000      31000
Sunny                Deol                      20000      21000
Bobby                Deol                      35000      36000

F_NAME               L_NAME                   SALARY NEW_SALARY
-------------------- -------------------- ---------- ----------
Vamiril              Khan                      15000      16000

12 rows selected.

SQL> SELECT f_name, salary * 12 + 1000 AS annual_salary_with_yearly_bonus,
  2         salary * 12 + 100 * 12 AS annual_salary_with_monthly_bonus
  3  FROM employee;

F_NAME               ANNUAL_SALARY_WITH_YEARLY_BONUS
-------------------- -------------------------------
ANNUAL_SALARY_WITH_MONTHLY_BONUS
--------------------------------
Arun                                         1081000
                         1081200

Barun                                         961000
                          961200

Chitra                                        721000
                          721200


F_NAME               ANNUAL_SALARY_WITH_YEARLY_BONUS
-------------------- -------------------------------
ANNUAL_SALARY_WITH_MONTHLY_BONUS
--------------------------------
Dheeraj                                       901000
                          901200

Emma                                          661000
                          661200

Floki                                         841000
                          841200


F_NAME               ANNUAL_SALARY_WITH_YEARLY_BONUS
-------------------- -------------------------------
ANNUAL_SALARY_WITH_MONTHLY_BONUS
--------------------------------
Dheeraj                                       481000
                          481200

Saul                                          721000
                          721200

Mou                                           361000
                          361200


F_NAME               ANNUAL_SALARY_WITH_YEARLY_BONUS
-------------------- -------------------------------
ANNUAL_SALARY_WITH_MONTHLY_BONUS
--------------------------------
Sunny                                         241000
                          241200

Bobby                                         421000
                          421200

Vamiril                                       181000
                          181200


12 rows selected.

SQL> SET LINESIZE 200;
SQL> SELECT f_name,
  2         salary * 12 + 1000 AS YEARLY_BONUS,
  3         salary * 12 + 1200 AS MONTHLY_BONUS
  4  FROM employee;

F_NAME               YEARLY_BONUS MONTHLY_BONUS
-------------------- ------------ -------------
Arun                      1081000       1081200
Barun                      961000        961200
Chitra                     721000        721200
Dheeraj                    901000        901200
Emma                       661000        661200
Floki                      841000        841200
Dheeraj                    481000        481200
Saul                       721000        721200
Mou                        361000        361200
Sunny                      241000        241200
Bobby                      421000        421200

F_NAME               YEARLY_BONUS MONTHLY_BONUS
-------------------- ------------ -------------
Vamiril                    181000        181200

12 rows selected.

SQL> SELECT f_name,
  2         salary * 12 + 1000 AS YEARLY_BONUS,
  3         salary * 12 + 1200 AS MONTHLY_BONUS
  4  FROM employee;

F_NAME               YEARLY_BONUS MONTHLY_BONUS
-------------------- ------------ -------------
Arun                      1081000       1081200
Barun                      961000        961200
Chitra                     721000        721200
Dheeraj                    901000        901200
Emma                       661000        661200
Floki                      841000        841200
Dheeraj                    481000        481200
Saul                       721000        721200
Mou                        361000        361200
Sunny                      241000        241200
Bobby                      421000        421200

F_NAME               YEARLY_BONUS MONTHLY_BONUS
-------------------- ------------ -------------
Vamiril                    181000        181200

12 rows selected.

SQL> SELECT f_name,
  2  salary * 12 + 1000 AS ANNUAL_SALARY_YEARLY_BONUS,
  3  salary * 12 + 1200 AS ANNUAL_SALARY_MONTHLY_BONUS,
  4  FROM employee;
FROM employee
*
ERROR at line 4:
ORA-00936: missing expression


SQL> SELECT f_name,
  2         salary * 12 + 1000 AS YEARLY_BONUS,
  3         salary * 12 + 1200 AS MONTHLY_BONUS
  4  FROM employee;

F_NAME               YEARLY_BONUS MONTHLY_BONUS
-------------------- ------------ -------------
Arun                      1081000       1081200
Barun                      961000        961200
Chitra                     721000        721200
Dheeraj                    901000        901200
Emma                       661000        661200
Floki                      841000        841200
Dheeraj                    481000        481200
Saul                       721000        721200
Mou                        361000        361200
Sunny                      241000        241200
Bobby                      421000        421200

F_NAME               YEARLY_BONUS MONTHLY_BONUS
-------------------- ------------ -------------
Vamiril                    181000        181200

12 rows selected.

SQL> SELECT f_name AS NAME, salary * 12 AS ANNSAL
  2  FROM employee;

NAME                     ANNSAL
-------------------- ----------
Arun                    1080000
Barun                    960000
Chitra                   720000
Dheeraj                  900000
Emma                     660000
Floki                    840000
Dheeraj                  480000
Saul                     720000
Mou                      360000
Sunny                    240000
Bobby                    420000

NAME                     ANNSAL
-------------------- ----------
Vamiril                  180000

12 rows selected.

SQL> SELECT emp_id, f_name, l_name, job_type
  2  FROM employee
  3  WHERE salary = (SELECT MAX(salary) FROM employee);

    EMP_ID F_NAME               L_NAME               JOB_TYPE
---------- -------------------- -------------------- --------------------
         1 Arun                 Khan                 Manager

SQL> SELECT l_name AS LasT, salary + 100 AS NewSal
  2  FROM employee;

LAST                     NEWSAL
-------------------- ----------
Khan                      90100
Kumar                     80100
Kapoor                    60100
Mishra                    75100
Dutt                      55100
Dutt                      70100
Kumar                     40100
Good                      60100
Bhat                      30100
Deol                      20100
Deol                      35100

LAST                     NEWSAL
-------------------- ----------
Khan                      15100

12 rows selected.

SQL> SELECT emp_id, f_name, l_name, job_type
  2  FROM employee
  3  WHERE salary = (SELECT MAX(salary) FROM employee);

    EMP_ID F_NAME               L_NAME               JOB_TYPE
---------- -------------------- -------------------- --------------------
         1 Arun                 Khan                 Manager

SQL> SELECT emp_id, f_name, l_name, job_type
  2  FROM employee
  3  WHERE salary = (SELECT MIN(salary) FROM employee);

    EMP_ID F_NAME               L_NAME               JOB_TYPE
---------- -------------------- -------------------- --------------------
        12 Vamiril              Khan                 Salesman

SQL> SELECT AVG(salary) AS average_salary
  2  FROM employee;

AVERAGE_SALARY
--------------
         52500
