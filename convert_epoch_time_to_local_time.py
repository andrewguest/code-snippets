import time


# seconds passed since epoch
# Change this to match your input
seconds = 1475035200

local_time = time.ctime(seconds)

print("Local time: {}".format(local_time))
