import openai
from decouple import config
from scraper import Scraper
from sms import SMS


class Bot():
    def __init__(self):
        openai.api_key = config('OPENAI_API_KEY')
        self.model = 'text-davinci-003'
        self.max_tokens = 500
        self.preface = '''Please provive a list of stocks appear most bullish and bearish for day trading based off the following news. Please provide data in the following format:
                        🚀 BUY: ... 
                        
                        📉 SELL: ...
                       '''
        self.scaper = Scraper()
        self.sms = SMS()

    def analyze(self):
        news = self.scaper.scrape_news()
        prompt = f'{self.preface}: {news}'
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            max_tokens=self.max_tokens,
        )
        self.sms.send(body=response['choices'][0].text)