import os
import concurrent.futures
import argparse

from bs4 import BeautifulSoup
import requests


###########################################
# Setup argument parser and add arguments #
###########################################
my_parser = argparse.ArgumentParser(prog='defconviddownloader.py', usage='%(prog)s [options] DefCon_number save_destination', description='Download videos from the specified Def Con')
my_parser.add_argument('-t', '--threads', type=int, help='Change the number of threads used to download videos with. Default is: 4 threads.', default=4, required=False)
my_parser.add_argument('DefCon_number', type=str, help='The DefCon number to download videos from')
my_parser.add_argument('save_destination', type=str, help='Destination to save the files to.')

args = my_parser.parse_args()


###############################################
# Define variables used for downloading files #
###############################################
url = 'https://media.defcon.org/DEF%20CON%20' + args.DefCon_number + '/DEF%20CON%20' + args.DefCon_number + '%20video%20and%20slides/'
# base_save_location = 'C:\\Users\\ag043542\\Videos\\Def Con\\26\\'
base_save_location = args.save_destination + '/DefCon_' + args.DefCon_number
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'}
links = []


#########################################################################
# Function to get, and format, the links for the appropriate .mp4 files #
#########################################################################
def get_video_links():
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    tags = soup.find('div', id='content').find_all('a')

    for tag in tags:
        link = tag.get('href')
        if link.endswith('.mp4'):
            full_url = url + link

            filename = link.replace('%20', ' ')
            filename = filename.replace('.mp4', '')
            filename = filename.split(' - ')
            filename = filename[2] + ' - ' + filename[1] + '.mp4'

            temp_list = (filename, full_url)
            links.append(temp_list)


#########################################################
# Function to perform the downloading of the .mp4 files #
#########################################################
def download_videos(url):
    nice_name, download_url = url
    file_save_location = base_save_location + nice_name

    if os.path.isfile(file_save_location):
        print('[+] ' + file_save_location + " already exists. Skipping...")
        exit
    else:
        print("[*] Downloading: " + nice_name)
        r = requests.get(download_url, stream=True, timeout=5, headers=headers)
        with open(file_save_location, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)


def main():

    #######################################################################
    # Check if the save directory already exists. If not, then create it. #
    #######################################################################
    if not os.path.exists(base_save_location):
        os.makedirs(base_save_location)
        print('[+] CREATED:', base_save_location)
    else:
        print('[*] Save location already exists:', base_save_location)

    get_video_links()

    ####################################################################
    # Start up to, 4 threads, at a time, to download files in parallel #
    ####################################################################
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(download_videos, links)


if __name__ == '__main__':
    main()
