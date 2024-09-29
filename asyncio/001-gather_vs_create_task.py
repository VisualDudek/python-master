# understand key diff between `asyncio.gather` and `asyncio.create_task`
# `.gather` waits for all coroutines to complete before continuing
# `.create_task` starts a coroutine in the background (it return a Task object
# immediately, allowing the coroutine to run tun the background without
# waiting for it to finish )
# in example coroutine task1 and task2 do not return payload, BUT it can
import asyncio


class AsyncProcessor:
    async def task1(self):
        print("Starting task 1...")
        await asyncio.sleep(2)
        # when run in background without await, will not end before
        # main coroutine ends
        print("Task 1 complete")

    async def task2(self):
        print("Starting task 2...")
        await asyncio.sleep(1)
        print("Task 2 complete")

    async def run_tasks_without_waiting(self):
        print("Running tasks without waiting...")

        # Create tasks and run them without awaiting
        asyncio.create_task(self.task1())
        asyncio.create_task(self.task2())

        print("Tasks started, but not waiting for them to finish...")

        # Do some other work while tasks are running
        for i in range(3):
            print(f"Doing other work {i + 1}")
            await asyncio.sleep(0.5)

    async def run_and_wait_to_complete(self):
        print("Running tasks and  waiting...")

        await asyncio.gather(self.task1(), self.task2())

        print("All Tasks completed...")

        # Do some other work while tasks are running
        for i in range(3):
            print(f"Doing other work {i + 1}")
            await asyncio.sleep(0.5)


async def main():
    processor = AsyncProcessor()

    # Try one of these:
    # await processor.run_tasks_without_waiting()
    await processor.run_and_wait_to_complete()

    print("Main coroutine is done.")


# Run the event loop
asyncio.run(main())
