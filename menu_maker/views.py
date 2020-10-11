from django.shortcuts import render
from .picgen import PicGen
from django.http import HttpResponseRedirect
from .picmerge import PicMerge
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def HomePageView(request):
    mod = 1
    if request.method == 'POST':
        fs = FileSystemStorage()
        mod = request.POST.get("mod")
        if mod == None:
            mod = 1
        try:
            if request.FILES['img1'] and request.FILES['img1'].content_type[0:5]=="image":
                img1 = request.FILES['img1']
                fs.delete("img1.jpeg")
                fs.save("img1.jpeg", img1)
            if request.FILES['img2'] and request.FILES['img2'].content_type[0:5] == "image":
                img2 = request.FILES['img2']
                fs.delete("img2.jpeg")
                fs.save("img2.jpeg", img2)
            if request.FILES['img3'] and request.FILES['img3'].content_type[0:5] == "image":
                img3 = request.FILES['img3']
                fs.delete("img3.jpeg")
                fs.save("img3.jpeg", img3)
        except MultiValueDictKeyError:
            pass
    generator = PicGen()
    generator.generate_pic()
    loc1 = os.path.join(BASE_DIR, 'media/img1.jpeg')
    loc2 = os.path.join(BASE_DIR, 'media/img2.jpeg')
    loc3 = os.path.join(BASE_DIR, 'media/img3.jpeg')
    merger = PicMerge(loc1, loc2, loc3, mod)
    merger.merge_pic()
    return render(request, 
            'base.html', {"value" : mod}
            )




