from cloudant.client import Cloudant

#call function when new account is created
def add_account(client, databaseName, data):
    #databaseName = "accounts"
    Database = client.create_database(databaseName)

    #[fname, lname, role, hospital, city, state, phone number]
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

def call_add_account(account_info):
    # set up 
    ACCOUNT_NAME = "f5bdda05-9289-4541-9665-0290ff2dd594-bluemix"
    API_KEY = "z_YFZaGQ3JmiXrLccCmqV8SeWxJz-SlMCiazZjB6aM6r"

    #create client
    client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True)
    client.connect()

    #creating database within the service instance if not already exist
    databaseName = "accounts"
    client.create_database(databaseName)

    add_account(client, databaseName, account_info)