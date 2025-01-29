# Twitter Sentiment Analysis Tool

A robust Python application that performs sentiment analysis on tweets using Twitter API and TextBlob. This tool fetches tweets based on keywords and analyzes their sentiment, providing insights into public opinion on specific topics.

## Features

- Fetch tweets based on keyword search
- Perform sentiment analysis using TextBlob
- Export results to CSV with timestamp
- Configurable tweet count and search parameters
- Built-in logging and error handling
- Clean tweet text processing

## Prerequisites

- Python 3.8 or higher
- Twitter Developer Account with API credentials
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Kushvinth-Madhavan/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your Twitter API credentials
```

## Usage

1. Basic usage:
```python
from src.sentiment_analyzer import TwitterSentimentAnalyzer

analyzer = TwitterSentimentAnalyzer()
results = analyzer.analyze_tweets(keyword="Python", count=100)
analyzer.save_results(results)
```

2. Run from command line:
```bash
python -m src.sentiment_analyzer
```

## Configuration

Edit the `.env` file to configure:
- Twitter API credentials
- Tweet search count
- Target keywords
- Output directory
- Debug mode
- Log level

## Output

The tool generates a CSV file with:
- Tweet text
- Sentiment polarity (-1 to 1)
- Sentiment subjectivity (0 to 1)
- Tweet creation timestamp

## Project Structure

```
twitter-sentiment-analysis/
├── src/                  # Source code
│   ├── __init__.py
│   ├── config.py        # Configuration management
│   ├── utils.py         # Utility functions
│   └── sentiment_analyzer.py  # Main analyzer
├── data/                 # Output directory
├── .env.example         # Environment template
├── requirements.txt     # Dependencies
└── setup.py            # Package setup
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author

**Kushvinth Madhavan**
- GitHub: [Kushvinth-Madhavan](https://github.com/Kushvinth-Madhavan)

## License

MIT License

Copyright (c) 2024 Kushvinth Madhavan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
