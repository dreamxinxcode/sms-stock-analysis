import openai
from decouple import config
from scraper import Scraper
from sms import SMS


class Bot():
    def __init__(self):
        openai.api_key = config('OPENAI_API_KEY')
        self.model = 'text-davinci-003'
        self.max_tokens = 500
        self.preface = '''Please provide a list of the most bullish and bearish stock tickers for day trading based off the following news in the following example format:
                        🚀 BUY: [ticker1], [ticker2]...
                        \n\n
                        📉 SELL: [ticker1], [ticker2]...
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