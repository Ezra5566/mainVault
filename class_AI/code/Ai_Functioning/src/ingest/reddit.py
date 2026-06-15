"""Reddit data ingestion."""

import os
import praw
import pandas as pd
from src import config

# Initialize PRAW reddit instance
reddit = praw.Reddit(
    client_id=config.config["social"]["reddit"]["client_id"],
    client_secret=config.config["social"]["reddit"]["client_secret"],
    user_agent=config.config["social"]["reddit"]["user_agent"],
)

def fetch_posts(subreddit_name: str, limit: int = 100) -> pd.DataFrame:
    """
    Fetch top posts from a subreddit.

    Args:
        subreddit_name: Name of the subreddit (e.g., 'technology').
        limit: Maximum number of posts to retrieve.

    Returns:
        DataFrame with post title, selftext, score, id, created_utc, etc.
    """
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.top(limit=limit):
        posts.append({
            "title": post.title,
            "selftext": post.selftext,
            "score": post.score,
            "id": post.id,
            "created_utc": post.created_utc,
            "num_comments": post.num_comments,
            "over_18": post.over_18,
        })
    df = pd.DataFrame(posts)
    return df

if __name__ == "__main__":
    # Simple demo: fetch top posts from r/python
    df = fetch_posts("python", limit=50)
    df.to_csv("data/raw/reddit_python.csv", index=False)
    print(f"Fetched {len(df)} posts.")