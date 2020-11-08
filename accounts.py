from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

from cloud2 import clear_all_documents
#call function when new account is created
def add_account(client, databaseName, account_info):
    #databaseName = "accounts"
    Database = client.create_database(databaseName)

    #[fname, lname, role, hospital, city, state, phone number]
    for data in account_info:
        firstName = data[0]
        lastName = data[1]
        role =data[2]
        hospital = data[3]
        city = data[4]
        state = data[5]
        phoneNumber = data[6]
        
        jsonDocument = {
            "firstName" : firstName,
            "lastName": lastName,
            "role": role,
            "hospital": hospital,
            "city": city,
            "state":state,
            "phoneNumber": phoneNumber
        }

        # Create a document using the Database API.
        Database.create_document(jsonDocument)


if __name__ == "__main__":  
    # set up 
    ACCOUNT_NAME = "f5bdda05-9289-4541-9665-0290ff2dd594-bluemix"
    API_KEY = "z_YFZaGQ3JmiXrLccCmqV8SeWxJz-SlMCiazZjB6aM6r"
    serviceURL = "https://f5bdda05-9289-4541-9665-0290ff2dd594-bluemix.cloudantnosqldb.appdomain.cloud"
  
    #create client
    client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True)
    client.connect()

    #creating database within the service instance
    databaseName = "accounts"
    myDatabaseDemo = client.create_database(databaseName)

    #checkking if database exists
    if myDatabaseDemo.exists():
        print("'{0}' successfully created.\n".format(databaseName))

    # Simple and full retrieval of the first document in the database.
    result_collection = Result(myDatabaseDemo.all_docs, include_docs=True)

    #[hospital, locationm dict of items]
    sampleData = [ 
                    ["John", "Smith", "doctor", "Samaritan", "Troy", "New York", 9000012342]
                ]

    #clear_all_documents(client, databaseName)
    add_account(client, databaseName, sampleData)



