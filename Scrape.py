from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.fifa.com/worldcup/matches/index.html').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('FIFA.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Round', 'Date'])

match = soup.title.text
print(match)

print() #printing new line

for article in soup.find_all('div', class_='match-list-round anchor'):
	game = article.h2.text
	print(game)

	print ()

	date = article.h3.text
	print(date)

	print()

	csv_writer.writerow([game, date])

csv_file.close()

	# for details in soup.find_all('div', class_='mu-m'):
	# 	for team1 in soup.find_all('div', class_='t home'):
	# 		team = team1.span.text
	# 		print(team)

	# 		print()
		#for team2 in soup.find_all('div', class_='')





# # article = soup.find('div', class_='navbar navbar-pageheader navbar-matchlistheader nav-scrollspy')
# article = soup.find('div', class_='inner')
# # print(article)

# heading = article.h1.text
# print(heading)