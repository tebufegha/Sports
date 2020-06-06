from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlalchemy

count =1
searchval = input("Enter the country of the league you which to search: ").lower()

if searchval == "holland":
	searchval = "netherlands"

while count < 20:
	try:
		url = 'https://www.soccerstats.com/team.asp?league={0}&teamid={1}'.format(searchval,count)
		x = requests.get(url)
		soup = BeautifulSoup(x.text, "html.parser")
		table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('width') and tag['width']=="98%") 
		stats = [b.string for b in table.findAll('b')]
		df = pd.DataFrame({'Team Name':stats[0], 'Points Per Game': stats[1], 'Win Percentage': stats[2], 'Loss Percentage': stats[3], 'Goals Scored Per Game': stats[4], 'Goals Conceded Per Game': stats[5]}, index = [count])
		print(df)
		count += 1
	except AttributeError:
		print("Search Complete!")
		break

