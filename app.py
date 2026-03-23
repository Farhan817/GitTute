import json
from flask import Flask, request ,render_template
from dotenv import load_dotenv
import pymongo
import os 

load_dotenv()


MONGO_URL = os.getenv('MONGO_URL')

client = pymongo.MongoClient(MONGO_URL)

db = client.test
collection= db['user']

app = Flask(__name__)

def serialize_docs(docs):
    return [
        {**doc, "_id": str(doc["_id"])}
        for doc in docs
    ]


@app.route("/api")
def get_data():
    file_path = "dummy.json"
    file = open(file_path, "r")
    return json.load(file)


@app.route("/api/add", methods=["POST"])
def add_data():
    payload = request.get_json()
    file_path = "dummy.json"
    file_read = open(file_path, "r")
    content = json.load(file_read)
    content.append(payload)
    file_write = open(file_path, "w")
    json.dump(content, file_write, indent=4)

    return content

@app.route("/signup")
def signup():
    return render_template('index.html')
@app.route("/complete")
def complete():
    return render_template('complete.html')
    
    
@app.route("/api/submit", methods=["POST"])
def submit():
    form_data= request.get_json()    
    print("form_data",form_data)
    collection.insert_one(form_data)
    return {
        'message':True
    }



if __name__ == "__main__":

    app.run(debug=True)
