import requests
import base64
import urllib.request
import urllib.error
import urllib.parse
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *


print('Dizinin bölüm linkini kopyala ve entere bas')
site = input()
r = requests.get(site)
dosya = r.text
baslangic = dosya.find('subtitle :')
bitis = dosya.find('vpaidMode :')

if bitis is None:
    bitis = dosya.find('skipTime :')



a = baslangic+12
b = bitis-105
dekod = ""

for i in range(a, b+1):
    dekod += dosya[i]


data = base64.b64decode(dekod)
sonuc = data.decode("ascii")
uzanti = '.vtt'

q = requests.get(sonuc)
altyazi = q.text

response = urllib.request.urlopen(sonuc)
webcontent = response.read()
print('Dosya adı giriniz')
dosyaAd = input()
dosyaAdi = dosyaAd + uzanti

f = open(dosyaAdi,'wb')
f.write(webcontent)
f.close()







