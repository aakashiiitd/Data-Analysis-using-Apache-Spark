import json
import csv
import pandas as pd
import pymongo
# # Open the CSV
# f = open( 'important-repos1.csv', 'r+' )
# # Change each fieldname to the appropriate field name. I know, so difficult.
# reader = csv.DictReader( f, fieldnames = ( 'id','url','owner_id','name','language','created_at','forked_from','deleted','updated_at'))
# # Parse the CSV into JSON
# out = json.dumps( [ row for row in reader ] )
# print ("JSON parsed!")
# # Save the JSON
f = open( 'ghtorrent-logs.json', 'r')
data = json.load(f)
#f.write(out)
#print ("JSON saved!" )
mng_client = pymongo.MongoClient('localhost', 27017)
mng_db = mng_client['BDA_2'] # Replace mongo db name
collection_name = 'ghtorrent' # Replace mongo db collection name
db_cm = mng_db[collection_name]
print(mng_client.list_database_names())
print(mng_db.list_collection_names())
#db_cm.delete_many()
db_cm.insert_many(data)
print("yay")
