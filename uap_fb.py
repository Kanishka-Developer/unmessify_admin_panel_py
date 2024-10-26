import firebase_admin, json
from firebase_admin import credentials
from firebase_admin import db

class FirebaseClient():
    def __init__(self):
        self.cred = credentials.Certificate("xxxxx-firebase-serviceAccountKey.json")
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': 'https://xxxxx-default-rtdb.firebaseio.com'
        })
        self.ref = db.reference('Unmessify')

    def get(self, key):
        return self.ref.child(key).get()

    def update(self, key, value):
        self.ref.child(key).update(value)

if __name__ == "__main__":
    print("Don't run this file directly. Run main.py instead.")
