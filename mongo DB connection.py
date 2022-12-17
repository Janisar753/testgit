import pymongo
client = pymongo.MongoClient("mongodb+srv://Janisar:Rubina786@cluster0.p0dnstl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name":"janisar",
    "email": "janisargaddi@gmail.com",
    "mobile" :"phone"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)