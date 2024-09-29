# this is modification of 001-X file to catch tasks that are still await
# in background after all other work is done and main coroutine is
# suposed to exit. Without mod. main coroutine exit before task1 is completed.
# Key Takeaway: two awaits in main coroutine run in sync (one after another)
# See my best solution in mian (commented)
import asyncio
from typing import List, Coroutine


class AsyncProcessor:
    def __init__(self) -> None:
        self.tasks: List[Coroutine[None, None, None]] = []

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
        task1 = asyncio.create_task(self.task1())
        self.tasks.append(task1)
        task2 = asyncio.create_task(self.task2())
        self.tasks.append(task2)

        print("Tasks started, but not waiting for them to finish...")

        # Do some other work while tasks are running
        for i in range(3):
            print(f"Doing other work {i + 1}")
            await asyncio.sleep(0.5)

    async def monitor_tasks(self):
        while self.tasks:
            print(f"Currently tracking {len(self.tasks)} tasks.")
            # REmove tasks that have completed
            done_tasks = [task for task in self.tasks if task.done()]
            for task in done_tasks:
                self.tasks.remove(task)
            await asyncio.sleep(0.5)  # Polling interval


async def main():
    processor = AsyncProcessor()

    await processor.run_tasks_without_waiting()
    await processor.monitor_tasks()  # will start monitoring after
    # .run_tasks_without_waiting complete

    # My best solution:
    # await asyncio.gather(
    #     processor.run_tasks_without_waiting(), processor.monitor_tasks()
    # )

    print("Main coroutine is done.")


# Run the event loop
asyncio.run(main())
