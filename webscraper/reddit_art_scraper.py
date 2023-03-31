# new scraper based on reddit.com/r/museum to get random art
# You have to put in your own credentials for Reddit!
import praw
import time

# Create a Reddit instance with your own credentials
reddit = praw.Reddit(
    client_id="IqmOrwTHCpxXyofkjhNm7w",
    client_secret="mjtY2SVYbovxqlopx2OQTfHOdbHXCg",
    username="LeBrokkole",
    password="963Y8tybLqdT8v",
    user_agent="LeBrokkole's /r/museum script",
)


def get_top_all_time(subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    top_all_time = []
    images = []

    # Fetch posts in chunks of 100
    count = 0
    while len(top_all_time) < limit:
        chunk = list(subreddit.top("all", limit=100, params={"count": count}))
        if not chunk:
            break
        top_all_time.extend(chunk)
        count += len(chunk)
        time.sleep(1)  # Add a delay to avoid hitting the rate limit

    # Truncate the list to the desired length and print the results
    top_all_time = top_all_time[:limit]
    for idx, post in enumerate(top_all_time, start=1):
        # print the direct link to the image connected to the post, as well as the link to the post/the comments
        # make sure the link is clickable (not cut off)
        images.append(f'{post.url} {post.shortlink}')

    return images

if __name__ == "__main__":
    # write the top imaes into ..global/data/art.tx
    with open("../global/data/art.txt", "w") as f:
        img = get_top_all_time("museum", 2000)
        for i in img:
            f.write(i + "\n")