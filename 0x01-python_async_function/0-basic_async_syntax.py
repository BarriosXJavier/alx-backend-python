#!/usr/bin/env python3 

"""
    asynchronous coroutine that takes in
    an integer argument (max_delay, with a
    default value of 10) named wait_random that waits for random seconds
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """ Takes random seconds"""
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay