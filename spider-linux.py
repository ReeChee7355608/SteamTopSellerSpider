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
try:
    os.system("wget -q http://store.steampowered.com/feeds/weeklytopsellers.xml")
except:
    print("404-l ERROR CODE 没有找到wget !")
date()
os.system("rm -f ./weeklytopsellers.xml")
os.system("rm -f ./.wget-hsts")
######################################
#      Steam Top Seller Spider       #
#               1.1                  #
# 完成于2020.10.13 22:07 (GMT+8, BJT) #
#          By      ReeChee           #
######################################