# -*- coding: UTF-8 -*-
from lxml import etree
import xml.etree.ElementTree as ElementTree
import os
def date():
    got=etree.parse("weeklytopsellers.xml")
    root=got.getroot()
    for temp in root:
        print(temp[0].text)
    print("更新时间:",root[0][4].text)
if os.path.exists("wget.exe"):
    # GET
    os.system("wget.exe -q http://store.steampowered.com/feeds/weeklytopsellers.xml")
    date()
    os.system("del /f /q weeklytopsellers.xml")
    os.system("del /f /q .wget-hsts")
    os.system("pause")
else:
    print("404 ERROR CODE 请检查该目录是否有wget.exe !")
    os.system("pause")
######################################
#      Steam Top Seller Spider       #
#               1.1                  #
# 完成于2020.10.13 22:07 (GMT+8, BJT) #
#          By      ReeChee           #
######################################