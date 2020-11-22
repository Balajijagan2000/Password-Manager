# Password-Manager
Password Manager is one of the commonly used applications worldwide. It simply stores username,passwords etc., of other applications.The stored details can be accessed anytime. It is difficult to memorize  username and passwords for all apps, so password manager comes into play.With use of password manager we no need to memorize username and passwords of other apps.
# Python Module Installation:
1.Installing psycopg2:Open CMD as admin and type the following:pip install psycopg2 

If any error occurs in "<b>pip install psycopg2</b>" use "<b>python -m pip install psycopg2"</b>

2.Installing PIP(pillow):Open CMD as admin and type the following:<b>"pip install pillow"</b> in case any error use <b>"python -m pip install pillow"</b>


<b>This application is built to work on postgresql, so it requires postgresql database to work:</b>
# Downloading Postgresql:
1.Go to the Link: <a href="https://www.postgresql.org/" target="_blank"> https://www.postgresql.org/</a>

2.Click on <b>Download</b>

3.Choose the <b>Operating System</b>and click on <b>Download the installer</b>

4.Based of the operating system and architecture install the required version

5.Direct link to download postgresql:<a href="https://www.enterprisedb.com/downloads/postgres-postgresql-downloads" target="_blank">https://www.enterprisedb.com/downloads/postgres-postgresql-downloads</a>
# Postgresql Installtion:
1.Download Postgres Installer using above links.

2.Click on the downloaded executable file to run the installer.

3.Select your preferred language.

4.PGInstaller GUI installer, install postgresql.

5.Specify directory where you want to install PostgreSQL.

6.Specify PostgreSQL server port. You can leave this as default if you’re unsure what to enter.

7.Create a PostgreSQL user password.

8.Create password for database Superuser.

9.Click next to begin PostgreSQL installation.

# Setting up the application:
       
# Directory
            PasswordManager(Mainfolder)
                  |
        |---------|----------|
        |                    |
    PasswordManager.py       Image.jpg

# Changes to be made in code before executing:
1.In "try" block under "db connectivity(commented in code)",enter your postgresql "dbname","user" ,"host","password"
<b>Example:conn=psycopg2.connect("dbname='< >' user='< >' host='< >' password='< >' ")</b>
Find this line and enter your postgresql dbname,user,host,password inside the single coats

2.Under "Opening Screen(commented in code)" find the line <b>"image1=ImageTk.PhotoImage(Image.open("E:\Python project Password Manager\Image.jpg"))"</b> and replace the image path with the absolute path of the image location in your system.
  
 ![First Window 1](Reference Images/img2.png)

                              
      
      


