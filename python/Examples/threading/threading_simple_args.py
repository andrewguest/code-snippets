import threading


def worker(num):
    # Thread worker function
    print('Worker: %s' % num)


threads = []
for i in range(5):
    """
    'worker' is the function that the worker threads
        will run when spawned.

    'args=(i,)' passes the 'i' variable to the 'worker'
        function, since that function is expecting
            something to be passed into it.
    """
    t = threading.Thread(target=worker, args=(i,))

    # Add each worker to the threads list
    threads.append(t)

    # Start the new thread
    t.start()
