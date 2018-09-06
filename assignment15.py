#Question1:->Write a python script to create a databse of students named Students.
import sqlite3
try:
    con=sqlite3.connect('chirag.db')
    cursor=con.cursor()
    query='create table students(name varchar(20),roll_no int(10) primary key,age int(3))'
    cursor.execute(query)
    query1='insert into students(name,roll_no,age) values("chirag",1610991253,20)'
    cursor.execute(query1)
    query2='insert into students(name,roll_no,age) values("bandita",1610991218,20)'
    cursor.execute(query2)
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("Error occured :",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        print("Done!!")
print()

#Question2:->Take students name and marks(between 0-100)
#as input from user 10 times using loops.
