import requests
import bs4
def weatherData(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    bars = soup.select('.myforecast-current-sm')

    print(bars[0].text)

