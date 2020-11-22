#!/usr/bin/python3

# Module for parsing arguments
import argparse

parser = argparse.ArgumentParser()

# Add an argument and save it in a variable named "src_dir"
# Also add description for -h (help) option
parser.add_argument("src_dir", help = "Directory to backup")

# Add an argument and save it in a variable named "dst_dir"
# Also add description for -h (help) option
parser.add_argument("dst_dir", help = "Location to store backup")

# Collect all of the arguments supplied on the command line
args = parser.parse_args()

print("Source:", args.src_dir)
print("Destination:", args.dst_dir)
