from django.shortcuts import render
from .picgen import PicGen

def MenuDispView(request):
    generator = PicGen()
    generator.generate_pic()
    return render(request, 
            'menu_maker/menu_disp.html',
            )


