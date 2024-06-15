"""
the implementation of faststream
"""
from faststream import FastStream
from faststream.redis import RedisBroker

from app.bot.pubsub import IPubSub
from app.bot.settings.external.redis import REDIS_HOST, REDIS_PORT


broker = RedisBroker(f"redis://{REDIS_HOST}:{REDIS_PORT}")
app = FastStream(broker)


class FastStreamPubSub(IPubSub):
    """
    the implementation of faststream
    """
    async def publish(self, topic, message):
        await broker.connect()
        await broker.publish(topic, message)


client = FastStreamPubSub()
