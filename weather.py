import requests

url = "http://api.weatherapi.com/v1/current.json"
access_key = "f48e53d3f4664357930164434220207"
sehir = input("Hava durumunu öğrenmek istediğiniz şehri giriniz: ")

response = requests.get(url, params= {
        "key": access_key,
        "q": sehir
})

sonuc = response.json()
havadurumu = sonuc["current"]["temp_c"]

print(f"{sehir} şehrinin şu anki hava sıcaklığı {havadurumu} derecedir.")

