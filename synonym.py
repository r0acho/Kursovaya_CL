from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import IDF
from pyspark.ml.feature import Word2VecModel
from pyspark.ml.feature import Word2Vec
from pprint import pprint
import re
import os
import datetime
import pymongo
from pymongo import MongoClient

PATH = '/home/vagrant/sema/lingva/lingva/'

spark = SparkSession \
    .builder \
    .appName("SimpleApplication") \
    .getOrCreate()

model = Word2VecModel.load(PATH)

client = MongoClient()
db = client.prasim

def get_synonyms(elements, count, model, spark_session):
    result = []
    for element in elements:
        try:
            elementDF = spark_session.createDataFrame([
                (element.lower().split(" "),)], ["words"])
            transform_elem = model.transform(elementDF)
            synonyms = model.findSynonyms(
                transform_elem.collect()[0][1], count).collect()
            result.append(synonyms)
        except Exception:
            result.append("Ничего не найдено")

    return result

with open("people.txt", "r") as myfile:
    data = myfile.readlines()
    for it in data:
        it = it.replace('\n', '')    
      

for name in data:
    name = name.replace('\n', '')
    for it in get_synonyms([name],5,model,spark)[0]:
        print(name)
        print(it[0])
        db.synonyms.insert_one({"name": name,"synonym": it[0]}) 

with open("places.txt", "r") as myfile:
    data = myfile.readlines()
    for it in data:
        it = it.replace('\n', '')    
        

for name in data:
    name = name.replace('\n', '')
    for it in get_synonyms([name],5,model,spark)[0]:
        print(name)
        print(it[0])
        db.synonyms.insert_one({"name": name,"synonym": it[0]}) 


spark.stop()