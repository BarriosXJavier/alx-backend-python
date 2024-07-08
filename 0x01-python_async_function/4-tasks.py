import asyncio
from typing import List
from 1-task_wait_random import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Sort the delays in ascending order without using sort()
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays

# Running the event loop
if __name__ == "__main__":
    asyncio.run(main())
