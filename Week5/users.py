import requests

class User():
    def __init__(self, firstName, lastName, email, username, password, uuid):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.password = password
        self.uuid = uuid
    def __str__(self):
        return f'{self.firstName} {self.lastName} ({self.email})'
    def getFirstName(self):
        return self.firstName
    def setFirstName(self, firstName):
        self.firstName = firstName

class AuthorizedUsers():
    def __init__(self):
        self.authUsers = []
    def addUser(self, user):
        self.authUsers.append(user)
    def showUsers(self):
        n = 10
        for user in self.authUsers:
            print(user)

def getData(numUsers, nationality):
    URL = "https://randomuser.me/api/?results="+ str(numUsers) + "&nat" + nationality
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

users = AuthorizedUsers()
numUsersRequesting = 10
data = getData(numUsersRequesting, 'us')
response_API = requests.get('https://randomuser.me/api/?results=10&nat=us')

for user in data["results"]:
    newUser = User(user["name"]["first"],
        user["name"]["last"],
        user["email"],
        user["login"]["username"],
        user["login"]["password"],
        user["login"]["uuid"]
        )
    users.addUser(newUser)
    users.showUsers()