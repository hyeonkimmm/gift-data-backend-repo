import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
# 경덕
cred = credentials.Certificate('../data/info/atte2gd-eb088-firebase-adminsdk-bftoy-36320b017e.json')
cred = credentials.Certificate('data/info/atte2gd-eb088-firebase-adminsdk-bftoy-36320b017e.json')

# 재희
cred = credentials.Certificate('../data/info/atte2jh-firebase-adminsdk-27fq5-24afbf0bb4.json')
cred = credentials.Certificate('data/info/atte2jh-firebase-adminsdk-27fq5-24afbf0bb4.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1811
})


data = {
    'name': 'Los Angeles',
    'state': 'CA',
    'country': 'USA'
}
final = dict()
db.collection(u'daily').document(u'result').set(final)
# create collection
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

# create another document
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})

# read data
users_ref = db.collection(u'daily')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

get_docs = users_ref.get()
for doc in get_docs:
    if doc.exists:
        print(f'Document data: {doc.to_dict()}')
        test = doc.to_dict()
    else:
        print(u'No such document!')
# get document
a_lovelace_ref = db.collection(u'users').document(u'alovelace')
# get collection
users_ref = db.collection(u'users')
# get document with /
a_lovelace_ref = db.document(u'users/alovelace')
