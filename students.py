while True:
    print("select an option from the menu")
    print("1 add student")
    print("2 view all students")  
    print("3 search a students")
    print("4 update the students")    
    print("5 delete a students")
    print("6 exit")
    choice = int(input('enter an option:'))
    if(choice==1):
        print('student enter selected')
    elif(choice==2):
        print('view student')
    elif(choice==3):
        print('search student')
    elif(choice==4):
        print('update student')
    elif(choice==5):
        print('delete student')
    elif(choice==6):
        break