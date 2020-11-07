from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
#from future import print


# set up 
ACCOUNT_NAME = "f5bdda05-9289-4541-9665-0290ff2dd594-bluemix"
API_KEY = "z_YFZaGQ3JmiXrLccCmqV8SeWxJz-SlMCiazZjB6aM6r"
serviceURL = "https://f5bdda05-9289-4541-9665-0290ff2dd594-bluemix.cloudantnosqldb.appdomain.cloud"

client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True)
# client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

#creating database within the service instance
databaseName = "our-database"
myDatabaseDemo = client.create_database(databaseName)

#checkking if database exists
if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(databaseName))

# Simple and full retrieval of the first document in the database.
result_collection = Result(myDatabaseDemo.all_docs, include_docs=True)
#print("Retrieved full document:\n{0}\n".format(result_collection[0]))

# prints out New York City, NY
#print("Location: {0}".format(result_collection[0][0].get("doc").get("location")))


def data_new_doc(data_name, client):
    databaseName = data_name
    myDatabase = client.create_database(databaseName)
    sampleData = [ 
                    ["Tim", "Albany, NY", {"masks": 100, "gloves": 600}] 
                ]

    for document in sampleData:
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

    result_collection = Result(myDatabase.all_docs)
    print("Retrieved minimal document:\n{0}\n".format(result_collection[0]))


    # Simple and full retrieval of the first
    # document in the database.
    result_collection = Result(myDatabase.all_docs, include_docs=True)
    print("Retrieved full document:\n{0}\n".format(result_collection[0]))


data_new_doc(databaseName, client)