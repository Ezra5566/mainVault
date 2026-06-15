"""Twitter data ingestion."""

import os
import tweepy
import pandas as pd
from src import config

# Initialize Tweepy client
client = tweepy.Client(
    bearer_token=config.config["social"]["twitter"]["bearer_token"],
    wait_on_rate_limit=True
)

def fetch_tweets(query: str, max_tweets: int = 100) -> pd.DataFrame:
    """
    Fetch recent tweets matching a query.

    Args:
        query: Search query string.
        max_tweets: Maximum number of tweets to retrieve.

    Returns:
        DataFrame with tweet text, author_id, created_at, etc.
    """
    # Twitter API v2 recent search endpoint
    response = client.search_recent_tweets(
        query=query,
        tweet_fields=["created_at", "author_id", "lang", "public_metrics"],
        max_results=100,  # Max per request
    )

    if not response.data:
        return pd.DataFrame()

    # Collect tweets until we reach max_tweets or exhaust results
    tweets = []
    for tweet in response.data:
        tweets.append({
            "text": tweet.text,
            "author_id": tweet.author_id,
            "created_at": tweet.created_at,
            "lang": tweet.lang,
            "retweet_count": tweet.public_metrics["retweet_count"],
            "reply_count": tweet.public_metrics["reply_count"],
            "like_count": tweet.public_metrics["like_count"],
            "quote_count": tweet.public_metrics["quote_count"]
        })
        if len(tweets) >= max_tweets:
            break

    df = pd.DataFrame(tweets)
    return df

if __name__ == "__main__":
    # Simple demo: fetch tweets about "climate change"
    df = fetch_tweets("climate change", max_tweets=50)
    df.to_csv("data/raw/twitter_climate.csv", index=False)
    print(f"Fetched {len(df)} tweets.")