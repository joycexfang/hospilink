from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.adapters import Replay429Adapter
import json

# set up 
ACCOUNT_NAME = "f5bdda05-9289-4541-9665-0290ff2dd594-bluemix"
API_KEY = "z_YFZaGQ3JmiXrLccCmqV8SeWxJz-SlMCiazZjB6aM6r"

client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True, adapter=Replay429Adapter(retries=10, initialBackoff=0.01))
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
print("Retrieved full document:\n{0}\n".format(result_collection[0]))

# prints out New York City, NY
print(" Location: {0}".format(result_collection[0][0].get("doc").get("location")))

# open data.json
f = open('data.json', 'w')

# write to json file
f.write('[')

length = 0

for k in result_collection:
    length +=1


print (length)

for i in range(length):
    f.write(json.dumps(result_collection[i]))
    if i < 2:
        f.write(',')

f.write(']')

# close file
f.close()
