import requests
import base64
import urllib.request
import urllib.parse

while True:
    print('Dizinin bölüm linkini kopyala ve entere bas ya da çıkmak için q ya bas')
    site = input()
    if site == "q":
        break
    elif site == "Q":
        break
    else:
        r = requests.get(site)
        dosya = r.text
        baslangic = dosya.find('vpaidMode :')
        bitis = dosya.find('skipTime :')

        a = baslangic+59
        b = bitis-69
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

        f = open(dosyaAdi, 'wb')
        f.write(webcontent)
        f.close()
