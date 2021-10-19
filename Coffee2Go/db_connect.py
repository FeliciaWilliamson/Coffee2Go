import pymongo
#connects to MongoDB and outputs the data in the terminal
client =pymongo.MongoClient('mongodb://127.0.0.1:27017')

mydb=client['Go2Coffee']

mycol = mydb['NewYork_CoffeeShops']
# Code to check that all data is in database
for x in mycol.find():
  print(x)   
  #Test case to add new data
  coffee_shop ={ "Name": "Stumptown Coffee Roasters", "Street Address": "18 W 29th St, New York, NY", "Zipcode": " 10001", "Latitude": "40.7169338","Longitude":"-74.013125" }
  n = mycol.insert_one(coffee_shop)
  print(n.inserted_id)