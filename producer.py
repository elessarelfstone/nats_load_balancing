import asyncio
import random
from uuid import uuid4


from nats.aio.client import Client as NATS


async def run():
    nc = NATS()
    await nc.connect("nats://localhost:4222")
    session_num = str(uuid4())

    for i in range(1, 201):
        msg = f"Message: session - {session_num[:7]}, #{i}"
        await nc.publish("jobs", msg.encode())
        print(f"Published: {msg}")
        await asyncio.sleep(random.uniform(0.8, 1))  # simulate delay

    await nc.drain()

if __name__ == '__main__':
    asyncio.run(run())