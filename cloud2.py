from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.adapters import Replay429Adapter
#from future import print


def data_new_doc(databaseName, client, data):
    #databaseName = data_name
    myDatabase = client.create_database(databaseName)


    for document in data:
        hospitalname = document.get("name")
        location = document.get("location")
        resources = document.get("resources")

        jsonDocument = {
            "hospitalname": hospitalname,
            "location": location,
            "resources": resources
        }

        # Create a document using the Database API.
        newDocument = myDatabase.create_document(jsonDocument)

        # Check that the document exists in the database.
        if newDocument.exists():
            print("Document successfully created.")

def clear_all_documents(client, databaseName):
    '''
    clears all document
    '''
    try :
        client.delete_database(databaseName)
    except CloudantException:
        print("There was a problem deleting '{0}'.\n".format(databaseName))
    else:
        print("'{0}' successfully deleted.\n".format(databaseName))

if __name__ == "__main__":  
    # set up 
    ACCOUNT_NAME = "f5bdda05-9289-4541-9665-0290ff2dd594-bluemix"
    API_KEY = "z_YFZaGQ3JmiXrLccCmqV8SeWxJz-SlMCiazZjB6aM6r"
    serviceURL = "https://f5bdda05-9289-4541-9665-0290ff2dd594-bluemix.cloudantnosqldb.appdomain.cloud"

    #create client
    client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True, adapter=Replay429Adapter(retries=10, initialBackoff=0.01))
    client.connect()

    #creating database within the service instance
    databaseName = "our-database"
    myDatabaseDemo = client.create_database(databaseName)

    #checking if database exists
    if myDatabaseDemo.exists():
        print("'{0}' successfully created.\n".format(databaseName))

    # Simple and full retrieval of the first document in the database.
    result_collection = Result(myDatabaseDemo.all_docs, include_docs=True)

    #[hospital, locationm dict of items]
    sampleData = [ 
                    {"name": "Tim", "location": "Albany, NY", "resources": {"masks": 1000, "gloves": 600}},
                    {"name": "Sally", "location": "New York City, NY", "resources": {"masks": 800, "gloves": 900}},
                    {"name": "Timmy", "location": "New York City, NY", "resources": {"masks": 300, "gloves": 2000}}
                ]

    clear_all_documents(client, databaseName)
    data_new_doc(databaseName, client, sampleData)

