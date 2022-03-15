# Program to simulate scraping news from website
import requests 
from bs4 import BeautifulSoup 
#URL to parse html.Change it depending on the source
URL="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN:en"
r = requests.get(URL) 
no_of_headlines=int(input("\nEnter number of headlines:"))
soup = BeautifulSoup(r.content, 'html5lib')
#class is the tag for the headlines. Chnage it according to the tag in console.
section = soup.find_all('a', class_='DY5T1d')
print("Your News Starts from Here : ")
#Loop For Printing them
for elem in section:
	text=elem.get_text()
	print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
	print(text)
	no_of_headlines-=1
	if no_of_headlines==0:
		break
