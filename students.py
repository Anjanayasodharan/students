import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'studentdb')
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print("1 add student")
    print("2 view all students")  
    print("3 search a students")
    print("4 update the students")    
    print("5 delete a students")
    print("6 exit")
    choice = int(input('Enter an option: '))
    if(choice==1):
        print('Student enter selected')
        name = input('enter the name')
        rollnumber = input('enter the adminnumber')
        adminno = input('enter the roll no')
        college = input('enter the college name')
        sql = 'INSERT INTO `students`(`name`, `rollnumber`, `adminno`, `college`) VALUES (%s,%s,%s,%s)'
        data = (name,rollnumber,adminno,college)
        mycursor.execute(sql , data)
        mydb.commit()
    elif(choice==2):
        sql = 'SELECT * FROM `students`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search student')
        adminno = input('enter the adminnumber')
        sql = 'SELECT `id`,`name`,`rollnumber`,`adminno`,`college` FROM `students` WHERE `adminno` = '+adminno
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update student')
        adminno = input('enter the adminnumber  to be updated')
        name = input('enter the name to be updated')
        rollno = input('enter the roll no to be updated')
        college = input('enter the college name to be updated')
        sql = "UPDATE `students` SET `name`='"+name+"',`rollnumber`='"+rollno+"',`college`='"+college+"' WHERE `adminno`="+adminno
        mycursor.execute(sql)
        mydb.commit()
        print("data updated succesfully")
    elif(choice==5):
        print('delete student')
    elif(choice==6):
        break