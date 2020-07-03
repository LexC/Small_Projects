"""
This script copy the liked Windows Spotlight Wallpapers and save it to a target folder.
Obs: The Windows delete this image files from time to from, so to get more wallpapers is indicated to run this script at least once per week.
"""
#%% Libery

import os
from os.path import isfile, join
import shutil
from PIL import Image

#%% Variables and Loads
source='C:\\Users\\alexc\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'
destin='C:\\Users\\alexc\\OneDrive\\Imagens\\Windows_Wallpapers'

del_vertical_images=True

#%%Main

# Create Wallpapers Folder
try:
    os.mkdir(destin)
except FileExistsError:
    pass


# Coping files
files = [f for f in os.listdir(source) if isfile(join(source, f))]

for f in files:

    outputimage=join(destin,f+'.jpg')
    shutil.copyfile(join(source,f),outputimage)

# delete vertical images
    if del_vertical_images:
        flag=0
        with Image.open(outputimage) as img:
            if img.size[0]<img.size[1]:
                flag = 1
        if flag==1:
            os.remove(outputimage)
        

