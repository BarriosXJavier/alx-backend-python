import time
import asyncio
from 1-concurrent_coroutines import wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the average time per call.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time per call.
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n

# Running the event loop
if __name__ == "__main__":
    asyncio.run(main())
