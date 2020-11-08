from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
#from future import print


def data_new_doc(databaseName, client, data):
    #databaseName = data_name
    myDatabase = client.create_database(databaseName)


    for document in data:
        hospitalname = document[0]
        location = document[1]
        resources = document[2]

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
    client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True)
    client.connect()

    #creating database within the service instance
    databaseName = "our-database"
    myDatabaseDemo = client.create_database(databaseName)

    #checkking if database exists
    if myDatabaseDemo.exists():
        print("'{0}' successfully created.\n".format(databaseName))

    # Simple and full retrieval of the first document in the database.
    result_collection = Result(myDatabaseDemo.all_docs, include_docs=True)

    #[hospital, locationm dict of items]
    sampleData = [ 
                    ["Tim", "Albany, NY", {"masks": 100, "gloves": 600}], 
                    ["Sally", "New York City, NY", {"masks": 100, "gloves": 600}], 
                    ["Timmy", "New York City, NY", {"masks": 100, "gloves": 600}] 
                ]

    clear_all_documents(client, databaseName)
    data_new_doc(databaseName, client, sampleData)

