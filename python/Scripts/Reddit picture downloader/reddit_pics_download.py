import time
import os
import ssl
import threading

from dotenv import load_dotenv
import requests
import praw
import yaml

load_dotenv()

# Parsing YAML config file
with open("config.yaml", "r") as configFile:
    configuration_data = yaml.load(configFile)


print("*" * 75)
print("[+] Reading configuration file\n")
print(f"Subreddits: {configuration_data['subreddits']}")
print(f"Number of pics to download: {configuration_data['post_limit']}")
print(f"Save location: {configuration_data['save_location']}")
print("*" * 75)


# Setting up PRAW
if not os.environ.get("PYTHONHTTPSVERIFY", "") and getattr(
    ssl, "_create_unverified_context", None
):
    ssl._create_default_https_context = ssl._create_unverified_context

reddit = praw.Reddit(
    client_id=os.getenv("client_id"),
    client_secret=os.getenv("client_secret"),
    user_agent="picdownloader",
)


# To download photos from more subreddits, update the
# 'config.json' file ('subreddits' item)
list_of_subreddits = configuration_data["subreddits"]


def download_images(subreddit_name):
    print("Starting thread: {}".format(threading.current_thread().getName()))
    print("*" * 75)
    print("[+] Working on subreddit:", subreddit_name)
    print("-" * 50)
    subreddit = reddit.subreddit(subreddit_name)
    # To download more or fewer photos, update the
    # 'config.json' file ('post_limit' item)
    new_pics = subreddit.hot(limit=configuration_data["post_limit"])
    log_datetime = time.strftime("%Y-%m-%d %H:%M:%S")
    log_file = open(
        configuration_data["save_location"] + "%s\\log.txt" % subreddit_name, "a"
    )
    for submission in new_pics:
        log_file.write(
            "\nDate and time: "
            + log_datetime
            + "\n"
            + "Submission ID: "
            + submission.id
            + "\n"
            + "Submission URL: "
            + submission.url
            + "\n"
        )
        filename = (
            configuration_data["save_location"]
            + "%s\\" % subreddit_name
            + submission.url.split("/")[-1]
        )
        # if submission.url.endswith('.jpg') or submission.url.endswith('.png') or submission.url.endswith('.gif'):
        if submission.url.endswith(".jpg") or submission.url.endswith(".png"):
            if os.path.isfile(filename):
                log_file.write("File already exists. Skipping download.\n\n")
            else:
                print("Downloading:", filename)
                log_file.write("Downloading picture...\n\n")
                image = requests.get(submission.url, allow_redirects=True)
                with open(filename, "wb") as f:
                    f.write(image.content)
        else:
            log_file.write("Image not detected: " + submission.url + "\n\n")
    log_file.close()


if __name__ == "__main__":
    for entry in list_of_subreddits:
        t = threading.Thread(name=entry, target=download_images, args=(entry,))
        t.start()
