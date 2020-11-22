import threading


def worker():
    # Thread worker function
    print('Worker')


threads = []
for i in range(5):
    # 'worker' is the function that the worker threads
    #     will run when spawned.
    t = threading.Thread(target=worker)

    # Add each worker to the threads list
    threads.append(t)

    # Start the new thread
    t.start()
