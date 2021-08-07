import pymongo
#connects to MongoDB and outputs the data in the terminal
client =pymongo.MongoClient('mongodb://127.0.0.1:27017')

mydb=client['Go2Coffee']

mycol = mydb['CoffeeShops']

for x in mycol.find():
  print(x)   
  
