from flask import Flask, render_template, json, jsonify
import requests
import addressbook
from flask import request

app = Flask(__name__)


def getData():
    URL = 'https://randomuser.me/api/?results=25&nat=us'
    try:
        response = requests.get(URL, timeout = 5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

myAddressBook = addressbook.AddressBook()
jsonAddressData = getData() 

for contacts in jsonAddressData["results"]:
    newContacts = addressbook.Contact(contacts["name"]["first"],
        contacts["name"]["last"],
        contacts["email"],
        contacts["phone"],
        contacts["picture"]["medium"]
        )
    myAddressBook.addAddress(newContacts)

@app.route("/", methods = ["GET"])
def rawData():
    # return json.dumps([contacts.__dict__ for contacts in myAddressBook.getAllAddresses()])
    return render_template("index.html", addresses = myAddressBook.getAllAddresses())



@app.route("/search", methods = ["GET", "POST"])
def search():
    if request.method == "POST":
        searchStr = request.form.get('search')
    return render_template("index.html", addresses = myAddressBook.findAllMatching(searchStr))

if __name__ == "__main__":
    app.run()








## Activate: source addressbook/Scripts/activate
## Deactivate: deactivate
## To render template: under def hello(): return render_template('index.html)
## export FLASK_ENV=development