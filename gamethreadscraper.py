# Instructions to get set up.
# Install PRAW: https://praw.readthedocs.io/en/v7.7.0/getting_started/quick_start.html
# Save this Python Script to your computer.
# Run this script with the command `python3 gamethreadscraper.py [token]`, where `[token]` is a token you want to search the thread for.
# Modify the script however you like to come up with interesting results.

# Imports
import praw, sys

# Setup a Reddit instance. This is a script application setup just for this Tech Challenge. You can create these at https://www.reddit.com/prefs/apps (and feel free to use your own).
reddit = praw.Reddit(
    client_id = "OQ1OsNYqBJ3vMBfJLn_DRQ",
    client_secret = "z5K8adUrqRKKKb7iUsP_4b-AZdKBzw",
    user_agent = "/r/CFB Tech Challenge",
)

# The Georgia - Ohio State Semifinal
submission = reddit.submission(id = '100cbyw')

# Expand some initially hidden comments. The limit means that at most 10 comment threads will be expanded. May take a minute.
submission.comments.replace_more(limit = 5)

# Flatten the comments from a tree into a list. Expanding and flattening will give us ~1500 comments to work with.
comments = submission.comments.list()

# Fetch the token you provided in the command line.
token = str(sys.argv[1])
 
# Iterate through the comments and do something on each one.
for comment in comments:
  try:
    # Get the author flair of the comment.
    comment_flair = comment.author_flair_text
    # Print the comment if it has flair that matches either team playing in the Semifinal.
    if (":georgia:" in comment_flair and token in comment.body.lower()): print("Georgia: " + comment.body)
    if (":ohiostate:" in comment_flair and token in comment.body.lower()): print("Ohio State: " + comment.body)
  except: pass
