import threading
import time
import logging


# Function for threads to run
def worker():
    # Print the assigned name of the thread instance.
    logging.debug('Starting')
    # Sleep for 0.2 seconds to simulate work being done.
    time.sleep(0.2)
    logging.debug('Exiting')


def my_service():
    logging.debug('Starting')
    time.sleep(0.3)
    logging.debug('Exiting')


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

"""
These three lines, each, create a thread in a slightly different way.

threading.Thread() <-- creates a thread.

name='my_service' & name='worker' <-- manually sets the name of the thread.
    (what shows up when you call 'threading.current_thread().getName()')

The third example leaves the 'Thread' class to create and set a name for the
    thread that is spawned.
"""
t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

"""
.start()  <-- Actually starts the thread
"""
w.start()
w2.start()
t.start()
