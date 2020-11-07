from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

# set up 
ACCOUNT_NAME = "f5bdda05-9289-4541-9665-0290ff2dd594-bluemix"
API_KEY = "z_YFZaGQ3JmiXrLccCmqV8SeWxJz-SlMCiazZjB6aM6r"

client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True)
# client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

databaseName = "our-database"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(databaseName))

# Simple and full retrieval of the first
# document in the database.
result_collection = Result(myDatabaseDemo.all_docs, include_docs=True)
print("Retrieved full document:\n{0}\n".format(result_collection[0]))