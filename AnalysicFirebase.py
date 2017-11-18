from  firebase import  firebase
firebase = firebase.FirebaseApplication('https://flycam-184516.firebaseio.com/', None)
def __results__(filename):
    temp='Image/'+filename+'/link'

    result = firebase.get(temp ,None)
    return result
def __requests__(time,name,value):
    request = firebase.post(time, {'Dudoan':name, 'xs': value})

def __deleteData(pri_name,value):
    remove = firebase.delete(pri_name,value)
    return  remove;
