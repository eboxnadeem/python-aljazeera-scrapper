from time import sleep
import bs4 as bs
import urllib.request as ureq
import urllib.parse
from urllib import request, parse
base_name = "https://www.aljazeera.com/news/"
page_html = ureq.urlopen('https://www.aljazeera.com/news/').read()
ureq.urlopen('https://www.aljazeera.com/news/').close()
page_soup = bs.BeautifulSoup(page_html, "lxml")
containers = page_soup.find_all("div", {"class":"topics-sec-item"})
filename = "aljazeera.csv"
f = open(filename, "w")
header = "Title , Url , Author , Tags \n"
f.write(header)
while containers is not None:
 for container in containers:
  title = container.find_all("h2", {"class":"topics-sec-item-head"})
  title_name = title[0].text
  links = container.find_all("a", {"class": "centered-video-icon"})
  url = links[0]["href"]
  complete_url = urllib.parse.urljoin(base_name, url)
  detail_page = ureq.urlopen(complete_url).read()
  ureq.urlopen(complete_url).close()
  detail_page_soup = bs.BeautifulSoup(detail_page, "lxml")
  pages = detail_page_soup.find_all("h1", {"class":"post-title"})
  finaltitle = pages[0].text
  author = detail_page_soup.find_all("div", {"class": "article-heading-author-name"} , "a")
  finalauthor ="".join(author[0].text.splitlines())
  tags = detail_page_soup.find_all("div", {"class": "article-body-tags"})
  finaltags = "|".join(tags[0].text.splitlines())
  print(finaltitle.replace("," , "|") + "," + complete_url + "," +  finalauthor + "," + finaltags + "\r\n\n\n" )
  f.write(finaltitle.replace("," , "|") + "," + complete_url + "," +  finalauthor + "," + finaltags + "\r\n"  )
 containers = None
 print("Click Show More\r\n")  
 show_more_form_data = parse.urlencode({"oryxcontext":"B8C906090FB19032EA03A7D3B8D5B5D7A73C85F46223076926689D7EDCA1378CED8159162317DD25CCACA5FBF36BB063F8B4A35AD1D6C5D7A3315C8F9F1907F9DB8F41B5756831489C845863B88999500F0E80B569A9BA3E218D232613C93FB97155126F02D36BC878FD91C334CB4B2A56EABEB9F209A62160A9A9106FF8C2634B3767ECE2BA8779957D64DE83EE9C02CA9954AD18BB54BCFAEFC0E81B1099A1074C3339725C85587913630A309253C388C45593C67D804BA9E8FB7C14E80C5CE5FBEC58423377A7BB9D30B3694500D87DBA6F4494BACCB2D7FA62CE949DFEEB8D52273BEDDFE0E15B64A13B2B956C310FAD0FF987CFAA460C85FC1C3A602368FCDDDA2E5B067C5A2614BE2E30F14A3984CFA4E2D2937B2708DCF6CB6E9D881BA6A7617367C742DC47A91A12BCC41C6C"}).encode()
 show_more_post_url = "https://www.aljazeera.com/portal/handlers/HTMLParser.ashx?cmd=ajax&cmdtext=D2AEAD90362EBA2D588998BF152C2F79DD26DD0D31E21DA70A3CFEE7740AAE94D00F5DDC3D2ACA9000ECE8E27805D90958376CCB0BA2DAD4EB1E8C0843F0138C61A7EAC6B632D9A4BF445D038A1D6BA658B1DEBFCF576A8D7FA9A9E39D408E8774A37BDD80165EFC09A3F0613A44D96B8910951A05B078D96040129609E161D0&pageid=161023134902510"
 req =  request.Request(show_more_post_url, data=show_more_form_data) # this will make the method "POST"
 resp = request.urlopen(req)
 page_html=resp.read()
 page_soup = bs.BeautifulSoup(page_html, "lxml")
 containers = page_soup.find_all("div", {"class":"topics-sec-item"})
 print("container updated.\r\n") 

f.close()
