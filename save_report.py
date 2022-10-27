# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:37:21 2022

@author: cnco
"""

import pandas as pd
import base64
import webbrowser
import time

df=pd.read_csv('Reports_list.csv',sep=';',decimal=',')

url_download="https://market-research.enerdata.net/include_php/viewPDF.php?file="

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

for i in range(len(df)):
    code_pays=df["id"].loc[i]
    print(code_pays)
    code=base64.b64encode(code_pays.encode('ascii')).decode('ascii')#code_pays encode en base 64
    url=url_download+code
    print(url)
    webbrowser.get(chrome_path).open(url)
    time.sleep(5)
    