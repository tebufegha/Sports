from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlalchemy

url = 'https://www.soccerstats.com/team.asp?league=spain&teamid=8'
x = requests.get(url)
soup = BeautifulSoup(x.text, "html.parser")
table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('width') and tag['width']=="98%") 
rows = table.findAll(lambda tag: tag.name=='tr')
print(rows)
#print(soup.prettify())
print("Search Complete.")
