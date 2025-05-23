from flask import Flask, jsonify, render_template
import requests

def get_categories():
    return ["dev", "animal", "food", "sports", "outdoor"]
    # URL= "https://api.chucknorris.io/jokes/categories"
    # response = requests.get(URL)

    # if response.status_code == 200:
    #     data = response.json()
    #     return data
    # else:
    #     print(f'Fehler: {response.status_code}')

def get_joke_from_api(category):
    URL = "https://api.chucknorris.io/jokes/random?category={}".format(category)
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Fehler: {response.status_code}')

app = Flask(__name__)

@app.route('/joke/<string:category>')
def get_joke(category):
    return jsonify({"joke": get_joke_from_api(category)})

@app.route('/')
def index():
    return render_template("chuck.html", categories=categories)

if __name__ == '__main__':
    categories = get_categories()
    app.run(host="0.0.0.0", port=3333)