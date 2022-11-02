from unittest import result
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='studentdb')

mycursor=mydb.cursor()
while True:
    print("\nSelect an option")
    print("1 add student")
    print("2 view all student")
    print("3 search a student")
    print("4 update the student")
    print("5 delete a student")
    print("6 exit")

    ch=int(input("select an option  : \n"))
    if(ch==1):
        print("selected add student")
        name=input("Enter the name")
        admo=input("Enter the admission number")
        rno=input("Enter rollnumber")
        clg=input("Enter the college name")
        sql='INSERT INTO `students` (`NAME`, `Rno`, `ADMno`, `COLLEGE`) VALUES (%s,%s,%s,%s)'
        data=(name,admo,rno,clg)
        mycursor.execute(sql,data)
        mydb.commit()
        print('inserted succes')
    elif(ch==2):
        sql='SELECT * FROM `students`'
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        print("selected view all student")
    elif(ch==3):
        print("selected search student")
        admo=input("Enter the admission number for searching a student")
        sql='SELECT * FROM `students` WHERE `ADMno`='+admo
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(ch==4):
        admo=input("Enter the admission number")
        name=input("Enter the name to be updated")
        rno=input("Enter rollnumber to be updated")
        clg=input("Enter the college name to be updated")
        sql="UPDATE `students` SET `NAME`='"+name+"',`Rno`='"+rno+"',`COLLEGE`='"+clg+"' WHERE `ADMno`="+admo
        mycursor.execute(sql)
        mydb.commit()
        print("updated successfully")
    elif(ch==5):
        admo=input("Enter the admission number for delete a student")
        sql='DELETE FROM `students` WHERE `ADMno`='+admo
        mycursor.execute(sql)
        mydb.commit()
        print("deleted successfully")    
    elif(ch==6):
        break
