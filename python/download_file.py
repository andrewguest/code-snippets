import requests

url = "http://www.google.com/favicon.ico"


def is_downloadable(url):
    # Does the URL contain a downloaded resource?

    header = requests.head(url)
    header = header.headers
    content_type = header.get("content-type")

    if "text" in content_type.lower():
        return False
    elif "html" in content_type.lower():
        return False
    else:
        return True


def download_file(url):
    req = requests.get(url)
    # Download the file (favicon.ico) and save it as google.ico
    open("google.ico", "wb").write(req.content)
