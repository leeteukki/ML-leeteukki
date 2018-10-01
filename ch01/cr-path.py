from urllib.parse import urljoin


base = "htttp://example.com/html/a.html"

print(urljion(base, "b.html"))
print(urljoin(base, "sub/c.html"))
print(urljoin(base, "../index.html"))
print(urljoin(base, "../img/hoge.png"))
print(urljoin(base, "../css/hoge.css"))
