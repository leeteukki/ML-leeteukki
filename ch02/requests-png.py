import requests
r = requests.get("http://www.kipris.or.kr/khome/images/common/logo01.png")

with open("test.png", "wb") as f :

    f.write(r.content)

    print("saved")
