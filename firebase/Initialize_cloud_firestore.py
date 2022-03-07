import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('../data/info/atte2gd-eb088-firebase-adminsdk-bftoy-36320b017e.json')
cred = credentials.Certificate('data/info/atte2gd-eb088-firebase-adminsdk-bftoy-36320b017e.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

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
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

get_docs = users_ref.get()
for doc in get_docs:
    if doc.exists:
        print(f'Document data: {doc.to_dict()}')
    else:
        print(u'No such document!')

# get document
a_lovelace_ref = db.collection(u'users').document(u'alovelace')
# get collection
users_ref = db.collection(u'users')
# get document with /
a_lovelace_ref = db.document(u'users/alovelace')
