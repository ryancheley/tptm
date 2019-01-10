import requests
import time
from bs4 import BeautifulSoup


url = 'https://training.talkpython.fm/courses/explore_ansible/introduction-to-ansible-with-python'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


course_title = soup.find('h1').text
course_chapter_elements = soup.find_all('tr', {"class":"chapter"})


print('{} @autodone(true) '.format(course_title))

for rows in course_chapter_elements:
	course_item = rows.find('td', {"class":"chapter-title-column"}).text.strip()
	if len(rows.find('td', {"class":"time-column"}).text.strip()) <= 5:
		course_item_duration_min = time.strptime(rows.find('td', {"class":"time-column"}).text.strip(), '%M:%S').tm_min
		duration = str((round(course_item_duration_min / 15)+1)*15)
	else:
		course_item_duration_min = time.strptime('0'+rows.find('td', {"class":"time-column"}).text.strip(), '%H:%M:%S').tm_min
		course_item_duration_hour = time.strptime('0'+rows.find('td', {"class":"time-column"}).text.strip(), '%H:%M:%S').tm_hour
		duration = str((round(course_item_duration_min / 15)+1)*15 + course_item_duration_hour * 60)

	item = ' - {} @estimate({}m) @context(Technology) @parallel(true)'.format(course_item, duration)
	print(item)