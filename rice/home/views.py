from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


model=load_model('./models/model.h5')

# Create your views here.

def index(request):
    context={'a':1}
    return render(request,'index.html',context)

def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileobj=request.FILES['filePath']
    fs=FileSystemStorage()

    filepathname=fs.save(fileobj.name,fileobj)
    filepathname=fs.url(filepathname)
    print(filepathname)
    s="E:/django rice/rice"
    img = image.load_img(s+filepathname, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255


    # check prediction
    img_class = model.predict(img_tensor)
    a=np.argmax(img_class,axis=1)
    var=a[0]
    if(var==0):
        print("Bacterial leaf blight")
    elif(var==1):
        print("Brown spot")
    else:
        print("Leaf smut")

    context={'filepathname':filepathname}
    
    return render(request,'index.html',context)    




