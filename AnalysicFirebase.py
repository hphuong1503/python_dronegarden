from  firebase import  firebase
firebase = firebase.FirebaseApplication('https://flycam-184516.firebaseio.com/', None)
def __results__(filename):
    temp='Image/'+filename+'/link'
    #'Image/2017-11-18 16:18:09/link'
    result = firebase.get(temp ,None)
    return result
def __requests__(name,pri_name,value):
    request = firebase.post('Predict/'+name,{'Rau':{pri_name:value}})
    return value;

def __deleteData(pri_name,value):
    remove = firebase.delete(pri_name,value)
    return  remove;
