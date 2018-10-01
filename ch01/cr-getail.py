from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

proc_files = {}

def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel ='stylesheet']")
    links += soup.select("a[herf]")
    result = []

    for a in links:
        href = a.attrs['href']
        url - urljoin(base, href)
        result.append(url)
        return result

    def download_file(url):
        o = urlparse(url)
        savepath = "./" + o.netloc + o.path
        if re.search(r"/$", savepaht):
            savepath += "index.html"
            savedir = os.path.dirnave(savepath)
            if os.path.exists(savepath): return savepath

            if not os.path.exists(savedir):
                print("mkdir=", savedir)
                makedirs(savedir)

                try:
                    print("download=", url)
                    urlretrieve(url, savepath)
                    time.sleep(1)
                    return savepath
                except:
                    print("다운 실패:", url)
                    return None

                def analyze_html(url, root_url):
                    savepath = download_file(url)

                if savepath is None : return 
                if savepath in proc_files: return 
                proc_files[savepath] = True
                print("analyze_html", url)

                html = opne(savepath, "r", endcoding="utf-8").read()
                links = enum_links(html, url)

                for link_url in links:
                    if link_url.find(root_url) != 0:
                        if not re.search(r".css$", linkurl): continue

                        if re.search(r".(html|htm)$", link_url):
                            analyze_html(link_url, root_url)
                            continue
                        download_file(link_url)

                        if _name_ == "_main_"
                        url = "httPs://docs.python.org/3.5/library/"
                        analyze_html(url, url)
