import requests
import os
import shutil
from multiprocessing.pool import ThreadPool

from pixiset_downloader_config import photoset_name, pictures_list, numOfThreads


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
}
save_location = "D:\\MyPictures\\temp\\" + photoset_name


def performDownload(url):

    filename, url = url
    print("{} from {}".format(filename, url))

    print("[+] Working on:", filename)
    resp = requests.get(url, stream=True)
    local_file = open(filename, "wb")
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)


if __name__ == "__main__":
    if not os.path.exists(save_location):
        os.makedirs(save_location)
        print("[!] Successfully created folder")
    else:
        print("[!] Save location already exists")

    os.chdir(save_location)
    print("[!] Using {} threads".format(numOfThreads))

    ThreadPool(numOfThreads).map(performDownload, pictures_list)
