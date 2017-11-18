import json
import codecs
from  AnalysicFirebase import  __requests__,__results__
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from pprint import pprint
# import  datetime
# tick = datetime.datetime.now()
# str = tick.strftime("%Y-%m-%d %H:%M:%S")
# #print(str)
t='2017-11-18 16:18:09'
rs=__results__('2017-11-18 16:18:09')
print(rs)

app = ClarifaiApp(api_key="d23a9b2861af443ba96d80763d365ad9")
model = app.models.get('AIBoy')
response = model.predict_by_url(rs)
predict_name= response['outputs'][0]['data']['concepts'][0]["id"]
pri_percent = response['outputs'][0]['data']['concepts'][0]["value"]
re = __requests__('2017-11-18 16:18:09',predict_name,pri_percent)