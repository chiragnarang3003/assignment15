#Question1:->Write a python script to create a databse of students named Students.
import sqlite3
try:
    con=sqlite3.connect('chirag.db') #create a database named chirag.db
    cursor=con.cursor() #initialize the cursor
    query='create table student(name varchar(20),marks(3),roll_no int(10) primary key,age int(3))'
    cursor.execute(query)
    query1='insert into student(name,marks,roll_no,age) values("chirag",90,1610991253,20)'
    cursor.execute(query1)
    query2='insert into student(name,marks,roll_no,age,marks) values("bandita",92,1610991218,20)'
    cursor.execute(query2)
    con.commit() #commits Query
    quer="select * from student"
    cursor.execute(quer)
    data=cursor.fetchall()
    for row in data:
        print("NAME : {} , MARKS : {} , ROLL NO : {} , AGE : {}" \
              .format(row[0],row[1],row[2],row[3]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback() #rollback query (it executes only when any error arrises)
        print("Error occured :",e)
finally:
    if cursor:
        cursor.close() #close the cursor
    if con:
        con.close() #close the connection
        print("Done!!")
print()

#Question2:->Take students name and marks(between 0-100)
#as input from user 10 times using loops.
lisst = []
for i in range(1,11):
    lisst.append((input("NAME : "), int(input("MARKS : "))))
print(lisst)
print()

#Question3:->Add these values in two columns named "Name" and "Marks" with the appropriate data type.

try:
    con=sqlite3.connect('chirag.db')
    cursor=con.cursor()
    query="insert into student(name,marks) values(?,?)"
    cursor.executemany(query,lisst)
    con.commit()
    print("query commited")
    query1="select * from student"
    cursor.execute(query1)
    data=cursor.fetchall()
    for row in data:
        print("NAME : {} , MARKS : {}" .format(row[0],row[1]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("ERROR occured : ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        print("Done!!")
print()

#Question4:->Print the names of all the students who scored more than 80 marks.
try:
    con=sqlite3.connect('chirag.db')
    cursor=con.cursor()
    quuery="select * from student where marks>80"
    cursor.execute(quuery)
    data1=cursor.fetchall()
    for row in data1:
        print("NAME : {} , MARKS : {} , Roll no : {} , age : {}" .format(row[0],row[1],row[2],row[3]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("ERROR occured : ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        print("Done!!")
print()
