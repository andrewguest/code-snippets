#!/usr/bin/python3

import argparse
import zipfile
import os
import time
import shutil

def get_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", help = "Directory to backup")
    parser.add_argument("destination_dir", help = "Location to store backup")
    args = parser.parse_args()
    print("Source:", args.source_dir)
    print("Destination:", args.destination_dir)
    create_backup(args.source_dir, args.destination_dir)


def create_backup(source, destination):
    month = time.strftime("%m")
    day = time.strftime("%d")
    year = time.strftime("%Y")
    backup_date = month + "-" + day + "-" + year
    os.chdir(os.path.dirname(source))
    with zipfile.ZipFile(backup_date + '.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, filenames in os.walk(os.path.basename(source)):
            for name in filenames:
                name = os.path.join(root, name)
                name = os.path.normpath(name)
                zf.write(name, name)
    shutil.move(backup_date + '.zip', destination)


if __name__ == "__main__":
    get_cli_arguments()
