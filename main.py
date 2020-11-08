from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask, request, render_template
from accounts import add_account, call_add_account
from inventory import call_inventory_doc
app = Flask(__name__)



@app.route("/Signup.html", methods=['GET', 'POST'])
def create_account_data():
    if request.method == "POST":
        account_info = []
        account_info.append(request.form["fname"])
        account_info.append(request.form["lname"])
        account_info.append(request.form["role"])
        account_info.append(request.form["hospital"])
        account_info.append(request.form["city"])
        account_info.append(request.form["state"])
        account_info.append(request.form["number"])
        call_add_account(account_info)
        return render_template("index.html")
    else:
        return render_template("Signup.html")

#if you are in root file, e
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def index2():
    return render_template("index.html")

@app.route("/home.html", methods=['GET', 'POST'])
def home():
    #return call_inventory_doc("our-database")
    return render_template("home.html")

@app.route("/myInventory.html")
def myInventory():
    return render_template("myInventory.html")

@app.route("/login.html")
def login():
    return render_template("login.html")
    
@app.route("/requests.html")
def requests():
    return render_template("requests.html")

@app.route("/data")
def data():
    return render_template("data.json")
        
if __name__ == "__main__":  
    app.run()