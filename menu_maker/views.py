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
    if request.method == 'POST':
        fs = FileSystemStorage()
        try:
            if request.FILES['img1']:
                img1 = request.FILES['img1']
                fs.delete("img1.jpeg")
                fs.save("img1.jpeg", img1)
            if request.FILES['img2']:
                img2 = request.FILES['img2']
                fs.delete("img2.jpeg")
                fs.save("img2.jpeg", img2)
            if request.FILES['img3']:
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
    merger = PicMerge(loc1, loc2, loc3)
    merger.merge_pic()
    return render(request, 
            'base.html',
            )




