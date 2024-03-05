"""
Locates the subscribers of a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API for the number of subscribers of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit, or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching subreddit information: {e}")
        return 0
