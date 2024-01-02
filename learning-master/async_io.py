import asyncio
import threading


class Amar:
    def __init__(self):
        pass

    async def my_async_task(self):
        i = 0
        while not terminate_flag.is_set():
            print("Working asynchronously...  :   ", i)

            if i == 1000000:
                terminate_flag.set()
            i += 1


amar = Amar()


async def my_async_task():
    while not terminate_flag.is_set():
        print("Working asynchronously...")

        await asyncio.sleep(1)


def start_event_loop():
    global task
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(amar.my_async_task())
    print(task)
    loop.run_until_complete(task)


terminate_flag = threading.Event()
task = None

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        thread = threading.Thread(target=start_event_loop)

        thread.start()

        # Let the task run for a while
        terminate_flag.wait()

        # Set the termination flag to stop the task
        terminate_flag.set()

        # Wait for the task to complete
        if task:
            # task.cancel()
            loop.run_until_complete(task)
            task.cancel()

    except KeyboardInterrupt:
        terminate_flag.set()
