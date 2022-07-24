from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

url = 'https://fifaonline4-nexon-com.translate.goog/datacenter/dailysquad?_x_tr_sl=auto&_x_tr_tl=vi&_x_tr_hl=vi&_x_tr_pto=op,wapp'
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<main[^>].*>([\s\S]*)</main.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
maincontent = match_results.group()
soup = BeautifulSoup(maincontent, "html.parser")
mua = soup.select('div[class="class_pl__cont content_wrap"]')
print(mua)