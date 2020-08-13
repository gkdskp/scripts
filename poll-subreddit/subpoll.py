import os
import time
import webbrowser
from datetime import datetime
import praw
from notify import notification

config = {
    'CLIENT_ID': '',
    'CLIENT_SECRET': '',
    'USER_AGENT': '',

    'LOG_FILE': '',
    'POLL_INTERVAL': 0, # in seconds,
    'AUTO_OPEN': False, # open chrome if new post arrives

    'SUBREDDIT': '',
}

log_file = open(config.get('LOG_FILE'), 'a+')

reddit = praw.Reddit(
    client_id=config.get("CLIENT_ID"),
    client_secret=config.get('CLIENT_SECRET'),
    user_agent=config.get('USER_AGENT')
)

last_post_created = None

err = {
    'hasError': False,
    'logged': False
}

while True:
    if(err['hasError'] and not err['logged']):
        err['logged'] = True
        log_file.write(f'--- {datetime.now()} ----\n')
    log_file.write('Error occured retrying...\n\n')

    try:
        for submission in reddit.subreddit(config.get('SUBREDDIT')).new(limit=1):
            err['err'], err['logged'] = False, False
            if(submission.created_utc != last_post_created):
                notification(submission.name, summary=submission.title)
                last_post_created = submission.created_utc

                if(config.get('AUTO_OPEN', False)):
                    webbrowser.open(
                        f'http://reddit.com/{submission.permalink}')

    except:
        err['err'] = True

    time.sleep(config.get('POLL_INTERVAL'))
