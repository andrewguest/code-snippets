import asyncio

async def myCoroutine():
	print("Simple event loop example.")
	
def main():
    # Define an instance of an event loop
    loop = asyncio.get_event_loop()
	
    # Tell this event loop to run until all the tasks assigned
    # to it are complete. In this example just the execution of
    # our myCoroutine() coroutine.
    loop.run_until_complete(myCoroutine())
	
    # Tidying up our loop by calling close()
    loop.close()

if __name__ == '__main__':
    main()