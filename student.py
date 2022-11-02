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
    print("6 insert mark")
    print("7 view all mark")
    print("8 view mark in subject wise")
    print("9 individual marks")
    print("10 exit")

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
        print("selected add student")
        admo=input("Enter the admission number student")
        sql="SELECT `ID`FROM `students` WHERE `ADMno`="+admo
        mycursor.execute(sql)
        result=mycursor.fetchall()
        id=0
        for i in result:
            id=str(i[0])
        print("student id is :",id)
        
        phy=input("Enter the marks in physics")
        che=input("Enter marks in chemistry")
        mat=input("Enter the marks in maths")
        sql="INSERT INTO `marks`(`studentid`, `physicsmark`, `chemistrymark`, `mathsmark`) VALUES (%s,%s,%s,%s)"
        data=(id,phy,che,mat)
        mycursor.execute(sql,data)
        mydb.commit()
        print("marks data inserted successfully")
    elif(ch==7):
        print("view all marks")
        sql="SELECT s.`NAME`,s.`Rno`,s.`ADMno`,s.`COLLEGE`,m.`physicsmark`,m.`chemistrymark`,m.`mathsmark` FROM `students` s JOIN marks m ON s.`ID`=m.`studentid`"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(ch==8):
        print("n")
    elif(ch==9):
        admo=input("Enter the admission number student")
        sql="SELECT `ID`FROM `students` WHERE `ADMno`="+admo
        mycursor.execute(sql)
        result=mycursor.fetchall()
        id=0
        for i in result:
            id=str(i[0])
        sql="SELECT s.`NAME`,s.`Rno`,s.`ADMno`,s.`COLLEGE`,m.`physicsmark`,m.`chemistrymark`,m.`mathsmark` FROM `students` s JOIN marks m ON s.`ID`=m.`studentid` WHERE s.ID="+id
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)    
    elif(ch==10):
        break
