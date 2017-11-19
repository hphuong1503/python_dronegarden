import json
import codecs
from  AnalysicFirebase import  __requests__,__results__
from clarifai.rest import ClarifaiApp
from clarifai import  rest
from clarifai.rest import Image as ClImage
from pprint import pprint
import firebase_admin
from firebase_admin import credentials

from firebase_admin import db
# Fetch the service account key JSON file contents
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate('flycam-184516-firebase-adminsdk-fps0w-307954056b.json')
# default_app = firebase_admin.initialize_app(cred)
#
# print(default_app.name)

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flycam-184516.firebaseio.com/'
})

ref = db.reference('Image')
result = ref.order_by_key().limit_to_last(1).get()
dateTimeKey = list(result.keys())[0]
imageLink = result[dateTimeKey]['link']
print(imageLink)
app = ClarifaiApp(api_key='d23a9b2861af443ba96d80763d365ad9')
model = app.models.get('AIBoy')
model.get_version('d1f91e14ce6145bfb01ce2e9461e0192')
response = model.predict_by_url(imageLink)
predict_name= response['outputs'][0]['data']['concepts'][0]["id"]
pri_percent = response['outputs'][0]['data']['concepts'][0]["value"]
print(predict_name,"--",pri_percent)
refPredict = db.reference()
request = refPredict.child("Predict").set({
    'dudoan':predict_name,
    'xs':pri_percent
})

