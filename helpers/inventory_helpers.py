from flask import Flask
from flaskext.mysql import MySQL 
from pymysql.cursors import DictCursor

app = Flask (__name__)
mysql = MySQL (
    app, 
    prefix = "my_database",
    host = "localhost",
    user = "test",
    password = "test",
    db = "InventoryRentalManagement",
    autocommit = True 
)
def getequipments():
    try:
        cur = mysql.get_db().cursor(DictCursor)
        cur.execute("SELECT * FORM EQUEPMENT WHERE quantity >0")
        equipmentlist = cur.fetchall()
        print ("equepmentlist ", equipmentlist)
        cur.close()
        return equepmentlist
    except mysql.get_db.cursor.DatabaseError as e:
        print (e) 
        return e 
def insert_equipment (details):
    try: 
        EquepmentType = details ["EquepmentType"]
        Name = details ["Name"]
        SKU = details ["SKU"]
        Discription = details ["discription"]
        AvailableFrom = details ["AvailableFrom"] 
        Quantity = details ["Quantity"]
        EstimatedCost = details ["EstimatedCost"]
        cur = mysql.get_db().cursor()
        cur.execute( "INSERT INTO equipment(EquipmentType, Name,SKU ,Discription, AvailableFrom, Quantity, EstimatedCost) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            (EquepmentType, Name,SKU ,Discription, AvailableFrom, Quantity, EstimatedCost),
        )

        mysql.get_db().commit()
        cur.close()
        return "equipment inserted successfully"
        
    except mysql.get_db().cursor().DatabaseError as e: 
        print(e) 
        return e 




