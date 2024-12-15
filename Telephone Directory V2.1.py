import mysql.connector as sql 
mydb=sql.connect(host="localhost",username="root",password="Prakhar1",database="Backstreet_Boyz")
cursor=mydb.cursor()
#Functions used
def IdCheck(Id):
 cursor.execute("select * from Directory;")
 data=cursor.fetchall()
 tick=0
 for i in range(len(data)):
      if data[i][0]==Id:
         tick=1
         break 
      else:
         tick=0
 if tick==1:
     return True
 else:
     return False
def NumCheck(Ph):
   Ph=str(Ph)
   if len(Ph)!=10:
      return True
   else:
      return False        
def f1():
    Id=int(input("enter ID number: "))
    if IdCheck(Id)==True:
       print("Wrong ID, enter a different ID")
    else:
     Name=input("enter name: ")
     Address=input("enter complete address")
     Ph1=int(input("enter primary phone number: "))
     if NumCheck(Ph1)==False:  
      Ques=input("would you like to add another phone number (y/n): ")
      if Ques=='y':
       Ph2=int(input("enter secondary phone number(optional): "))
       if NumCheck(Ph2)==False:   
        query="insert into Directory  values({},'{}','{}',{},{});".format(Id,Name,Address,Ph1,Ph2)
        cursor.execute(query)
        mydb.commit()
        print("entry is saved")
       else:
        print("invalid digits,number does not exist")
      else:
       query="insert into Directory(Id,name,address,PriPhone) values({},'{}','{}',{});".format(Id,Name,Address,Ph1)   
       cursor.execute(query) 
       mydb.commit()
       print("entry is saved")
     elif NumCheck(Ph1)==True:
       print("invalid digits,number does not exist")       
def f2():
    Id=int(input("enter ID : "))
    if IdCheck(Id)==True:
     print("CAUTION: KINDLY WRITE WHAT YOU WANT TO CHANGE IN FULL PROPER WORDS,NO SHORT FORMS ")
     update=(input("what do you want to change : "))
     if update.strip().lower()=='name':
        Name=input("enter name: ")
        query="update Directory set name='{}' where ID={};".format(Name,Id)
        cursor.execute(query)
        mydb.commit()
        print("record for ID",Id, "has been updated")
     elif update.strip().lower()=='address':
      Address=input("enter new address: ")
      query="update Directory set Address='{}' where ID={};".format(Address,Id)
      cursor.execute(query)
      mydb.commit()
      print("record for ID",Id, "has been updated")
     elif update.strip().lower()=='primary phone number':
       Ph1=int(input("enter primary phone number: "))
       NumCheck(Ph1)
       if NumCheck(Ph1)==False:
        query="update Directory set PriPhone={} where ID={};".format(Ph1,Id)
        cursor.execute(query)
        mydb.commit()
        print("record for ID",Id, "has been updated")
       else:
           print("invalid digits,number does not exist") 
     elif update.strip().lower()=='secondary phone number':
       Ph2=int(input("enter secondary phone number: "))
       NumCheck(Ph2)
       if NumCheck(Ph2)==False:
        query="update Directory set SecPhone={} where ID={};".format(Ph2,Id)
        cursor.execute(query)
        mydb.commit()
        print("record for ID",Id, "has been updated")
       else:
           print("invalid digits,number does not exist") 
     else:
        print("please enter valid option")     
    else:
       print("please enter valid option ")   
def f3():
    Id=int(input("enter ID : "))
    query="Delete from Directory  where Id={};".format(Id)
    cursor.execute(query)
    mydb.commit()
    print("Record deleted")
def f4():
     cursor.execute("select * from Directory")
     data=cursor.fetchall()
     print("PLEASE WRITE THE FOLLOWING OPTION CAREFULLY")
     q1=input("by which means do you want to search : ")
     count=0
     c=""
     if q1.strip().lower()=='name':
        Name=input("enter name: ")
        for i in range(len(data)):
           if Name in data[i][1]:
              a=data[i]
              count=count+1
              print("Record number: ",count)
              print("ID:",a[0],"\n""Name:",a[1],"\n""Address: ", a[2],"\n""primary phone number: ",a[3],"\n""Secondary Phone number: ",a[4],"\n")  
              break
        else:
              print("data not found")
     elif q1.strip().lower()=='address':
      Address=input("enter complete address: ")
      for i in range(len(data)):
           if Address in data[i][2]:
              a=data[i]
              count=count+1
              print("Record number: ",count)
              print("ID:",a[0],"Name:",a[1],"\n""Address: ", a[2],"\n""primary phone number: ",a[3],"\n""Secondary Phone number: ",a[4])   
              break                
      else: 
            print("data not found" )  
     elif q1.strip().lower()=='primary phone number':
        Ph1=int(input("enter primary phone number: "))
        NumCheck(Ph1)
        if NumCheck(Ph1)==False:
          for i in range(len(data)):
           if Ph1 in data[i][3]:
              a=data[i]
              count=count+1
              print("Record number: ",count)
              print("ID:",a[0],"\n""Name:",a[1],"\n""Address: ", a[2],"\n""primary phone number: ",a[3],"\n""Secondary Phone number: ",a[4],"\n")  
              break
          else:
            print("data not found")
     elif q1.strip().lower()=='secondary phone number':
        Ph2=int(input("enter secondary phone number(optional): "))
        NumCheck(Ph2)
        if NumCheck(Ph2)==False:
          for i in range(len(data)): 
           if Ph2==data[i][4]:
              a=data[i]
              count=count+1
              print("Record number: ",count)
              print("ID:",a[0],"\n""Name:",a[1],"\n""Address: ", a[2],"\n""primary phone number: ",a[3],"\n""Secondary Phone number: ",a[4],"\n") 
              break   
          else:
              print("data not found")  
        else:
           print("invalid digits,number does not exist")             
     elif q1.strip().lower()=='id': 
        Id=int(input("enter ID : "))
        if IdCheck(Id)==True: 
         for i in range(len(data)):
            if data[i][0]==Id:
              a=data[i]
              print("ID:",a[0],"\n""Name:",a[1],"\n""Address: ", a[2],"\n""primary phone number: ",a[3],"\n""Secondary Phone number: ",a[4],"\n")              
        else:
           print("ID not found")   
     else:
        print("please enter valid option")
#user interface
while True:
 print("\n")
 print("welcome to the telephone records ,please select which option would you like to pick ")
 print("1.INSERT NEW Record")
 print("2.UPDATE EXISTING Record")
 print("3.DELETE Record")
 print("4.SEARCH Record")
 print("5.EXIT")           
 q=int(input("enter option : "))
 if q==1:
    f1()
 if q==2:
    f2()
 if q==3:
    f3()
 if q==4:
    f4()   
 if q==5:
    break
