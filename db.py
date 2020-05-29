import os
from firebase import firebase

_URL_DB = os.environ['BD_FIREBASE']
firebase = firebase.FirebaseApplication(_URL_DB, None)

result = firebase.get('/device/sensores', None)
print(type(result))

