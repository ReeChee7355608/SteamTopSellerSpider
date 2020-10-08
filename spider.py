# -*- coding: UTF-8 -*-
from lxml import etree
import xml.etree.ElementTree as ElementTree
import os
import re
if os.path.exists("wget.exe"):
    os.system("wget.exe -q http://store.steampowered.com/feeds/weeklytopsellers.xml")
    f=open("weeklytopsellers.xml","rb")
    html=f.readlines()
    f.close()
    os.system("del /f /q weeklytopsellers.xml")
    os.system("del /f /q .wget-hsts")
    conf = re.compile("\<\!\[CDATA\[(.*?)\]\]\>")
    m = conf.findall(str(html))
    print (" "+str(m[0].encode("raw_unicode_escape").decode("utf-8")),"\n",str(m[2].encode().decode('unicode_escape')),"\n",str(m[4].encode().decode('unicode_escape')),"\n",str(m[6].encode().decode('unicode_escape')),"\n",str(m[8].encode().decode('unicode_escape')),"\n",str(m[10].encode().decode('unicode_escape')),"\n",str(m[12].encode().decode('unicode_escape')),"\n",str(m[14].encode().decode('unicode_escape')),"\n",str(m[16].encode().decode('unicode_escape')),"\n",str(m[18].encode().decode('unicode_escape')))
    os.system("pause")
else:
    print("404 ERROR CODE 请检查该目录是否有wget.exe !")
    os.system("pause")