from pymongo import MongoClient
import os

os.chdir('/home/vagrant/tomita-parser/build/bin')

client = MongoClient()
database = client["prasim"]
collection = database["news"]

# collection.update({}, {'$unset': {'Person': None}}, multi=True)
# collection.update({}, {'$unset': {'Object': None}}, multi=True)


for news in collection.find( {} ):
    with open("Arcticles.txt","w") as f:
        #print(news['text'])
        f.write(news['text'])

    os.system("./tomita-parser kr.proto")

    person = []
    object = []
    place = ""

    with open("output2.txt","r") as f:
        foutput = f.read()
        words = foutput.split()
        for i in range(len(words)):
            if words[i] == "Person_output":
                if words[i+2] not in person:
                    person.append(words[i+2])
            elif words[i] == "Object_output":
                while words[i+2] != "}":
                    place += " " + words[i+2]
                    i+=1
                if place not in object:
                    object.append(place)


    for i in range(len(person)):            
        collection.update({
                "_id": news["_id"]
            }, {
                "$pull": {
                "Person": person[i] 
                }
            }) 

    for i in range(len(object)):            
        collection.update({
                "_id": news["_id"]
            }, {
                "$pull": {
                "Object": object[i] 
                }
            }) 

    for i in range(len(person)):
        collection.update({
            "_id": news["_id"]
        }, {
            "$push": {
            "Person": person[i] 
            }
        }) 
    
    for i in range(len(object)):
        collection.update({
            "_id": news["_id"]
        }, {
            "$push": {
            "Object": object[i] 
            }
        }) 

    person.clear()
    object.clear()






