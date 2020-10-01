from django.shortcuts import render
from .picgen import PicGen
from django.http import HttpResponse
from .picmerge import PicMerge
from .ffmenu import MakeMenu
def MenuDispView(request):
    generator = PicGen()
    generator.generate_pic()
    return render(request, 
            'menu_maker/menu_disp.html',
            )

def MenuSaveView(request):
    MakeMenu()
    return HttpResponse("<h1>Menu Saved</h1>")


