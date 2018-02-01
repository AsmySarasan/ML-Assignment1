from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.fifa.com/worldcup/matches/index.html').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('FIFA.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ROUND', 'DATE'])

match = soup.title.text
print(match)

print() #printing new line

for article in soup.find_all('div', class_='match-list-round anchor'):
	game = article.h2.text

	for article in soup.find_all('div', class_='match-list-date anchor'):
		date = article.h3.text
	
		csv_writer.writerow([game, date])

csv_file.close()

#Display game details in the terminal

data = soup.find_all("div", {"class": "matches"})

for item in data:

	#First stage
	try:
		data = item.contents[0].text
		print(data)
		print()
	except:
		pass

	# #round of 16
	# try:
	# 	print(item.contents[1].text)
	# 	print()
	# except:
	# 	pass

	# #quarter finals
	# try:
	# 	print(item.contents[2].text)
	# 	print()
	# except:
	# 	pass

	# #semi finals
	# try:
	# 	print(item.contents[3].text)
	# 	print()
	# except:
	# 	pass

	# #third place
	# try:
	# 	print(item.contents[4].text)
	# 	print()
	# except:
	# 	pass

	# #finals
	# try:
	# 	print(item.contents[5].text)
	# 	print()
	# except:
	# 	pass
