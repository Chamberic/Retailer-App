from flask import render_template,request,session 
from app import app
from helpers.users_helpers import valadateuser, getUserByID

@app.route("/") 
def index():
    return render_template("index.html")


@app.route("/menu", methods=["GET", "POST"])
def menu():
    if request.method=="POST":
        formData = request.form
        user = valadateuser(formData)
            
        if len(user) == 0:
            return render_template (
            "index.html",msg= "enter correct username and password")

        for ID in user:
            roleID == ID["RoleID"]

        if roleID == 1:
            username = session ["username"]
            userinfo = getUserByID(username)
            return render_template("admin/menu.html",msg = userinfo)         
        elif roleID == 2:
            username = session ["username"]
            userinfo = getUserByID ["username"]
            return render_template("admin/menu.html",msg = userinfo)
        elif roleID == 3:
            username = session ["username"]
            userinfo = getUserByID ["username"]
            return render_template("admin/menu.html",msg = userinfo)
        else:  
            return render_template("/index.html", msg = "enter correct password")
    else:
        render_template("/index.html")
        
@app.route("/equipment", methods=["GET"])
def equipment():
    return render_template("/admin/equipment.html")
from helpers.inventory_helpers import getequipments, insert_equipment

@app.route("/viewequipments", methods=["GET","POST"])
def viewequipments():
        equipmentlist = getequipments
        return render_template("admin/viewequipments.html", msg=equipmentlist)

@app.route("/viewusers")
def viewusers():
        userlist = viewusers
        return render_template("admin/viewusers.html", msg=viewusers)

@app.route("/addusers")
def addusers():
        return render_template("admin/adduser.html", msg=adduser)

@app.route("/addequipment", methods=["POST"])
def addequipment():
     if request.method == "POST":
        details = request.form
        result = insertequipments(details)
        return render_template("admin/addequipment", msg=result)
@app.route("/newuser", methods=["POST"])
def newuser():
     if request.method == "POST":
        details = request.form
        result = insertnewuser(details)
        return render_template("admin/adduser.html", msg=result)    
@app.route("/logout", methods=["GET"]) 
def logout():
    session.pop("username",None)
    return render_template("index.html")