import asyncio
import random
from nats.aio.client import Client as NATS


async def run():
    nc = NATS()
    await nc.connect("nats://localhost:4222")

    async def message_handler(msg):
        data = msg.data.decode()
        print(f"[Consumer] Received: {data}")
        await asyncio.sleep(random.uniform(0.05, 1.1))  # simulate processing time

    # 'workers' is the queue group name
    await nc.subscribe("jobs", queue="workers", cb=message_handler)

    print("Consumer ready (queue: workers)...")
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        await nc.drain()

if __name__ == '__main__':
    asyncio.run(run())