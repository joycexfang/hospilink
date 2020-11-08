from cloudant.client import Cloudant
from cloudant.result import Result, ResultByKey

from flask_table import Table, Col
from flask import render_template
#from db_setup import init_db, db_session





def call_inventory_doc(databaseName):
    # set up 
    ACCOUNT_NAME = "f5bdda05-9289-4541-9665-0290ff2dd594-bluemix"
    API_KEY = "z_YFZaGQ3JmiXrLccCmqV8SeWxJz-SlMCiazZjB6aM6r"

    #create client
    client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True)
    client.connect()

    #creating database within the service instance if not already exist
    #databaseName = "our-database"
    myDatabase = client.create_database(databaseName)

    result_collection = Result(myDatabase.all_docs, include_docs=True)
    #print("Retrieved full document:\n{0}\n".format(result_collection[0]))

    for doc in result_collection: 
        print(doc["id"])
    
    #qry = db_session.query(result_collection)
    #results = qry.all()

    #table = Results(results)
    #table.border = True
    #return render_template('home.html', table=table)
    
    #table.border = True
    
    #return render_template("home.html")

if __name__=="__main__":
    call_inventory_doc("our-database")



# https://www.blog.pythonlibrary.org/2017/12/14/flask-101-adding-editing-and-displaying-data/