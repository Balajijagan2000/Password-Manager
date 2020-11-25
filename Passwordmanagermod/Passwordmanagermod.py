#import psycopg2
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk,Image

#db connectivity
try:
      conn=sqlite3.connect('passwordmanager.db')
      print("Connected to database.....")
      
except IOError:
      print(IOError)
#db object initializaion
cursor1=conn.cursor()
 
#Opening Screen

root=Tk()
root.title("Password Vault")
canvas=Canvas(root,bg='black',width=500,height=500)
image1=ImageTk.PhotoImage(Image.open("Image.jpg"))

canvas.create_image(0,0,anchor=NW,image=image1)
canvas.pack()

userwidth5=500
userheight5=500

mainscrnwidth=root.winfo_screenwidth()
mainscrnheight=root.winfo_screenheight()

xcoor5=(mainscrnwidth/2)-(userwidth5/2)
ycoor5=(mainscrnheight/2)-(userheight5/2)
root.geometry("%dx%d+%d+%d"%(userwidth5,userheight5,xcoor5,ycoor5))
root.resizable(False,False)

root.after(3000,lambda:root.destroy())
root.mainloop()
#First Window
users=Tk()
users.title("Password Vault")
#to centre the user window 
userwidth=300
userheight=300

mainscrnwidth=users.winfo_screenwidth()
mainscrnheight=users.winfo_screenheight()

xcoor=(mainscrnwidth/2)-(userwidth/2)
ycoor=(mainscrnheight/2)-(userheight/2)

users.geometry("%dx%d+%d+%d"%(userwidth,userheight,xcoor,ycoor))
users.resizable(False,False)
users['background']='#8bcdcd'







#Button Styles
style=Style()
style.configure('W.TButton', font =('Helvetica', 10,'bold'),foreground="black",background="#3797a4",padding=3 )
          

                 
flag=0
count=0 
def clicked():

      style=Style()
      style.configure('W.TButton', font =('Helvetica', 10,'bold'),foreground="black",background="#3797a4",padding=3 )

    
      def clicked2():


            if(pwdtxt.get()==cnfpwdtxt.get()):


                  cursor1.execute('''CREATE TABLE IF NOT EXISTS userlogin(uid INTEGER PRIMARY KEY,username text,pswd text) ''')
                  cursor1.execute('''SELECT username from userlogin''')

                  conn.commit()
                  data=cursor1.fetchall()
                  
                  if(len(data)!=0):


            
                        for i in data:
                              
                              
                              if unametxt.get() in i:
                                    global flag
                                    flag=1
                                    break
                            
                        if flag==1:

                              messagebox.showinfo("Alert","Username Already Exists/Please enter another name")     
                              pwdtxt.delete(0,END)
                              unametxt.delete(0,END)
                              cnfpwdtxt.delete(0,END)       
                        else:

                              if(unametxt.get()!="" and pwdtxt.get()!=""):


                                    #cursor1.execute('''INSERT INTO userlogin(username,pswd) Values(%s,%s)''',(unametxt.get(),pwdtxt.get()))
                                    cursor1.execute('''INSERT INTO userlogin(username,pswd) Values(:username,:pswd)''',{'username':unametxt.get(),'pswd':pwdtxt.get()})
                                    conn.commit()
                                    messagebox.showinfo("Information","Account Created Successfully")
                                    pwdtxt.delete(0,END)
                                    unametxt.delete(0,END)
                                    cnfpwdtxt.delete(0,END)
                                    messagebox.showinfo("Information","Please Click the 'Signin Button'")
                                    #break
                              else:
                                    messagebox.showinfo("Empty Fields Detectd","Please fill all fields/Enter correct values")
                                    #break

                  else:
                        if(unametxt.get()!="" and pwdtxt.get()!=""):

                              #cursor1.execute('''INSERT INTO userlogin(username,pswd) Values(%s,%s)''',(unametxt.get(),pwdtxt.get()))
                              cursor1.execute('''INSERT INTO userlogin(username,pswd) Values(:username,:pswd)''',{'username':unametxt.get(),'pswd':pwdtxt.get()})
                              conn.commit()
                              pwdtxt.delete(0,END)
                              unametxt.delete(0,END)
                              cnfpwdtxt.delete(0,END)
                              messagebox.showinfo("Information","Account Created Successfully")
                              messagebox.showinfo("Information","Please Click the 'Signin Button'")
                              
                              
                        else:
                              messagebox.showinfo("Empty Fields Detectd","Please fill all fields/Enter correct values")

            else:


                  messagebox.showinfo("Warning","Password and Confirmpassword Doesn't match")
                  
            

           

      #newuser window
      global newuser
      newuser=Tk()
      newuser.title("Password Manager")

      #To center the newuser window

      userwidth2=400
      userheight2=400

      mainscrnwidth2=newuser.winfo_screenwidth()
      mainscrnheight2=newuser.winfo_screenheight()

      xcoor2=(mainscrnwidth2/2)-(userwidth2/2)
      ycoor2=(mainscrnheight2/2)-(userheight2/2)

     
      newuser.geometry("%dx%d+%d+%d"%(userwidth2,userheight2,xcoor2,ycoor2))
      newuser.resizable(False,False)
      
      #newuserbackground color
      newuser['background']='#8bcdcd'
      
      

      uname=Label(newuser,text="Username:",font=("Helvetica Bold",14),background="#8bcdcd").pack(padx=10,pady=10)
      unametxt=Entry(newuser,width=20,font=("Helvetica",18))
      unametxt.pack(padx=10,pady=10)
      pwd=Label(newuser,text="Password:",font=("Helvetica Bold",14),background="#8bcdcd").pack(padx=10,pady=10)
      bullet = "\u2022"
      pwdtxt=Entry(newuser,width=20,font=('Helvetica Bold', 18),show=bullet)
      pwdtxt.pack(padx=10,pady=10)
      cnfpwd=Label(newuser,text="Confirm Password:",font=("Helvetica Bold",14),background="#8bcdcd").pack(padx=10,pady=10)
      cnfpwdtxt=Entry(newuser,width=20,show=bullet,font=("Helvetica Bold",18))
      cnfpwdtxt.pack(padx=10,pady=10)

      
      btncreate=Button(newuser,text="Create Account",style="W.TButton",command=clicked2).pack(padx=10,pady=10)
      newuser.mainloop()


    
    


#Login Screen window
def clicked1():
      users.destroy()
      
      global login
      login=Tk()
      login.title("Password Manager")
      #to center login window 
      userwidth3=300     #300
      userheight3=300    #250

      mainscrnwidth3=login.winfo_screenwidth()
      mainscrnheight3=login.winfo_screenheight()

      xcoor3=(mainscrnwidth3/2)-(userwidth3/2)
      ycoor3=(mainscrnheight3/2)-(userheight3/2)

      login.geometry("%dx%d+%d+%d"%(userwidth3,userheight3,xcoor3,ycoor3))
      login.resizable(False,False)
      

      #login screen background color
      login['background']='#8bcdcd'

      uname=Label(login,text="Username:",font=("Helvetica Bold",14),background="#8bcdcd").pack(padx=10,pady=10)
      unametxt=Entry(login,width=20,font=("Helvetica",18))
      unametxt.pack(padx=10,pady=10)
      pwd=Label(login,text="Password:",font=("Helvetica Bold",14),background="#8bcdcd").pack()
      bullet = "\u2022"
      pwdtxt=Entry(login,width=20,font=('Helvetica Bold', 18),show=bullet)
      pwdtxt.pack(padx=10,pady=10)
      

      
      #Main Window Password Manager
      
      
      def clicked3():
            
            if(unametxt.get()!="" and pwdtxt.get()!=""):
                  
                  #to check the entered username or password is correct
                  cursor1.execute('''SELECT username,pswd from userlogin''')
                  conn.commit()
                  data1=cursor1.fetchall() 
                  
                    
                  for j in data1:

                        
                        if(j[0]==unametxt.get() and j[1]==pwdtxt.get()):

                              unametxt.delete(0,END)
                              pwdtxt.delete(0,END)
                              login.withdraw()
                              messagebox.showinfo("Alert","Login Successfull")
                              
                              pswdmgr=Tk()
                              
                              pswdmgr.title("Password Vault")
                              #to center password manager window 
                              userwidth1=600    #600
                              userheight1=700   #500
                              

                              mainscrnwidth1=pswdmgr.winfo_screenwidth()
                              mainscrnheight1=pswdmgr.winfo_screenheight()


                              xcoor1=(mainscrnwidth1/2)-(userwidth1/2)
                              ycoor1=(mainscrnheight1/2)-(userheight1/2)


                              
                              pswdmgr.geometry("%dx%d+%d+%d"%(userwidth1,userheight1,xcoor1,ycoor1))
                              pswdmgr.resizable(False,False)      
                              #pswdmgr bg color
                              pswdmgr['background']='#8bcdcd'

                              
                              
                              def savefn():




                                    
                                    
                                    doname=dnametxt.get()
                                    username1=punametxt.get()
                                    password=ppwdtxt.get()
                                    if(doname!="" and username1!="" and password!=""):







                                          
                  
                                          
                                          #cursor1.execute('''CREATE TABLE IF NOT EXISTS passwordmanager(id INTEGER PRIMARY KEY,DomainName Varchar(30),Username Varchar(20),pswd Varchar(20))''')
                                          cursor1.execute('''CREATE TABLE IF NOT EXISTS passwordmanager(id INTEGER PRIMARY KEY,DomainName text,Username text,pswd text)''')
                                          conn.commit()
                                          #cursor1.execute('''INSERT INTO passwordmanager(DOMAINNAME,USERNAME,PSWD) VALUES(%s,%s,%s)''',(doname,username1,password))
                                          cursor1.execute('''INSERT INTO passwordmanager(DOMAINNAME,USERNAME,PSWD) VALUES(:DomainName,:Username,:Pswd)''',
                                                          {'DomainName':doname,'Username':username1,'Pswd':password})

                                          conn.commit()
                                          dnametxt.delete(0,END)
                                          punametxt.delete(0,END)
                                          ppwdtxt.delete(0,END)
                                          messagebox.showinfo("Information","Details Added!")
                                          
                                          
                                    else:

                                          messagebox.showinfo("Empty Fields Detected","Please Enter all values/correct values")
                                    
                              #display fn to displaye all saved passwords
                              
                              def display():
                                    global displaywindow
                                    displaywindow=Tk()
                                    displaywindow.title("Password Vault")
                                    #to centre the display window
                                    userwidth4=800    #800
                                    userheight4=400   #400

                                    mainscrnwidth4=displaywindow.winfo_screenwidth()
                                    mainscrnheight4=displaywindow.winfo_screenheight()

                                    xcoor4=(mainscrnwidth4/2)-(userwidth4/2)
                                    ycoor4=(mainscrnheight4/2)-(userheight4/2)

                                    displaywindow.geometry("%dx%d+%d+%d"%(userwidth4,userheight4,xcoor4,ycoor4))

                                    

                                    

                                    displaywindow.resizable(False,False)
                                    #displaywindow bg color
                                    displaywindow['background']='#8bcdcd'
                                    frm=Frame(displaywindow)
                                    frm.pack(padx=10,pady=10)
                                    cursor1.execute('''SELECT * FROM passwordmanager''')
                                    conn.commit()
                                    data2=cursor1.fetchall()
                                    table=ttk.Treeview(displaywindow,columns=(1,2,3,4),show="headings",height="5")
                                    table.pack()

                                    table.heading(1,text="UserId")
                                    table.heading(2,text="App")
                                    table.heading(3,text="Username")
                                    table.heading(4,text="Password")
                                    for row in data2:
                                          table.insert("","end",value=row)
                                    displaywindow.mainloop()

                              def exitfn1():
                                    messagebox.showinfo("Information","Thank You!!")
                                    pswdmgr.destroy()
                                    
                                    newuser.withdraw()
                                    conn.close()
                                    sys.exit()
                                    
                              def deletion():
                                    cursor1.execute('''SELECT * FROM passwordmanager''')
                                    check=cursor1.fetchall()
                                    if(deletetxt.get()==""):
                                          messagebox.showinfo("Alert","Please Enter the ID")
                                          
                                    elif(len(check)==0):
                                        messagebox.showinfo("Alert","No data found or no details saved")
                                    else:

                                          #cursor1.execute('''DELETE FROM passwordmanager WHERE id=%s''',(deletetxt.get(),))
                                          cursor1.execute('''DELETE FROM passwordmanager WHERE id=:id''',{'id':deletetxt.get()})
                                          conn.commit()
                                          messagebox.showinfo("Alert","Removed..")
                                          deletetxt.delete(0,END)
                              def update():
                                    #cursor1.execute('''SELECT * FROM passwordmanager WHERE id=%s''',(updatetxt.get(),))
                                    cursor1.execute('''SELECT * FROM passwordmanager WHERE id=:id''',{'id':updatetxt.get()})
                                    conn.commit()
                                    dat=cursor1.fetchone()
                                    if(updatetxt.get()==""):
                                          messagebox.showinfo("Alert","Please Enter ID to update")
                                    else:
                                          upwin=Tk()
                                          width4=300    #800
                                          height4=300   #400

                                          upwinwidth=upwin.winfo_screenwidth()
                                          upwinheight=upwin.winfo_screenheight()

                                          xcoorupwin=(upwinwidth/2)-(width4/2)
                                          ycoorupwin=(upwinheight/2)-(height4/2)

                                          upwin.geometry("%dx%d+%d+%d"%(width4,height4,xcoorupwin,ycoorupwin))
                                          upwin.resizable(False,False)
                                          #displaywindow bg color
                                          upwin['background']='#8bcdcd'
                                          upwin.title("Password Vault")
                                          
                                          appname=Label(upwin,text="App Name:",font=("Helvetica bold",14),background="#8bcdcd")
                                          appname.place(x=30,y=50)
                                          appnametxt=Entry(upwin,width=13,font=("Helvetica",14))
                                          appnametxt.place(x=140,y=50)
                                          appnametxt.insert(0,dat[1])
                                          

                                          urname=Label(upwin,text="Username:",font=("Helvetica bold",14),background="#8bcdcd")
                                          urname.place(x=30,y=90)
                                          urnametxt=Entry(upwin,width=13,font=("Helvetica",14))
                                          urnametxt.place(x=140,y=90)
                                          urnametxt.insert(0,dat[2])

                                          uppwd=Label(upwin,text="Password:",font=("Helvetica bold",14),background="#8bcdcd")
                                          uppwd.place(x=30,y=130)
                                          uppwdtxt=Entry(upwin,width=13,font=("Helvetica",14))
                                          uppwdtxt.place(x=140,y=130)
                                          uppwdtxt.insert(0,dat[3])


                                          def modify():
                                                #cursor1.execute('''UPDATE passwordmanager SET DomainName=%s,Username=%s,pswd=%s WHERE id=%s''',(appnametxt.get(),urnametxt.get(),uppwdtxt.get(),updatetxt.get(),))
                                                cursor1.execute('''UPDATE passwordmanager SET DomainName=:DomainName,Username=:Username,pswd=:pswd WHERE id=:id''',
                                                                {'DomainName':appnametxt.get(),'Username':urnametxt.get(),'pswd':uppwdtxt.get(),'id':updatetxt.get()})
                                                conn.commit()
                                                messagebox.showinfo("Information","Details Updated")
                                                updatetxt.delete(0,END)
                                                upwin.destroy()

                                          upwinbtn=Button(upwin,text="Update",style="W.TButton",command=modify).place(x=120,y=175)

                                          upwin.mainloop()


                                          

                                          
                              
                                          
                                          
                              dname=Label(pswdmgr,text="App Name:",font=("Helvetica bold",14),background="#8bcdcd").pack(padx=10,pady=10)
                              bullet = "\u2022"
                              dnametxt=Entry(pswdmgr,width=20,font=("Helvetica",14))
                              dnametxt.pack(padx=10,pady=10)
                              puname=Label(pswdmgr,text="User Name:",font=("Helvetica bold",14),background="#8bcdcd").pack(padx=10,pady=10)
                              punametxt=Entry(pswdmgr,width=20,font=("Helvetica",14))
                              punametxt.pack(padx=10,pady=10)
                              ppwd=Label(pswdmgr,text="Password:",font=("Helvetica bold",14),background="#8bcdcd").pack(padx=10,pady=10)
                              ppwdtxt=Entry(pswdmgr,width=20,font=("Helvetica",14),show=bullet)
                              ppwdtxt.pack(padx=10,pady=10)
                              pbtn=Button(pswdmgr,text="Save",style="W.TButton",command=savefn).pack(padx=10,pady=10)
                              dbtn=Button(pswdmgr,text="Show All App",style="W.TButton",command=display).pack(padx=10,pady=10)
                              
                             
                             
                              
                              

                              

                              dbtn=Button(pswdmgr,text="Exit",style="W.TButton",command=exitfn1).pack(padx=10,pady=10)

                              deletelabel=Label(pswdmgr,text="Updation",font=("Helvetica bold",14),background="#8bcdcd").pack(padx=10,pady=10)
                             
                              deletebtn=Button(pswdmgr,text="Delete",style="W.TButton",command=deletion).place(x=183,y=500)



                              deletetxt=Entry(pswdmgr,width=15,font=("Helvetica",14))
                              deletetxt.place(x=280,y=500)
                              
                              updatebtn=Button(pswdmgr,text="Update",style="W.TButton",command=update).place(x=183,y=550)
                              updatetxt=Entry(pswdmgr,width=15,font=("Helvetica",14))
                              updatetxt.place(x=280,y=550)


                              pswdmgr.mainloop()
                              break
                        else:
                              global count
                              count=count+1
                              
                              if(count==len(data1)):
                                    messagebox.showinfo("Warning","Username or Password doesn't found")
                                    count=0
                                    break
                              
                              continue
                        
                         
                              
                                
                               
      
            else:
                  messagebox.showinfo("Empty Fields Detected","Please Enter all values/correct values")




           
            
            
            

      
      



                  
      btnlogin=Button(login,text="Login",style="W.TButton",command=clicked3).pack(padx=10,pady=10)
      login.mainloop()
      
def exitfn():
      users.destroy() 
      

#buttons in users window
btn1=Button(users,text="New User",style="W.TButton",command=clicked).pack(side=TOP,expand=YES)
btn2=Button(users,text="Signin",style="W.TButton",command=clicked1).pack(side=TOP,expand=YES)
btnexit=Button(users,text="Exit",style="W.TButton",command=exitfn).pack(side=TOP,expand=YES)




users.mainloop()




