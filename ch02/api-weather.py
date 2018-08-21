import requests
import json

#api 키를 지정
apikey = "8e41d268323d4bc0bdcdd6695c896c78"

#날씨를 확인할 도시 선정
cities = ["Seoul,KR", "Tokyo,JP", "Nwe York,US"]

#api 지정
api = "http://api.weathermap.org/data/2.5/weather?q={city}&APPID={key}"

#켈빈 온도를 섭시온도로 변환하는 함수
k2c = lambda k : k - 273.15

#각 도시의 정보 추출하기
for name in cities:
    #api의 URL 구성하기
    url = api.format(city=name, key=apikey)

    #api에 요청을 보내 데이터 추출하기
    r = requests.get(url)

    #결과를 JSON 형식으로 변환하기
    data = json.loads(r.text)

    #결과 도출하기
    print("+도시 =", data["name"])
    print("|날씨 =", data["Weather"][0]["description"])
    print("|최저온도 =", k2c(data["main"]["temp_min"]))
    print("|최고온도 =", k2c(data["main"]["temp_max"]))
    print("|습도 =", data["main"]["humidity"])
    print("|기압 =", data["main"]["pressure"])
    print("|풍향 =", data["wind"]["deg"])
    print("|풍속 =", data["wind"]["speed"])
    print("")
