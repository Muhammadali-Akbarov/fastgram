"""
the implementation of pubsub
"""
from app.bot.pubsub import IPubSub
from app.bot.services.external.faststream import client


class PubSub(IPubSub):
    """
    the implementation of pubsub
    """
    async def publish(self, topic, message):
        await client.publish(topic, message)


pubsub = PubSub()
