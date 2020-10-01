from .picgen import PicGen
from .picmerge import PicMerge
from tkinter import Tk
from tkinter.filedialog import *
def MakeMenu():
    Tk().withdraw()
    img1 = askopenfilename(title='Choose first image:')
    img2 = askopenfilename(title='Choose second image:')
    outfile = asksaveasfilename(title='Save menu as:')
    picmerge = PicMerge(outfile, img1, img2)
    picmerge.merge_pic()

