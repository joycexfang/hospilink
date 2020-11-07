from __future__ import print_function

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

# set up 
ACCOUNT_NAME = "f5bdda05-9289-4541-9665-0290ff2dd594-bluemix"
API_KEY = "z_YFZaGQ3JmiXrLccCmqV8SeWxJz-SlMCiazZjB6aM6r"

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
print("Retrieved full document:\n{0}\n".format(result_collection[0]))

# prints out New York City, NY
print("Location: {0}".format(result_collection[0][0].get("doc").get("location")))



# write-html.py

# f = open('index.html', 'a')

# message = '<p>hello world</p>'

# f.write(message)
# f.close()


html_str = """
<table>
     <tr>
       <th>Number</th>
       <th>Square</th>
     </tr>
     <indent>
     <% for i in range(10): %>
       <tr>
         <td><%= i %></td>
         <td><%= i**2 %></td>
       </tr>
     </indent>
</table>
"""

html_file= open("index.html","w")
html_file.write(html_str)
html_file.close()