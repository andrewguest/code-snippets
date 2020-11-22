import json

# Open the JSON file
with open("json_format.json") as json_data_file:
    # Store the data from the JSON file in a variable named "data"
    data = json.load(json_data_file)

# For each key in "data"
# This equates to "b4298", "c4298", and "p4298" in the above json
for item in data:
    print(item)

# For each item in the "data" dictionary, in the "b4298" subdictionary
# This would equate to "servers" from the above JSON
for item in data["b4298"]:
    # For each value in the data[b4298][item] key/value pair
    # This equates to the "cphyprapp##" lines in the above JSON
    for x in data["b4298"][item]:
        # Print the value
        print("Item:", x)