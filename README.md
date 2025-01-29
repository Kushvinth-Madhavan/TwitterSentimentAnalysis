# Twitter Sentiment Analysis Tool

A Python-based tool that performs sentiment analysis on tweets containing specific keywords using Twitter API and TextBlob.

## Features

- Fetches tweets based on specified keywords
- Performs sentiment analysis on retrieved tweets
- Exports results to CSV format
- Simple and easy-to-use interface

## Project Structure

```
twitter-sentiment-analysis/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── LICENCE
├── src/
│   ├── __init__.py
│   ├── config.py
│   └── sentiment_analyzer.py
└── data/
    └── .gitkeep
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kushvinth-madhavan/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example` and add your Twitter API credentials.

## Configuration

1. Create a Twitter Developer account and obtain API credentials from [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Copy `.env.example` to `.env` and fill in your credentials:
```
API_KEY=your_api_key
API_KEY_SECRET=your_api_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret
```

## Usage

1. Run the sentiment analyzer:
```bash
python src/sentiment_analyzer.py
```

2. Check the generated CSV file in the `data` directory for results.

## Requirements

See `requirements.txt` for a full list of dependencies. Main requirements include:
- Python 3.8+
- tweepy
- textblob
- python-dotenv

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
