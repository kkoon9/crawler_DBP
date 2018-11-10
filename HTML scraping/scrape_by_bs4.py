from bs4 import BeautifulSoup

with open('DOTAX_url.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

buffer = soup.select('tbody')

for a in buffer:
    print(a.text)
