#!/Python36/python
import pymongo
import pandas as pd
from os import system
from pymongo import MongoClient
import time
import datetime


def to_integer(stu_doa):
    return 10000*stu_doa.year + 100*stu_doa.month + stu_doa.day 

class student:
    def add_student(self):
        stu_roll=int(input("enter roll no of student"))
        stu_name=input("enter name of student")
        stu_mother=input("enter mother's name of student")
        stu_father=input("enter father's name of student")
        stu_contact=input("enter contact number for student")
        stu_address=input("enter address of student")
        stu_course=input("enter course of student")
        stu_year=input("enter year student")
        stu_branch=input("enter Branch of student")
        stu_email=input("enter email of student")
        stu_doa=datetime.datetime.now()
        collection1=db.student
        if collection1.insert({"roll":stu_roll,"name":stu_name,"mother name":stu_mother,"father name":stu_father,"contact":stu_contact,"address":stu_address,"course":stu_course,"year":stu_year,
                       "branch":stu_branch,"email":stu_email,"date of admission":to_integer(stu_doa),"admission status":"active"}):
            print("Record Added Successfully")
            rch=input("Do you want to perform more addition? Y|N")
            if rch=='Y':
                s.add_student()
            elif rch=='N':
                m.mainmenu()
            else:
                print("Please enter choice only Y and N and not small letter words or anything else")
                exit()
        else :
            print("record not added. It may face some Errors")

    def del_student(self):
        try:
            roll=int(input("enter ID/Roll no for Student"))
            dotc=datetime.datetime.now()
            collectiondel=db.student
            if collectiondel.update({"roll":roll},{ "$set":{"date of TC":to_integer(dotc),"admission status":"T C"}}):
                print("record delete Successfully")
                delch=input("Do you want to perform more deletion? Y|N")
                if delch=='Y':
                    del_student()
                elif delch=='N':
                    m.mainmenu()
                else:
                    print("Please enter choice only Y and N and not small letter words or anything else")
                    exit()
            else:
                print("record not deleted. It may face some Errors")
        except Exception as e :
            print (e)
   
class result():
    def add_result(self):
        exam=input("Name of Examination  (Semester/Mid Terms)")
        roll=int(input("enter roll no for student"))
        name=input("enter name of student")
        sub1=int(input("enter marks for subject 1"))
        sub2=int(input("enter marks for subject 2"))
        sub3=int(input("enter marks for subject 3"))
        total=sub1+sub2+sub3
        avg=(sub1+sub2+sub3)/3
        year=int(input("enter year of study"))
        branch=input("branch of student")
        if avg>40 :
            result="pass"
        else:
            result="fail"
        collection1=db.result 
        if collection1.insert({"examination":exam,"roll":roll,"name":name,"subject 1":sub1,"subject 2":sub2,"subject 3":sub3,"total":total,"average":avg,"year":year,
                       "branch":branch,"result":result}):
            print("Record Added Successfully")
            rch=input("Do you want to perform more addition? Y|N")
            if rch=='Y':
                res.add_result()
            elif rch=='N':
                m.mainmenu()
            else:
                print("Please enter choice only Y and N and not small letter words or anything else")
                exit()
        else :
            print("record not added. It may face some Errors")

    def del_result(self):
        roll=int(input("enter roll no. whose result has to delete"))
        collection12=db.result
        if db.result.remove({"roll":roll},1):
            print("delete successfully"," ")
            ch=input("do you want to delete more records")
            if ch=='Y':
                res.del_result()
            elif ch=='N':
                m.mainmenu()
            else:
                print("Please enter choice only Y and N and not small letter words or anything else")
                exit()
        else :
            print("record not deleted. It may face some Errors")
    def view_result(self):
        resu={}
        keys=[]
        values=[]
        roll=int(input("enter roll/id for search/view record"))
        collection_se=db.result
        if collection_se.find():
            for post in collection_se.find({"roll":roll}):
                resu=post
                rollno=resu['roll']
            if len(resu) >0:
                print("record found for. ",resu['name']," ")
                print("result ",resu['result'],"with aggregate of = ",resu['average']," ")
            else :
                print("no record found")
                exit()
                
            ch=input("Want to View Record..( Y | N )")
            if ch=='Y':
                for i in collection_se.find({"roll":rollno},{"_id":0}):
                    resu=i  
                #print(resu)
                keys=list(resu.keys())
                values=list(resu.values())
                df=pd.DataFrame()
                df=df.append({keys[0]:values[0]},ignore_index=True)
                for i in range(1,len(keys)):
                    df2=pd.DataFrame()
                    df2=df2.append({keys[i]:values[i]},ignore_index=True)
                    df=pd.concat([df, df2],axis=1,join='inner')
                print(df.T)
                ch=input("Do you want to search more records.? ( Y| N)")
                if ch=='Y':
                    res.view_result()
                elif ch=='N':
                    m.mainmenu()
                else:
                    print("wrong choice")
                    exit()
            elif ch=='N':
                m.mainmenu()
            else:
                print("Not a Option")
                m.mainmenu()
        else:
            print("Error")



            
class teacher:
    def add_teacher(self):
        t_id=int(input("enter id for teacher"))
        t_name=input("enter name of teacher")
        t_age=int(input("enter age of teacher"))
        t_designation=input("enter designation of teacher")
        t_contact=input("enter contact number for teacher")
        t_address=input("enter address of teacher")
        t_dept=input("enter department of teacher")
        t_salary=float(input("enter salary for teacher"))
        t_email=input("enter email of teacher")
        t_doj= datetime.datetime.now()
        collection1=db.teacher
        if collection1.insert({"teacher id":t_id,"teacher name":t_name,"teacher's age":t_age,"teacher's designation":t_designation,"teacher contact":t_contact,"address":t_address,
                           "teacher's department":t_dept,"salary":t_salary,"teacher's email":t_email,"date of joining":to_integer(t_doj),"date of resign/fire":"","status":"active"}):
            print("Record Added Successfully")
            rch=input("Do you want to perform more addition? Y|N")
            if rch=='Y':
                teach.add_teacher()
            elif rch=='N':
                m.mainmenu()
            else:
                
                print("Please enter choice only Y and N and not small letter words or anything else")
                exit()
        else :
            print("record not added. It may face some Errors")

         
    def del_teacher(self):
        try:
            t_id=int(input("enter ID for teacher"))
            dol=datetime.datetime.now()
            collectiondel=db.teacher
            if collectiondel.update({"teacher id":t_id},{ "$set":{"date of resign/fire":to_integer(dol),"status":"Resigned/Fired"}}):
                print("record delete Successfully")
                delch=input("Do you want to perform more deletion? Y|N")
                if delch=='Y':
                    teach.del_student()
                elif delch=='N':
                    m.mainmenu()
                else:
                    print("Please enter choice only Y and N and not small letter words or anything else")
                    exit()
            else :
                print("record not deleted. It may face some Errors")
        except Exception as e :
            print (e)

class staff:
    def add_staff(self):
        st_id=int(input("enter id for staff member"))
        st_name=input("enter name of staff member")
        st_age=int(input("enter age of staff member"))
        st_post=input("enter post of staff member")
        st_contact=input("enter contact number for staff member")
        st_address=input("enter address of staff memebr")
        st_dept=input("enter department of staff member")
        st_salary=float(input("enter salary for staff member"))
        st_email=input("enter email of staff member")
        st_doj= datetime.datetime.now()
        collection1=db.staff
        if collection1.insert({"staff id":st_id,"staff name":st_name,"staff's age":st_age,"staff's post":st_post,"staff contact":st_contact,"address":st_address,
                           "staff's department":st_dept,"salary":st_salary,"staff's email":st_email,"date of joining":to_integer(st_doj),"status":"active"}):
            print("Record Added Successfully")
            rch=input("Do you want to perform more addition? Y|N")
            if rch=='Y':
                st.add_staff()
            elif rch=='N':
                m.mainmenu()
            else:
                
                print("Please enter choice only Y and N and not small letter words or anything else")
                exit()
        else :
            print("record not added. It may face some Errors")

         
    def del_staff(self):
        try:
            st_id=int(input("enter ID for staff"))
            dol=datetime.datetime.now()
            collectiondel=db.staff
            if collectiondel.update({"staff id":st_id},{ "$set":{"date of resign/fire":to_integer(dol),"status":"Resigned/Fired"}}):
                print("record delete Successfully")
                delch=input("Do you want to perform more deletion? Y|N")
                if delch=='Y':
                    st.del_student()
                elif delch=='N':
                    m.mainmenu()
                else:
                    print("Please enter choice only Y and N and not small letter words or anything else")
                    exit()
            else :
                print("record can not deleted. It may face some Errors")
        except Exception as e :
            print (e)

class search_record():
    def search_student(self):
        stu={}
        s={}
        keys=[]
        values=[]
        roll=int(input("enter roll/id for search/view record"))
        collection_se=db.student
        if collection_se.find():
            for post in collection_se.find({"roll":roll}):
                stu=post
                rollno=stu['roll']
            if len(stu) >0:
                print("record found for. ",stu['name']," ")
            else :
                print("no record found")
                exit()
                
            ch=input("Want to View Record..( Y | N )")
            if ch=='Y':
                for i in collection_se.find({"roll":rollno},{"_id":0}):
                    s=i  
                #print(s)
                keys=list(s.keys())
                values=list(s.values())
                df=pd.DataFrame()
                df=df.append({keys[0]:values[0]},ignore_index=True)
                for i in range(1,len(keys)):
                    df2=pd.DataFrame()
                    df2=df2.append({keys[i]:values[i]},ignore_index=True)
                    df=pd.concat([df, df2],axis=1,join='inner')
                print(df.T)
                ch=input("Do you want to search more records.? ( Y| N)")
                if ch=='Y':
                    srch.search_student()
                elif ch=='N':
                    m.mainmenu()
                else:
                    print("wrong choice")
                    exit()
            elif ch=='N':
                m.mainmenu()
            else:
                print("Not a Option")
                m.mainmenu()
        else:
            print("Error")

    def search_teacher(self):
        teach={}
        t=[]
        keys=[]
        values=[]
        teach_id=int(input("enter id for search/view for record"))
        collection_se=db.teacher
        if collection_se.find():
            for post in collection_se.find({"teacher id":teach_id}):
                teach=post
                teacher_id=teach['teacher id']
            if len(teach) >0:
                print("record found for. ",teach['teacher name']," ")
            else :
                print("no record found")
                exit()
                
            ch=input("Want to View Record..( Y | N )")
            if ch=='Y':
                for i in collection_se.find({"teacher id":teacher_id},{"_id":0}):
                    t=i
                    keys=list(t.keys())
                    values=list(t.values())
                #print(t)
                df=pd.DataFrame()
                df=df.append({keys[0]:values[0]},ignore_index=True)
                for i in range(1,len(keys)):
                    df2=pd.DataFrame()
                    df2=df2.append({keys[i]:values[i]},ignore_index=True)
                    df=pd.concat([df, df2],axis=1,join='inner')
                print(df.T)
                ch=input("Do you want to search more records.? ( Y| N)")
                if ch=='Y':
                    srch.search_teacher()
                elif ch=='N':
                    m.mainmenu()
                else:
                    print("wrong choice")
                    exit()
            elif ch=='N':
                m.mainmenu()
            else:
                print("Not a Option")
                m.mainmenu()
        else:
            print("Error")

    def search_staff(self):
        staff={}
        st={}
        keys=[]
        values=[]
        staff_id=int(input("enter id for search/view for record"))
        collection_se=db.staff
        if collection_se.find():
            for post in collection_se.find({"staff id":staff_id}):
                staff=post
                staff_id=staff['staff id']
            if len(staff) >0:
                print("record found for. ",staff['staff name']," ")
            else :
                print("no record found")
                exit()
                
            ch=input("Want to View Record..( Y | N )")
            if ch=='Y':
                for i in collection_se.find({"staff id":staff_id},{"_id":0}):
                    st=i
                #print(st)
                keys=list(st.keys())
                values=list(st.values())
                df=pd.DataFrame()
                df=df.append({keys[0]:values[0]},ignore_index=True)
                for i in range(1,len(keys)):
                    df2=pd.DataFrame()
                    df2=df2.append({keys[i]:values[i]},ignore_index=True)
                    df=pd.concat([df, df2],axis=1,join='inner')
                print(df.T)
                ch=input("Do you want to search more records.? ( Y| N)")
                if ch=='Y':
                    srch.search_staff()
                elif ch=='N':
                    m.mainmenu()
                else:
                    print("wrong choice")
                    exit()
            elif ch=='N':
                m.mainmenu()
            else:
                print("Not a Option")
                m.mainmenu()
        else:
            print("Error")

class downrecord():
    def xl_student(self):
        keys=[]
        values=[]
        student={}
        collection_xl=db.student
        if collection_xl.find():
            writer=pd.ExcelWriter('output.xlsx')
            count=0
            for i in collection_xl.find({},{"_id":0}):
                student=i
                print(student)
                keys=list(student.keys())
                values=list(student.values())
                df=pd.DataFrame()
                df=df.append({keys[0]:values[0]},ignore_index=True)
                for i in range(1,len(keys)):   
                    df2=pd.DataFrame()
                    df2=df2.append({keys[i]:values[i]},ignore_index=True)
                    df=pd.concat([df, df2],axis=1,join='inner')
                
                #print(df.T)
                if count==0:
                    df_main=pd.DataFrame()
                    df_main=df
                else:
                    df_main=df_main.append(df,sort=False)
                count+=1
            df_main.set_index('roll',inplace=True)
            df_main.to_excel(writer,'Sheet1')
            writer.save()
            print("print successfully")
            ch=input("press c to continue to main menu or press e to exit")
            if ch=='c':
                m.mainmenu()
            else:
                exit()
                
        else:
            print("Error. No database found!!!!")
            m.mainmenu()
    def xl_teacher(self):
        keys=[]
        values=[]
        teacher={}
        collection_xl=db.teacher
        if collection_xl.find():
            writer=pd.ExcelWriter('teacherdata.xlsx')
            count=0
            for i in collection_xl.find({},{"_id":0}):
                teacher=i
                #print(teacher)
                keys=list(teacher.keys())
                values=list(teacher.values())
                df=pd.DataFrame()
                df=df.append({keys[0]:values[0]},ignore_index=True)
                for i in range(1,len(keys)):   
                    df2=pd.DataFrame()
                    df2=df2.append({keys[i]:values[i]},ignore_index=True)
                    df=pd.concat([df, df2],axis=1,join='inner')
                
                #print(df.T)
                if count==0:
                    df_main=pd.DataFrame()
                    df_main=df
                else:
                    df_main=df_main.append(df,sort=False)
                count+=1
            df_main.set_index('teacher id',inplace=True)
            df_main.to_excel(writer,'Sheet1')
            writer.save()
            print("print successfully")
            ch=input("press c to continue to main menu or press e to exit")
            if ch=='c':
                m.mainmenu()
            else:
                exit()    
        else:
            print("Error. No database found!!!!")
            m.mainmenu()


    def xl_teacher(self):
        keys=[]
        values=[]
        staff={}
        collection_xl=db.staff
        if collection_xl.find():
            writer=pd.ExcelWriter('staffdata.xlsx')
            count=0
            for i in collection_xl.find({},{"_id":0}):
                staff=i
                #print(staff)
                keys=list(staff.keys())
                values=list(staff.values())
                df=pd.DataFrame()
                df=df.append({keys[0]:values[0]},ignore_index=True)
                for i in range(1,len(keys)):   
                    df2=pd.DataFrame()
                    df2=df2.append({keys[i]:values[i]},ignore_index=True)
                    df=pd.concat([df, df2],axis=1,join='inner')
                
                #print(df.T)
                if count==0:
                    df_main=pd.DataFrame()
                    df_main=df
                else:
                    df_main=df_main.append(df,sort=False)
                count+=1
            df_main.set_index('staff id',inplace=True)
            df_main.to_excel(writer,'Sheet1')
            writer.save()
            print("print successfully")
            ch=input("press c to continue to main menu or press e to exit")
            if ch=='c':
                m.mainmenu()
            else:
                exit()    
        else:
            print("Error. No database found!!!!")
            m.mainmenu()
    

class library():
    def addbook(self):
        b_id=int(input("enter book id"))
        b_name=input("enter book name")
        b_author=input("enter author name")
        b_theme=input("enter theme of book")
        b_qty=int(input("Total no. of book is.."))
        b_price=float(input("enter book price"))
        collection1=db.book
        if collection1.insert({"book id":b_id,"book name":b_name,"author name":b_author,"book theme":b_theme,"total book":b_qty,"price":b_price}):
            print("Record Added Successfully")
            rch=input("Do you want to perform more addition? Y|N")
            if rch=='Y':
                lib.addbook()
            elif rch=='N':
                m.mainmenu()
            else:
                print("Please enter choice only Y and N and not small letter words or anything else")
                exit()
        else :
            print("record not added. It may face some Errors")
    def bookdetail(self):
        b=[]
        keys=[]
        values=[]
        id=int(input("enter book id"))
        collection_bd=db.book
        if collection_bd.find({},{"_id":0}):
            for i in collection_bd.find({"book id":id},{"_id":0}):
                b=i
                print(b)
                keys=list(b.keys())
                values=list(b.values())
            df=pd.DataFrame()
            df=df.append({keys[0]:values[0]},ignore_index=True)
            for i in range(1,len(keys)):
                df2=pd.DataFrame()
                df2=df2.append({keys[i]:values[i]},ignore_index=True)
                df=pd.concat([df, df2],axis=1,join='inner')
                print(df)
                ch=input("Do you want to search more records.? ( Y| N)")
                if ch=='Y':
                    lib.bookdetail()
                elif ch=='N':
                    m.mainmenu()
                else:
                    print("wrong choice")
                    exit()
        else:
            print("record not found...")


    def delbook(self):
        b={}
        id=int(input("enter book id"))
        collection=db.book
        if collection.find({"book id":id},{"_id":0}):
            for i in collection.find({"book id":id}):
                b=i
            if len(b)>0:
                collection.remove({"book id":id},1)
                print("delete successfully")
                ch=input("Do you want to delete more record? (Y | N)")
                if ch=='Y':
                    lib.delbook()
                elif ch=='N':
                    m.mainmenu()
                else:
                    print("Not a valid option")
                    exit()
            else:
                print("Record not found. Record can't deleted")
                m.mainmenu()
        else:
            print("IT may face some error while searching record for deletion. Sorry for inconvience")

    def updatebook(self,b_id,qty):
        collection_up=db.book
        collection_up.update({"book id":b_id},{ "$inc":{"total book":-qty}})

    def up_ret_book(self,b_id,qty):
        collection_up_ret=db.book
        collection_up_ret.update({"book id":b_id},{ "$inc":{"total book":qty}})
        

    def issuebook(self):
        s_id=int(input("enter roll no of student"))
        name=input("enter name of student")
        branch=input("enter branch of student")
        year=input("enter year")
        contact=input("enter contact no")
        b_id=int(input("enter book id"))
        b_name=input("enter name of book")
        iss_dt=time.asctime( time.localtime(time.time()))
        qty=int(input("enter total no. of books"))
        collection_iss=db.library
        if collection_iss.insert({"student id":s_id,"student name":name,"branch":branch,"year":year,"contact":contact,"book id":b_id,"book name":b_name,"issue date":iss_dt,"no of book":qty}):
            print("Book issued successfully")
            lib.updatebook(b_id,qty)
            ch=input("Do you want to issue another books..( Y | N)")
            if ch=='Y':
                lib.issuebook()
            elif ch=='N':
                m.mainmenu()
            else:
                print("not a valid option")
                exit()
        else:
            print("can't issue book right now")
            m.mainmenu()

    def retbook():
        s_id=int(input("enter roll no of student"))
        b_id=int(input("enter book id"))
        qty=int(input("enter no of books to return"))
        ret_dt=time.asctime( time.localtime(time.time()))
        collection_ret=db.library
        collection_ret.update({"student id":s_id},{"$set":{"return date":ret_dt}})
        up_ret_book(b_id,qty)


class main:
    def mainmenu(self):
        print("      Welcome  to  JECRC portal    ","   ")
        print("Choose Option to perform from the following functions.....","  ")
        print("  1. Add Record  "," ")
        print("  2. Delete a Record  "," ")
        print("  3. Search and View Record  "," ")
        print("  4. Update a Record  "," ")
        print("  5. View Result of Student  "," ")
        print("  6. Download complete records  "," ")
        print("  7. Fees Department  "," ")
        print("  8. Library "," ")
        print("  9. Close Application  "," ")
        choice=int(input("enter Your Choice of Opertaion (please select option from 1 to 9 only)"))
        system('cls')
        if choice==1:
            print(" Add Record For: "," ")
            print(" 1. Student"," ")
            print(" 2. Teacher"," ")
            print(" 3. Staff"," ")
            print(" 4. Result of Student"," ")
            ch=int(input("enter Your Choice of Opertaion For Addition Of Record"))
            system('cls')
            if ch==1:
                s.add_student()
            elif ch==2:
                teach.add_teacher()
            elif ch==3:
                st.add_staff()
            elif ch==4:
                res.add_result()
            else:
                print("you enter incorrect option for operation of record addtion")
                mainmenu()
        elif choice==2:
            print(" Delete Record For: "," ")
            print(" 1. Student"," ")
            print(" 2. Teacher"," ")
            print(" 3. Staff"," ")
            print(" 4. Result of Student"," ")
            ch=int(input("enter Your Choice of Opertaion For DELETION Of Record"))
            system('cls')
            if ch==1:
                s.del_student()
            elif ch==2:
                teach.del_teacher()
            elif ch==3:
                st.del_staff()
            elif ch==4:
                res.del_result()
            else:
                print("you enter incorrect option for operation of record deletion")
                mainmenu()
        elif choice==3:
            print("View Record for:...."," ")
            print(" 1. Student"," ")
            print(" 2. Teacher"," ")
            print(" 3. Staff"," ")
            ch=int(input("enter Your Choice of Opertaion For search and view Of Record"))
            if ch==1:
                srch.search_student()
            elif ch==2:
                srch.search_teacher()
            elif ch==3:
                srch.search_staff()
            else:
                print("You enter incorrect choice for functionality")
                m.mainmenu()
        elif choice==4:
            print("coming soon... Under Development")
        elif choice==5:
            res.view_result()
        elif choice==6:
            print("Download record for:-...."," ")
            print(" 1. Students")
            print(" 2. Teachers")
            print(" 3. Staff Members")
            ch=int(input("Enter choice of opertaion"))
            if ch==1:
                down.xl_student()
            elif ch==2:
                down.xl_teacher()
            elif ch==3:
                down.xl_staff()
            else:
                print("Sorry there is no operation for this choice. Try again..")
                m.mainmenu()
        elif choice==7:
            print("coming soon... Under Development")
        elif choice==8:
            print("Welcome to Library...")
            print(" 1. Add Book"," ")
            print(" 2. Issue Books")
            print(" 3. Return Books")
            print(" 4. Book  Detail")
            print(" 5. Delete Books")
            ch=int(input("please enter your choice"))
            if ch==1:
                lib.addbook()
            elif ch==2:
                lib.issuebook()
            elif ch==3:
                lib.retbook()
            elif ch==4:
                lib.bookdetail()
            elif ch==5:
                lib.delbook()
            else:
                print("Not a valid option")
                m.mainmenu()
        elif choice==9:
            exit()
        else:
            print("Sorry this is not a valid choice....")
            m.mainmenu()


m=main()
s=student()
teach=teacher()
st=staff()
res=result()
srch=search_record()
down=downrecord()
lib=library()



print("               Welcome to Project                 ","  ")
print("Please  enter id and password to continue  ","  ")
id =int(input("enter id "))
password=input("password")
a={}
conn=MongoClient('localhost',27017)
db=conn.college_project
collection_login=db.login
db.login.find({"password":password})
for post in collection_login.find():
    a=post
if id==a['id']:
    if password==a['password']:
        system('cls')
        m.mainmenu()
    else:
        print("Wrong Password")
        exit()
else:
    print("The ID doesn't seems to be correct!!! try again... ")

