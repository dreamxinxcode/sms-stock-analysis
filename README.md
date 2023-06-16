# Stock Trading News Bot

This Python application uses OpenAI's GPT-3.5 language model to analyze stock trading news and send the analysis via SMS to a list of recipients.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.x installed
- Required Python packages installed (install using `pip install -r requirements.txt`)
- OpenAI API key
- Twilio account credentials (SID, auth token, and phone number)
- Properly configured `.env` file with the necessary environment variables

## Getting Started

1. Clone the repository:

```shell
git clone https://github.com/your-username/stock-trading-news-bot.git
cd stock-trading-news-bot
```

2. Install the required dependencies:

```shell
pip install -r requirements.txt
```

3. Configure the environment variables:

Create a .env file in the project root directory and add the following variables:

```shell
OPENAI_API_KEY=your_openai_api_key
TWILIO_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_NUMBER=your_twilio_phone_number
RECIPIENTS=recipient1_phone_number,recipient2_phone_number,recipient3_phone_number
```

4. Run the application:

```shell
python main.py
```

Code Structure

The application consists of the following main files:

    bot.py: Contains the Bot class responsible for analyzing stock trading news using OpenAI and sending the analysis via SMS.
    scraper.py: Contains the Scraper class responsible for scraping stock trading news from a website.
    sms.py: Contains the SMS class responsible for sending SMS messages using the Twilio API.

## Customize

Feel free to customize the application as per your requirements. You can modify the prompt, the OpenAI model, the scraping source, and more by editing the respective variables in the Bot class.

For further customization, refer to the documentation of the used libraries:

    OpenAI Python
    Twilio Python
    python-decouple
    Beautiful Soup
    cloudscraper

License

This project is licensed under the MIT License.