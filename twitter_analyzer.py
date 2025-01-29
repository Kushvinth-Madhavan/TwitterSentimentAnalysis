# twitter_analyzer.py
import tweepy
from textblob import TextBlob
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TwitterAnalyzer:
    def __init__(self):
        # Twitter API Credentials
        self.auth = tweepy.OAuthHandler(
            os.getenv("API_KEY"), 
            os.getenv("API_KEY_SECRET")
        )
        self.auth.set_access_token(
            os.getenv("ACCESS_TOKEN"), 
            os.getenv("ACCESS_TOKEN_SECRET")
        )
        self.api = tweepy.API(self.auth)

    def analyze_tweets(self, keyword="Trump", count=100):
        try:
            # Fetch tweets
            tweets = self.api.search_tweets(q=keyword, count=count, tweet_mode="extended")
            
            # Analyze each tweet
            results = []
            for tweet in tweets:
                # Analyze sentiment
                analysis = TextBlob(tweet.full_text)
                
                results.append({
                    'tweet': tweet.full_text,
                    'polarity': analysis.sentiment.polarity,
                    'subjectivity': analysis.sentiment.subjectivity,
                    'created_at': tweet.created_at
                })
            
            # Convert to DataFrame
            df = pd.DataFrame(results)
            
            # Save results
            os.makedirs('data', exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"data/tweets_{timestamp}.csv"
            df.to_csv(filename, index=False)
            print(f"Results saved to {filename}")
            
            return df
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

if __name__ == "__main__":
    analyzer = TwitterAnalyzer()
    analyzer.analyze_tweets()
