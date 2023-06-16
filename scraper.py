from bs4 import BeautifulSoup as beauty
import cloudscraper


class Scraper():
    def __init__(self):
        self.scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 
        self.url = "https://finviz.com/news.ashx"
    
    def scrape_news(self):
        info = self.scraper.get(self.url).text
        soup = beauty(info, "html.parser")
        headlines = soup.find_all('a', class_='nn-tab-link')
        news = ''.join([tag.text for tag in headlines])
        return news