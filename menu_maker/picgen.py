import pandas as pd
import sqlite3
import dataframe_image as dfi
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class PicGen:

    def __init__(self):
        self.raw_file = os.path.join(BASE_DIR, 'db.sqlite3')
        self.conn = sqlite3.connect(self.raw_file)
        self.raw_df = pd.read_sql_query("select * from menu_maker_item;",self.conn)
        self.convert_dict = {"Rate" : "str",
                             "Count Per Kg" : "str"}
        self.style_list = [{'selector':'table .dataframe',
                            'props':[('table-layout','fixed'),
                                     ('width', '150%'),]},
                           {'selector':'th',
                            'props':[('text-align', 'left'),
                                     ('background', 'white'),
                                     ('border-top', '1px solid black'),
                                     ('color', '297c60'),
                                     ('font-family', 'Noto sans, sans-serif'),
                                     ('font-weight', '600'),
                                     ('font-size', '16px')]},
                           {'selector':'td',
                            'props':[('text-align', 'center'),
                                     ('background', 'white'),
                                     ('color', '297c60'),
                                     ('font-family','Noto sans, sans-serif'),
                                     ('font-size', '16px')]},
                           {'selector':'tr:last-of-type',
                            'props':[('border-bottom','1px solid black')]}]
        self.valid_columns = ["product", "cut_details", "count", "rate"]
        self.source = os.path.join(BASE_DIR, "menu_maker/templates/menu_maker/menu.png")

    def _refine_db(self):
        self.raw_df.columns = [label.lower().strip() for label in self.raw_df.columns]
        self.raw_df.fillna("", inplace=True)        
        self.filt_df = self.raw_df.copy()
        for label, content in self.raw_df.iterrows():
            if self.raw_df.loc[label]['availability'].lower() == "no":
                self.filt_df.drop(label, inplace=True) 
        self.drop_list = [column for column in self.filt_df.columns if column not in self.valid_columns]
        self.filt_df.drop(columns=self.drop_list, inplace=True)
        self.filt_df.columns = [label.title() for label in self.filt_df.columns]
        self.filt_df.reset_index(inplace=True, drop=True)                
        self.filt_df.columns = ["Product", "Cut Details", "Count Per Kg", "Rate"]
        self.filt_df = self.filt_df.astype(self.convert_dict, errors='ignore')

    def _style_df(self):
        for n in range(1,self.filt_df.size):
            if n%5 == 1:
                self.style_list.append({'selector': f'td:nth-of-type({n})',
                                        'props': [('text-align', 'left'),
                                                  ('background', 'white'),
                                                  ('color', '297c60'),
                                                  ('font-family','Noto sans, sans-serif'),
                                                  ('font-size', '16px')]})
        self.filt_df = self.filt_df.style.set_table_styles(self.style_list).hide_index()

    def _save_df_image(self):
        dfi.export(self.filt_df, self.source)

    def generate_pic(self):
        self._refine_db()
        self._style_df()
        self._save_df_image()


