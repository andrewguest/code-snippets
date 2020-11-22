#!/usr/bin/python3

import yaml

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print("Sections list: " + section)

# Printing the first item in "Fruits"
print("First item in Fruit:", cfg['fruits'][0])

# Printing the value associated with the key 'job' for the section "Bob"
print("Items in:", cfg['Bob']['job'])

print("Items in:", cfg['James'])
