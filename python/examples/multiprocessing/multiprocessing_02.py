#!/usr/bin/python3

import multiprocessing
import os

def info(conn):
    conn.send("Hello from {}\nppid = {}\npid={}".format(mp.current_process().name, os.getppid(), os.getpid()))
    conn.close()

if __name__ == '__main__':

    parent_conn, child_conn = multiprocessing.Pipe()
	# Set the target function for the new processes to run
    p = multiprocessing.Process(target=info, args=(child_conn,))
    # Set the process as a daemon to run in the background
	p.daemon = True
    p.start()
    print(parent_conn.recv())