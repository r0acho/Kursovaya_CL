from flask import Flask, render_template, request, jsonify, make_response
import time
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("PUT YOUR CONNECTION STRING HERE")
db1 = client.prasim

res = db1.news.find().count()

app.config['JSON_AS_ASCII'] = False

all_news = list(db1.news.find().sort('_id', 1))
all_synonyms = list(db1.synonyms.find().sort('_id', 1))

db = []
db2 = []
db3 = []
posts = res  

quantity = 10

for item in all_news:
    news_title = item['headline']
    news_discription = item['text']
    news_link = item['url']
    news_date = item['time']
    db.append(["".join(news_title), "".join(news_discription), "".join(news_link), "".join(news_date)])

for item in all_synonyms:
    name = item['name']
    sinonim = item['synonym']
    db3.append(["".join(name), "".join(sinonim)])

@app.route("/")
def index():
    """ Route to render the HTML """
    return render_template("index.html")

@app.route("/synonym", methods=['GET', 'POST'])
def sinonim():
    return render_template("synonym.html")

@app.route("/load")
def load():
    """ Route to return the posts """

    time.sleep(0.2) 

    if request.args:
        counter = int(request.args.get("c"))  

        if counter == 0:
            print(f"Returning posts 0 to {quantity}")
           
            res = make_response(jsonify(db[0: quantity]), 200)

        elif counter == posts:
            print("No more posts")
            res = make_response(jsonify({}), 200)

        else:
            print(f"Returning posts {counter} to {counter + quantity}")
           
            res = make_response(jsonify(db[counter: counter + quantity]), 200)

    return res
@app.route("/load1")
def load1():
    """ Route to return the posts """

    time.sleep(0.2)  

    if request.args:
        counter = int(request.args.get("c"))  

        if counter == 0:
            print(f"Returning posts 0 to {quantity}")
            
            res = make_response(jsonify(db2[0: quantity]), 200)

        elif counter == posts:
            print("No more posts")
            res = make_response(jsonify({}), 200)

        else:
            print(f"Returning posts {counter} to {counter + quantity}")
            
            res = make_response(jsonify(db2[counter: counter + quantity]), 200)
    return res

@app.route("/load2")
def load2():
    """ Route to return the posts """

    time.sleep(0.2)  

    if request.args:
        counter = int(request.args.get("c"))  

        if counter == 0:
            print(f"Returning posts 0 to {quantity}")
            
            res = make_response(jsonify(db3[0: quantity]), 200)

        elif counter == posts:
            print("No more posts")
            res = make_response(jsonify({}), 200)

        else:
            print(f"Returning posts {counter} to {counter + quantity}")
            
            res = make_response(jsonify(db3[counter: counter + quantity]), 200)
    return res

if __name__ == '__main__':
    app.run(debug=True)