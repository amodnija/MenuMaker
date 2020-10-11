from PIL import Image
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class PicMerge:
    def __init__(self, img1loc, img2loc, img3loc, mod):
        self.menu_df = Image.open(os.path.join(
            BASE_DIR, 'online_menu_maker/static/menu.png'))
        self.header = Image.open(os.path.join(
            BASE_DIR, 'online_menu_maker/static/ff-header.jpg'))
        self.disp_image1 = Image.open(img1loc) 
        self.disp_image2 = Image.open(img2loc)
        self.disp_image3 = Image.open(img3loc)
        self.border = Image.open(os.path.join(
            BASE_DIR, 'online_menu_maker/static/border.jpg'))
        self.menu_size = self.menu_df.size
        self.header_ratio = self.header.size[1]/self.header.size[0]
        self.loc = os.path.join(
            BASE_DIR, 'online_menu_maker/static/menu.jpg')
        self.mod = float(mod)

    def _prep_images(self):
        self.header = self.header.resize((self.menu_size[0],\
           int(self.menu_size[0]*self.header_ratio)))
        self.disp_image1 = self.disp_image1.resize((self.menu_size[0]//3,\
             int(self.mod*self.menu_size[1]//3)))
        self.disp_image2 = self.disp_image2.resize((self.menu_size[0]//3,\
             int(self.mod*self.menu_size[1]//3)))        
        self.disp_image3 = self.disp_image3.resize((self.menu_size[0]//3,\
             int(self.mod*self.menu_size[1]//3)))
        self.bg_image_size = (self.menu_size[0],(self.menu_size[1]\
             + self.header.size[1] + self.disp_image1.size[1]))
        self.bg_image = Image.new("RGB", (self.bg_image_size))
        self.border = self.border.resize((self.bg_image_size[0]+4,\
             self.bg_image_size[1]+4))

    def _paste_images(self):
        self.bg_image.paste(self.header, (0,0))
        self.bg_image.paste(self.disp_image1, (0,self.header.size[1]))
        self.bg_image.paste(self.disp_image2,\
             (self.disp_image1.size[0],self.header.size[1]))
        self.bg_image.paste(self.disp_image3,
            (2*self.disp_image1.size[0], self.header.size[1]))
        self.bg_image.paste(self.menu_df,\
             (0,(self.header.size[1] + self.disp_image1.size[1])))
        self.border.paste(self.bg_image, (2,2))

    def _save_image(self, name, form):
        self.border.save(name, form)

    def merge_pic(self):
        self._prep_images()
        self._paste_images()
        self._save_image(self.loc, "JPEG")




