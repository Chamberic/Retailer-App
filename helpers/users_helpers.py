from pymysql.cursors import DictCursor 
from flaskext.mysql import MySQL 
from flask import Flask, session 
from flask_session import Session 
app = Flask (__name__)  
app.config.from_object(__name__)
Session (app)
DATABASE_NAME= "InventoryRentalManagement"
mysql = MySQL(
    app,
    prefix ="my_database",
    host ="localhost",
    user= "test",
    password = "test",
    DB = "InventoryRentalManagement",
    autocommit = True 
)

def valadateuser(details):
    try: 
        username = details["username"]
        password = deatails["password"]
        cur = mysql.get_db().cursor(DictCursor)
        print("Inside ValadateUser")
        cur.execute(
        "SELECT RoleID FROM users where username=%s and password=%s",
        (username,password),
        ) 
        userlist = (cur.fetchall)
        print ("userlist",userlist)
        cur.close() 
        session ["username "] = username 
        return userlist 

    except mysql.get_db().cursor.DatabaseError as e:
        print ("e")
        return e  
def getUserByID (username):
    try:    
        cur = mysql.get_db().cursor (DictCursor)
        cur.execute("SELECT * FROM users where username=%s") 
        userlist  = cur.fetchall()
        print ("userlist ",userlist)
        cur.close()
        return userlist 
    except mysql.get_db().cursor.DatabaseError as e:
        print ("e")
        return e  

def get_users():
    try: 
     cur = mysql.get_db().cursor (DictCursor)
     cur.execute ("SELECT * FROM users")
     userlist = cur.fetchall()
     print ("userlist",userlist)
     cur.close()
     return userlist 
    except mysql.get_db().cursor.DatabaseError as e:
        print ("e")
        return e  
def inseewuser(details):
    print (details)
    try: 
        roleType = details ["roleType"]
        userID = details  ['userID']
        fName = details ["fName"]
        lName =details ["lName"]
        password = details ["password"]
        email = details ["email"]
        ph = details ["ph"]
        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO Users(UserName,Password,FirstName.LastName,EmailID,Phone,RollID) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (UserID, password, fName, lName, email, ph, roleType), 
        )
        mysql.get_db().commit()
        cur.close()
        return "user " +userID + " user created"
    
    except mysql.get_db().cursor().DatabaseError as e:
        print(e) 
        return e 