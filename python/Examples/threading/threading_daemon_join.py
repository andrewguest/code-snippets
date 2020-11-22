import threading
import time
import logging


# Function for threads to run
def daemon():
    # Print the assigned name of the thread instance.
    logging.debug('Starting')
    # Sleep for 0.2 seconds to simulate work being done.
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)


"""
These three lines, each, create a thread in a slightly different way.

threading.Thread()
-creates a thread.

name=
-manually sets the name of the thread.
-(what shows up when you call 'threading.current_thread().getName()')

daemon=True
-Sets up the thread to run in the background, disconnected
    from the process that started (spawned) it.

Since 'd' is a 'daemon' thread, it will disconnect from the parent
    process before it has a chance to print it's "Exiting" message
    from the funtion.
    (NOTE: It will still execute all of the steps
    in the assigned function, the output just won't be visable to
    the parent process)
"""

d = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)

"""
.start()  <-- Actually starts the thread
"""
d.start()
t.start()

"""
.join()
-Waits for a daemon thread to finish before the parent process
completes.
-Blocks the parent process indefinitely.


Now 'd' will have a chance to log it's "Exiting" message.
"""
d.join()
t.join()
