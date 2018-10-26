import json
from pymongo import MongoClient
from pprint import pprint

with open('winemag-data-130k-v2.json', 'r') as source:
  wines = json.load(source)

client = MongoClient('mongodb://localhost:32769')
db = client['wines']
winesCollection = db.create_collection('wines')
winesCollection.insert_many(wines)

with open('wines.system.json', 'r') as source:
  sys_funcs = json.load(source)

sys_col =  db['system.js']
for func in sys_funcs:
  sys_col.save(func)

print('Migration finished')