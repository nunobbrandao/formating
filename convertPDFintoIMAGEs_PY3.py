# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pdf2image import convert_from_path
import glob
import os

#list of files to be imported
files = glob.glob(os.path.join(os.getcwd(),'*.pdf')) 

for file in files:
    file_name = file.split("\\")[-2] + "_" + file.split("\\")[-1].split(".")[0]
    pages = convert_from_path(file, 500)
    for i,page in enumerate(pages):
        page.save(os.path.join(os.getcwd(), file_name + "_{}.jpg".format(i)), 'JPEG')
print("Code Run")