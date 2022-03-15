from bs4 import BeautifulSoup
import requests

URL = 'https://www.parliament.bg/bg/parliamentarygroups/2930'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

script = soup.find_all('script')

print(script)
