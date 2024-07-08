import asyncio
import random
"""async basics"""
async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay time.

    Raises:
        ValueError: If max_delay is not a positive integer.
    """
    if max_delay <= 0:
        raise ValueError("max_delay must be a positive integer")

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
